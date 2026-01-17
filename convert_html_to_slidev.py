#!/usr/bin/env python3
"""Convert Reveal.js HTML presentation to Slidev Markdown format"""

import re
from html.parser import HTMLParser
from pathlib import Path

class SlideParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides = []
        self.current_slide = []
        self.in_section = False
        self.in_code = False
        self.in_pre = False
        self.current_lang = "plaintext"
        self.code_buffer = []
        
    def handle_starttag(self, tag, attrs):
        if tag == "section":
            self.in_section = True
            self.current_slide = []
        elif tag == "pre" and self.in_section:
            self.in_pre = True
            self.code_buffer = []
            # Try to get language from code tag
            attrs_dict = dict(attrs)
            if "style" in attrs_dict:
                self.in_pre = True
        elif tag == "code" and self.in_pre:
            self.in_code = True
            attrs_dict = dict(attrs)
            if "class" in attrs_dict:
                class_str = attrs_dict["class"]
                match = re.search(r'language-(\w+)', class_str)
                if match:
                    self.current_lang = match.group(1)
        elif tag == "h1" and self.in_section:
            self.current_slide.append(("h1", ""))
        elif tag == "h2" and self.in_section:
            self.current_slide.append(("h2", ""))
        elif tag == "h3" and self.in_section:
            self.current_slide.append(("h3", ""))
        elif tag == "h4" and self.in_section:
            self.current_slide.append(("h4", ""))
        elif tag == "ul" and self.in_section:
            self.current_slide.append(("ul_start", ""))
        elif tag == "li" and self.in_section:
            self.current_slide.append(("li", ""))
        elif tag == "p" and self.in_section:
            self.current_slide.append(("p", ""))
        elif tag == "br":
            if self.in_section and not self.in_code:
                self.current_slide.append(("br", ""))
        elif tag == "strong" and self.in_section:
            self.current_slide.append(("strong", ""))
        elif tag == "div" and "mermaid" in dict(attrs).get("class", ""):
            self.current_slide.append(("mermaid_start", ""))
        elif tag == "table" and self.in_section:
            self.current_slide.append(("table_start", ""))
        elif tag == "tr" and self.in_section:
            self.current_slide.append(("tr", ""))
        elif tag == "th" and self.in_section:
            self.current_slide.append(("th", ""))
        elif tag == "td" and self.in_section:
            self.current_slide.append(("td", ""))
            
    def handle_endtag(self, tag):
        if tag == "section" and self.in_section:
            if self.code_buffer:
                self.current_slide.append(("code_end", "".join(self.code_buffer)))
                self.code_buffer = []
            self.in_section = False
            if self.current_slide:
                self.slides.append(self.current_slide)
            self.current_slide = []
        elif tag == "pre" and self.in_pre:
            self.in_pre = False
            self.in_code = False
        elif tag == "code" and self.in_code:
            self.in_code = False
        elif tag == "ul" and self.in_section:
            self.current_slide.append(("ul_end", ""))
        elif tag == "p" and self.in_section:
            self.current_slide.append(("p_end", ""))
        elif tag == "strong" and self.in_section:
            self.current_slide.append(("strong_end", ""))
        elif tag == "div":  # End of mermaid or other div
            pass
        elif tag == "table" and self.in_section:
            self.current_slide.append(("table_end", ""))
        elif tag == "tr" and self.in_section:
            self.current_slide.append(("tr_end", ""))
            
    def handle_data(self, data):
        if self.in_code:
            self.code_buffer.append(data)
        elif self.in_section and data.strip():
            if self.current_slide and self.current_slide[-1][0] in ("h1", "h2", "h3", "h4", "p", "li", "th", "td", "strong"):
                tag_type, content = self.current_slide[-1]
                self.current_slide[-1] = (tag_type, content + data.strip())
            elif not (self.current_slide and self.current_slide[-1][0] in ("ul_start", "ul_end", "tr", "tr_end", "table_start", "table_end", "br")):
                self.current_slide.append(("text", data.strip()))

def extract_mermaid_diagram(html_content, start_pos):
    """Extract mermaid diagram content from HTML"""
    mermaid_start = html_content.find("<div class=\"mermaid\">", start_pos)
    if mermaid_start == -1:
        return None
    
    mermaid_end = html_content.find("</div>", mermaid_start)
    if mermaid_end == -1:
        return None
    
    diagram_content = html_content[mermaid_start + len("<div class=\"mermaid\">"):mermaid_end].strip()
    return diagram_content

def extract_slides_with_regex(html_content):
    """Extract slides using regex to preserve mermaid diagrams"""
    slides = []
    
    # Split by section tags
    section_pattern = r'<section>(.*?)</section>'
    matches = re.finditer(section_pattern, html_content, re.DOTALL)
    
    for match in matches:
        section_content = match.group(1)
        slides.append(section_content)
    
    return slides

def clean_html_tags(text):
    """Remove remaining HTML tags"""
    # Remove style attributes
    text = re.sub(r'\s+style="[^"]*"', '', text)
    # Remove class attributes
    text = re.sub(r'\s+class="[^"]*"', '', text)
    # Remove other attributes
    text = re.sub(r'\s+\w+="[^"]*"', '', text)
    # Remove remaining tags
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()

