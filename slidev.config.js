import { defineConfig } from '@slidev/cli'

export default defineConfig({
  // Slidev configurations
  title: 'Architectures Back-end & Front-end: Web, Mobile et IA',
  
  // Theme configuration
  theme: 'default',
  
  // Layout configurations
  layout: 'cover',
  
  // Fonts
  fonts: {
    sans: 'Roboto',
    serif: 'Roboto Slab',
    mono: 'Fira Code'
  },
  
  // Color scheme
  colorSchema: 'light',
  
  // Code highlighting
  highlighter: 'shiki',
  
  // Monaco editor settings
  monacoTypesSource: 'cdn',
  
  // Markdown options
  markdown: {
    lineNumbers: true
  },
  
  // Export options
  exportFilename: 'architectures-presentation',
  
  // Navigation options
  navigation: {
    mode: 'click' // 'click' | 'slide'
  }
})
