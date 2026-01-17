#!/bin/bash

# Slidev Presentation Setup Script
# This script prepares the Slidev presentation for use

echo "🚀 Slidev Presentation Setup"
echo "============================"
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 14+ from https://nodejs.org"
    exit 1
fi

echo "✅ Node.js version: $(node --version)"
echo "✅ npm version: $(npm --version)"
echo ""

# Check if slides.md exists
if [ ! -f "slides.md" ]; then
    echo "❌ slides.md not found. Make sure you're in the correct directory."
    exit 1
fi

echo "✅ slides.md found ($(wc -l < slides.md) lines)"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
npm install

echo ""
echo "✅ Setup complete!"
echo ""
echo "🎯 Next steps:"
echo "   1. Start development server:  npm run dev"
echo "   2. Open browser:              http://localhost:3030"
echo "   3. Build for production:      npm run build"
echo "   4. Export to PDF:             npm run export"
echo ""
echo "📚 For more info, see CONVERSION_GUIDE.md"