def convert_html_slide_to_markdown(section_html):
    """Convert a single slide section from HTML to Markdown"""
    markdown = []
    
    # Extract mermaid diagrams
    mermaid_pattern = r'<div class="mermaid">(.*?)</div>'
    mermaid_matches = list(re.finditer(mermaid_pattern, section_html, re.DOTALL))
    
    # Remove mermaid divs temporarily
    section_clean = section_html
    for match in mermaid_matches:
        section_clean = section_clean.replace(match.group(0), f"__MERMAID_{len(mermaid_matches) - 1}__")
    
    # Extract tables
    table_pattern = r'<table[^>]*>(.*?)</table>'
    table_matches = list(re.finditer(table_pattern, section_clean, re.DOTALL))
    
    for match in table_matches:
        section_clean = section_clean.replace(match.group(0), f"__TABLE_{table_matches.index(match)}__")
    
    # Process headings
    h1_pattern = r'<h1[^>]*>(.*?)</h1>'
    h1_matches = re.finditer(h1_pattern, section_clean, re.DOTALL)
    for match in h1_matches:
        content = clean_html_tags(match.group(1))
        markdown.append(f"# {content}\n")
    
    h2_pattern = r'<h2[^>]*>(.*?)</h2>'
    h2_matches = re.finditer(h2_pattern, section_clean, re.DOTALL)
    for match in h2_matches:
        content = clean_html_tags(match.group(1))
        markdown.append(f"## {content}\n")
    
    h3_pattern = r'<h3[^>]*>(.*?)</h3>'
    h3_matches = re.finditer(h3_pattern, section_clean, re.DOTALL)
    for match in h3_matches:
        content = clean_html_tags(match.group(1))
        markdown.append(f"### {content}\n")
    
    h4_pattern = r'<h4[^>]*>(.*?)</h4>'
    h4_matches = re.finditer(h4_pattern, section_clean, re.DOTALL)
    for match in h4_matches:
        content = clean_html_tags(match.group(1))
        markdown.append(f"#### {content}\n")
    
    # Extract paragraphs
    p_pattern = r'<p[^>]*>(.*?)</p>'
    p_matches = re.finditer(p_pattern, section_clean, re.DOTALL)
    for match in p_matches:
        content = clean_html_tags(match.group(1)).strip()
        if content:
            markdown.append(f"{content}\n")
    
    # Extract lists
    ul_pattern = r'<ul[^>]*>(.*?)</ul>'
    ul_matches = re.finditer(ul_pattern, section_clean, re.DOTALL)
    for match in ul_matches:
        ul_content = match.group(1)
        li_pattern = r'<li[^>]*>(.*?)</li>'
        li_matches = re.finditer(li_pattern, ul_content, re.DOTALL)
        for li_match in li_matches:
            content = clean_html_tags(li_match.group(1)).strip()
            if content:
                markdown.append(f"- {content}\n")
    
    # Extract code blocks
    pre_pattern = r'<pre[^>]*><code[^>]*>(.*?)</code></pre>'
    pre_matches = re.finditer(pre_pattern, section_clean, re.DOTALL)
    for match in pre_matches:
        code_content = match.group(1).strip()
        # Try to detect language
        lang = "plaintext"
        markdown.append(f"```{lang}\n{code_content}\n```\n")
    
    # Replace placeholders with actual content
    result = "".join(markdown)
    
    # Add mermaid diagrams
    for idx, match in enumerate(mermaid_matches):
        diagram_content = match.group(1).strip()
        result = result.replace(f"__MERMAID_{idx}__", f"```mermaid\n{diagram_content}\n```\n")
    
    # Add tables
    for idx, match in enumerate(table_matches):
        table_html = match.group(1)
        table_md = convert_html_table_to_markdown(table_html)
        result = result.replace(f"__TABLE_{idx}__", table_md)
    
    return result.strip()

def convert_html_table_to_markdown(table_html):
    """Convert HTML table to Markdown"""
    rows = []
    tr_pattern = r'<tr[^>]*>(.*?)</tr>'
    tr_matches = re.finditer(tr_pattern, table_html, re.DOTALL)
    
    for tr_match in tr_matches:
        tr_content = tr_match.group(1)
        cells = []
        
        # Extract th and td
        cell_pattern = r'<(?:th|td)[^>]*>(.*?)</(?:th|td)>'
        cell_matches = re.finditer(cell_pattern, tr_content, re.DOTALL)
        
        for cell_match in cell_matches:
            cell_content = clean_html_tags(cell_match.group(1)).strip()
            cells.append(cell_content)
        
        if cells:
            rows.append("| " + " | ".join(cells) + " |")
    
    if rows:
        # Add separator after header
        if len(rows) > 1:
            header = rows[0]
            num_cols = len(header.split("|")) - 2
            separator = "| " + " | ".join(["---"] * num_cols) + " |"
            return "\n".join([header, separator] + rows[1:]) + "\n"
        else:
            return rows[0] + "\n"
    
    return ""

def main():
    # Read HTML file
    html_path = Path("/home/francois/dev/code/formation/index.html")
    html_content = html_path.read_text(encoding='utf-8')
    
    # Extract slides
    slides_html = extract_slides_with_regex(html_content)
    
    # Convert to Markdown
    markdown_slides = []
    
    for slide_html in slides_html:
        slide_md = convert_html_slide_to_markdown(slide_html)
        if slide_md:
            markdown_slides.append(slide_md)
    
    # Create Slidev presentation
    slidev_content = f"""---
theme: default
title: Architectures Back-end & Front-end
subtitle: Web, Mobile et IA
date: 2026-01-17
author: Formation continue
---

"""
    
    for slide_md in markdown_slides:
        slidev_content += f"{slide_md}\n\n---\n\n"
    
    # Write output file
    output_path = Path("/home/francois/dev/code/formation/slides.md")
    output_path.write_text(slidev_content, encoding='utf-8')
    
    print(f"✅ Conversion complete!")
    print(f"   - Total slides: {len(markdown_slides)}")
    print(f"   - Output: {output_path}")

if __name__ == "__main__":
    main()
