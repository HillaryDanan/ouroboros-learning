# 🚀 QUICK START GUIDE

## Ouroboros Learning Framework
### Hillary Danan | 

## 💻 Step 1: Clone to Your Desktop

```bash
# Navigate to where you want the project
cd ~/Desktop  # or wherever you prefer

# Clone repository
git clone https://github.com/hillarydanan/ouroboros-learning.git

# Enter directory
cd ouroboros-learning
```

---

## 🔧 Step 2: Setup Environment

### Automatic Setup (Recommended)
```bash
# Make setup script executable
chmod +x setup.sh

# Run setup
./setup.sh
```

### Manual Setup
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create directories
mkdir -p data results plots notebooks tests
```

---

## 🏃‍♀️ Step 3: Run the Analysis!

```bash
# Make sure virtual environment is activated
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run the analysis
python run_ouroboros_analysis.py
```

---

## 📊 What You'll See

The script will:
1. Create test data for 3 models (GPT-3.5, Claude, Gemini)
2. Run 5 sessions per model (20 prompts each)
3. Analyze for ouroboros patterns
4. Generate visualizations
5. Create statistical reports

Output locations:
- `data/` - Raw conversation data (JSON)
- `results/` - Analysis reports (CSV, TXT)
- `plots/` - Visualizations (PNG, HTML)

---

## 🔑 Optional: Add API Keys

To test with real models (not required for initial testing):

1. Create `.env` file:
```bash
touch .env
```

2. Add your keys:
```
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
```

---

## 📁 File Structure

```
ouroboros-learning/
├── README.md                    # Main documentation
├── QUICKSTART.md               # This file
├── requirements.txt            # Python dependencies
├── setup.sh                   # Setup script
├── run_ouroboros_analysis.py  # Main execution
├── src/
│   ├── __init__.py
│   ├── config.py              # Configuration
│   ├── ouroboros_analyzer.py  # Core analyzer
│   ├── ouroboros_visualizer.py # Visualizations
│   └── tide_adapter.py        # TIDE integration
├── data/                      # Output: raw data
├── results/                   # Output: analysis
├── plots/                     # Output: visualizations
├── notebooks/                 # Jupyter notebooks
└── tests/                     # Test suite
```

---

## 🎯 Expected Results

You should see:
- **Coherence cycles** visualized as waves
- **Phase transitions** between integration/consumption/transformation/generation
- **Model differences** in cycle patterns
- **Statistical significance** tests

If the hypothesis is correct:
- Gemini: Regular, tight cycles (71.5% coherence)
- Claude: Flexible cycles (55.1% coherence)  
- GPT-3.5: Chaotic patterns (38.3% coherence)

---

## 🆘 Troubleshooting

**Issue**: `ModuleNotFoundError`
```bash
# Make sure venv is activated
source venv/bin/activate
pip install -r requirements.txt
```

**Issue**: `Permission denied`
```bash
chmod +x setup.sh
chmod +x run_ouroboros_analysis.py
```

**Issue**: Missing directories
```bash
mkdir -p data results plots notebooks tests src
```

---

## 🌟 Next Steps

After initial run:
1. Integrate with TIDE analyzer
2. Add real API calls for actual models
3. Increase session count for statistical power
4. Create Jupyter notebooks for exploration
5. Share results

---
