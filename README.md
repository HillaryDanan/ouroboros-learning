# Ouroboros Learning Framework

## Phase Distribution Analysis in GPT-3.5: Quantifying Model Behavior

**Hillary Danan** | August 2025

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Data](https://img.shields.io/badge/Responses-1000-green.svg)](data/)
[![Significance](https://img.shields.io/badge/p--value-0.038-yellow.svg)](results/)

### 🎯 Finding: Non-Uniform Phase Distribution in GPT-3.5

**GPT-3.5 exhibits significant phase preferences** (p=0.038), with integration dominating at 38.6% while transformation remains suppressed at 9.7%. This quantifies what users perceive as "mechanical" behavior.

- 📊 **1,000 GPT-3.5 responses analyzed** (50 sessions × 20 prompts)
- 📈 **Statistically significant patterns** (p=0.038)
- 🔄 **57.9% phase transition rate** with maintained coherence (0.56±0.10)
- ✅ **Synthetic validation** proves mathematical framework

## 📊 Data

### Collected
- ✅ **GPT-3.5**: 50 complete sessions (1,000 responses) - 100% success rate
- ⚠️ **Claude-3**: Partial data (~30 sessions) - 70% success rate, incomplete
- ❌ **Gemini-1.5**: Minimal data (4 responses) - 99% API failure rate

### What The Data Shows
```
GPT-3.5 Phase Distribution (n=1,000):
Integration:     38.6% ████████████████
Consumption:     29.9% ████████████
Transformation:   9.7% ████
Generation:      21.8% █████████

Statistical Test: p = 0.038 (significant)
```

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/HillaryDanan/ouroboros-learning.git
cd ouroboros-learning

# Setup environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run synthetic validation (no API keys needed!)
python synthetic_data_validation.py

# Analyze existing GPT-3.5 data
python analyze_50_sessions_final.py

# With API keys (optional - for reproduction)
cp .env.example .env
# Add your keys to .env
python test_apis.py
```

### Primary Finding
GPT-3.5 shows non-uniform phase distribution (p=0.038) with clear preferences:
- **Over-representation**: Integration (38.6% vs 25% expected)
- **Under-representation**: Transformation (9.7% vs 25% expected)

### Methodology
1. Collected 20-response conversations with designed prompts
2. Classified responses into four phases using linguistic markers
3. Analyzed phase distributions and transitions
4. Validated findings with synthetic data

## 📈 Key Results

### Statistical Validation
- **p-value**: 0.038 (statistically significant)
- **Effect**: Non-uniform phase distribution
- **Coherence**: 0.56 ± 0.10 (maintained despite transitions)
- **Transition rate**: 57.9% (dynamic but avoiding transformation)

### API Constraints as Data
The differential API failure rates revealed architectural insights:
- GPT-3.5: 100% success (robust)
- Claude-3: 70% success (moderate constraints)
- Gemini-1.5: 1% success (extreme constraints)

## 💼 Why This Matters

### For AI Understanding
- **Quantifies user perceptions**: "Mechanical" = high integration, low transformation
- **Reveals behavioral patterns**: Not just what models say, but how they think
- **Provides measurable metrics**: Beyond performance benchmarks

### For Applications
- **Model selection**: Choose based on phase requirements
- **Prompt engineering**: Target specific phases for desired outputs
- **Behavioral prediction**: Understand model tendencies

## 📚 Repository Structure

```
ouroboros-learning/
├── data/
│   ├── ouroboros_gpt-3.5-turbo_*.json  # 1,000 responses
│   ├── ouroboros_claude_*.json         # Partial data
│   └── synthetic_ouroboros_*.json      # Validation data
├── results/
│   ├── ouroboros_report_*.txt          # Statistical analyses
│   ├── fixed_analysis_*.csv            # Corrected metrics
│   └── synthetic_validation_*.csv      # Mathematical validation
├── plots/
│   ├── neurips_main_figure_*.png       # p=0.038 visualization
│   ├── ouroboros_*_example.png         # Phase patterns
│   └── synthetic_validation_*.png      # Framework validation
├── src/
│   ├── ouroboros_analyzer.py           # Core analysis
│   ├── ouroboros_visualizer.py         # Visualizations
│   └── config.py                       # Configuration
├── papers/
│   ├── neurips_2026.md                 # Conference paper
│   └── arxiv_ouroboros.md              # Extended version
└── synthetic_data_validation.py         # Mathematical proof
```

## 🔍 Honest Assessment

### What Worked
- ✅ GPT-3.5 analysis is complete and statistically significant
- ✅ Synthetic validation proves the mathematical framework
- ✅ Phase classification methodology is reproducible
- ✅ Findings explain user perceptions quantitatively

### What Didn't
- ❌ Comprehensive comparison across models (API constraints)
- ⚠️ Claude data is partial but suggestive
- ❌ Gemini data insufficient for analysis
- ⚠️ Single temperature setting (0.7)

### What It Means
This is primarily a **GPT-3.5 behavioral study** with a validated theoretical framework that can be extended to other models when API access permits.

## 📊 Visualizations

Key plots available in `/plots/`:
- **Phase distribution bars**: Shows 38.6% integration dominance
- **Statistical validation**: p=0.038 significance test
- **Coherence evolution**: 0.56±0.10 stability
- **Synthetic validation**: Mathematical framework confirmation

## 📚 Papers

- [NeurIPS Submission](papers/neurips_2026.md) - Focused empirical findings
- [ArXiv Extended](papers/arxiv_ouroboros.md) - Complete methodology and context

## 🤝 Future Work

- Complete comparative analysis when API access improves
- Investigate temperature effects on phase distribution
- Develop phase-aware prompting strategies
- Connect phases to attention mechanisms

## 📜 Citation

```bibtex
@software{danan2025ouroboros,
  author = {Danan, Hillary},
  title = {Phase Distribution Analysis in GPT-3.5: Quantifying Model Behavior},
  year = {2025},
  url = {https://github.com/HillaryDanan/ouroboros-learning}
}
```

## 🙏 Acknowledgments

Self-funded research driven by curiosity about AI behavior. The discovery that measurable patterns underlie intuitive perceptions validates the investigation despite API constraints.

## 📝 License

MIT License - See [LICENSE](LICENSE) for details

---

**Contact**: hillarydanan@gmail.com | [GitHub](https://github.com/HillaryDanan)

<4577> <45774EVER> 🐍♾️
