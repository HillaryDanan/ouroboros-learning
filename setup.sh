#!/bin/bash

# Setup script for Ouroboros Learning Framework
# Hillary Danan - August 2025

echo "🐍♾️ OUROBOROS LEARNING FRAMEWORK SETUP ♾️🐍"
echo "============================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Create virtual environment
echo -e "${BLUE}Creating virtual environment...${NC}"
python3 -m venv venv

# Activate virtual environment
echo -e "${BLUE}Activating virtual environment...${NC}"
source venv/bin/activate

# Upgrade pip
echo -e "${BLUE}Upgrading pip...${NC}"
pip install --upgrade pip

# Install requirements
echo -e "${BLUE}Installing requirements...${NC}"
pip install -r requirements.txt

# Create directory structure
echo -e "${BLUE}Creating directory structure...${NC}"
mkdir -p data results plots notebooks tests src

# Create .env file template if it doesn't exist
if [ ! -f .env ]; then
    echo -e "${BLUE}Creating .env template...${NC}"
    cat > .env << EOL
# API Keys for Model Access
# Uncomment and add your keys to enable actual model calls

# OPENAI_API_KEY=your_openai_key_here
# ANTHROPIC_API_KEY=your_anthropic_key_here
# GOOGLE_API_KEY=your_google_key_here

# Configuration
DEBUG=False
LOG_LEVEL=INFO
EOL
    echo -e "${YELLOW}Remember to add your API keys to .env file!${NC}"
fi

# Create __init__.py files
touch src/__init__.py
touch tests/__init__.py

# Make run script executable
chmod +x run_ouroboros_analysis.py

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "To run the analysis:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Run analysis: python run_ouroboros_analysis.py"
echo ""
