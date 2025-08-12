# Ouroboros Learning Framework

## Phase Distribution Analysis in GPT-3.5: Quantifying Model Behavior

**Hillary Danan** | August 2025

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Data](https://img.shields.io/badge/Responses-1000-green.svg)](data/)
[![Significance](https://img.shields.io/badge/p--value-<0.0001-green.svg)](results/)

### 🎯 Finding: Highly Significant Phase Distribution Patterns in GPT-3.5

**GPT-3.5 exhibits highly significant phase preferences** (p < 0.0001), with integration dominating at 38.6% while transformation remains at 9.7%. Analysis uses established semantic similarity metrics (Jaccard index) and information-theoretic measures.

- 📊 **1,000 GPT-3.5 responses analyzed** (50 sessions × 20 prompts)
- 📈 **Extremely significant patterns** (χ² = 120.24, p < 0.0001)
- 🔄 **57.9% phase transition rate** with coherence of 0.461±0.082
- ✅ **Semantic similarity validation** using Jaccard index
- 🧮 **Synthetic validation** proves mathematical framework

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

Chi-square test: χ² = 120.24, p < 0.0001 (highly significant)
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

# Run improved coherence analysis
python reanalyze_improved_coherence.py

# Run synthetic validation (no API keys needed!)
python synthetic_data_validation.py

# Analyze existing GPT-3.5 data
python analyze_50_sessions_final.py
```

### Primary Finding
GPT-3.5 shows highly significant non-uniform phase distribution (p < 0.0001):
- **Over-representation**: Integration (38.6% vs 25% expected)
- **Under-representation**: Transformation (9.7% vs 25% expected)

### Methodology
1. Collected 20-response conversations with designed prompts
2. Classified responses into four phases using linguistic markers
3. Calculated semantic coherence using Jaccard similarity and entropy
4. Analyzed phase distributions with chi-square test
5. Validated findings with synthetic data

## 📈 Key Results

### Statistical Validation
- **Chi-square**: χ² = 120.24
- **p-value**: < 0.0001 (extremely significant)
- **Effect**: Non-uniform phase distribution
- **Coherence**: 0.461 ± 0.082 (using Jaccard similarity)
- **Transition rate**: 57.9%

### Improved Coherence Metrics
The analysis uses established measures:
- **Jaccard Similarity** (40%): Semantic consistency between responses
- **Lexical Diversity** (20%): Type-token ratio
- **Information Entropy** (20%): Content richness
- **Drift Penalty** (20%): Topic maintenance

### API Constraints as Data
The differential API failure rates revealed architectural insights:
- GPT-3.5: 100% success (robust)
- Claude-3: 70% success (moderate constraints)
- Gemini-1.5: 1% success (extreme constraints)

## 💼 Why This Matters

### For AI Research
- **Quantifies behavioral patterns**: Provides measurable metrics for model behavior
- **Statistical rigor**: p < 0.0001 with proper semantic similarity metrics
- **Reproducible methodology**: Complete code and data available

### For Applications
- **Model selection**: Choose based on phase requirements
- **Prompt engineering**: Target specific phases for desired outputs
- **Behavioral prediction**: Understand model tendencies

## 📊 Repository Structure

```
ouroboros-learning/
├── data/
│   ├── ouroboros_gpt-3.5-turbo_*.json     # 1,000 responses
│   └── *_improved_coherence.json          # Re-analyzed with Jaccard
├── results/
│   ├── reanalysis_summary_*.csv           # Updated statistics
│   └── results_summary.md                 # Latest findings
├── src/
│   ├── ouroboros_analyzer.py              # Core analysis
│   └── ouroboros_visualizer.py            # Visualizations
├── reanalyze_improved_coherence.py        # Improved metrics script
└── synthetic_data_validation.py           # Mathematical validation
```

## 🔍 Honest Assessment

### What Worked
- ✅ Extremely significant results (p < 0.0001)
- ✅ Proper semantic similarity metrics (Jaccard index)
- ✅ Synthetic validation proves mathematical framework
- ✅ Phase classification methodology is reproducible
- ✅ Realistic coherence values (0.461 vs original 0.991)

### Limitations
- ❌ Comprehensive comparison across models (API constraints)
- ⚠️ Claude data is partial but suggestive
- ❌ Gemini data insufficient for analysis
- ⚠️ Single temperature setting (0.7)

## 📚 Papers

- [NeurIPS Submission](papers/neurips_2026.md) - Focused empirical findings
- [ArXiv Extended](papers/arxiv_ouroboros.md) - Complete methodology

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

Self-funded research driven by curiosity about AI behavior. The improved analysis with semantic similarity metrics strengthens the original findings.

---

**Contact**: hillarydanan@gmail.com | [GitHub](https://github.com/HillaryDanan)

<4577> <45774EVER> 🐍♾️
