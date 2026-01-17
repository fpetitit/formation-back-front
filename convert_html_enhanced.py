#!/usr/bin/env python3
"""Convert Reveal.js HTML presentation to Slidev Markdown format - Enhanced version"""

import re
from pathlib import Path

def extract_text_from_html(html_text):
    """Extract clean text from HTML, removing tags"""
    # Remove HTML comments
    html_text = re.sub(r'<!--.*?-->', '', html_text, flags=re.DOTALL)
    # Remove script and style tags
    html_text = re.sub(r'<script[^>]*>.*?</script>', '', html_text, flags=re.DOTALL | re.IGNORECASE)
    html_text = re.sub(r'<style[^>]*>.*?</style>', '', html_text, flags=re.DOTALL | re.IGNORECASE)
    # Remove tags but keep content
    html_text = re.sub(r'<[^>]+>', '', html_text)
    # Clean up whitespace
    html_text = re.sub(r'\n\s*\n', '\n', html_text)
    return html_text.strip()

def extract_mermaid_diagram(section_html):
    """Extract mermaid diagram from section"""
    mermaid_match = re.search(r'<div class="mermaid">\s*(.*?)\s*</div>', section_html, re.DOTALL)
    if mermaid_match:
        return mermaid_match.group(1).strip()
    return None

def extract_table_html(section_html):
    """Extract HTML table and convert to markdown"""
    table_match = re.search(r'<table[^>]*>(.*?)</table>', section_html, re.DOTALL)
    if not table_match:
        return None
    
    table_html = table_match.group(1)
    rows = []
    
    # Extract rows
    for row_match in re.finditer(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL):
        row_html = row_match.group(1)
        cells = []
        
        # Extract cells (both th and td)
        for cell_match in re.finditer(r'<(?:th|td)[^>]*>(.*?)</(?:th|td)>', row_html, re.DOTALL):
            cell_content = re.sub(r'<[^>]+>', '', cell_match.group(1)).strip()
            cells.append(cell_content)
        
        if cells:
            rows.append('| ' + ' | '.join(cells) + ' |')
    
    if not rows:
        return None
    
    # Add separator after first row
    if len(rows) > 1:
        num_cols = len(rows[0].split('|')) - 2
        separator = '| ' + ' | '.join(['---'] * num_cols) + ' |'
        return '\n'.join([rows[0], separator] + rows[1:])
    
    return rows[0]

def process_slide_html(section_html):
    """Process a single section/slide"""
    lines = []
    
    # Extract headings
    for h_match in re.finditer(r'<h([1-4])[^>]*>(.*?)</h\1>', section_html, re.DOTALL):
        level = int(h_match.group(1))
        content = extract_text_from_html(h_match.group(2)).strip()
        if content:
            lines.append('#' * level + ' ' + content)
            lines.append('')
    
    # Extract paragraphs (but not in divs with special classes)
    for p_match in re.finditer(r'<p[^>]*>(.*?)</p>', section_html, re.DOTALL):
        content = extract_text_from_html(p_match.group(1)).strip()
        if content and not content.startswith('<'):
            lines.append(content)
            lines.append('')
    
    # Extract unordered lists
    for ul_match in re.finditer(r'<ul[^>]*>(.*?)</ul>', section_html, re.DOTALL):
        ul_content = ul_match.group(1)
        for li_match in re.finditer(r'<li[^>]*>(.*?)</li>', ul_content, re.DOTALL):
            li_content = extract_text_from_html(li_match.group(1)).strip()
            if li_content:
                lines.append('- ' + li_content)
        lines.append('')
    
    # Extract code blocks
    for code_match in re.finditer(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', section_html, re.DOTALL):
        code_content = code_match.group(1).strip()
        lang = 'plaintext'
        # Try to detect language from class
        class_match = re.search(r'language-(\w+)', section_html[max(0, code_match.start()-100):code_match.start()])
        if class_match:
            lang = class_match.group(1)
        lines.append(f'```{lang}')
        lines.append(code_content)
        lines.append('```')
        lines.append('')
    
    # Extract mermaid diagrams
    mermaid = extract_mermaid_diagram(section_html)
    if mermaid:
        lines.append('```mermaid')
        lines.append(mermaid)
        lines.append('```')
        lines.append('')
    
    # Extract tables
    table_md = extract_table_html(section_html)
    if table_md:
        lines.append(table_md)
        lines.append('')
    
    # Clean up empty lines
    result = '\n'.join(lines).strip()
    
    # Remove multiple consecutive empty lines
    result = re.sub(r'\n\n\n+', '\n\n', result)
    
    return result

def main():
    """Main conversion function"""
    # Read HTML file
    html_path = Path('/home/francois/dev/code/formation/index.html')
    html_content = html_path.read_text(encoding='utf-8')
    
    # Extract all sections (slides)
    slides = []
    for section_match in re.finditer(r'<section[^>]*>(.*?)</section>', html_content, re.DOTALL):
        section_html = section_match.group(1)
        slide_md = process_slide_html(section_html)
        if slide_md:
            slides.append(slide_md)
    
    # Create Slidev presentation with frontmatter
    slidev_md = """---
theme: default
title: Architectures Back-end & Front-end
subtitle: Web, Mobile et IA
date: 2026-01-17
layout: cover
---

"""
    
    # Add slides with proper separator
    for i, slide in enumerate(slides):
        slidev_md += slide + '\n\n---\n\n'
    
    # Write output
    output_path = Path('/home/francois/dev/code/formation/slides.md')
    output_path.write_text(slidev_md, encoding='utf-8')
    
    print(f'✅ Conversion complete!')
    print(f'   - Total slides: {len(slides)}')
    print(f'   - Output file: {output_path}')
    print(f'   - File size: {len(slidev_md)} bytes')

if __name__ == '__main__':
    main()
