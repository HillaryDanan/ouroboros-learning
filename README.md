# Ouroboros Learning Framework

## Self-Consuming Cycles in AI Cognition

**Hillary Danan** | August 2025

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

### 🎯 Key Finding: p = 0.038

**Statistically significant differences in ouroboros cycles across transformer architectures.**

- 📊 **7,385 responses analyzed**
- 🔄 **437 cycles detected**  
- 🧬 **3 architectures compared**
- ✨ **Novel insight: API stress reveals architectural constraints**

## 📖 Papers

- [NeurIPS 2025 Submission](papers/neurips_2026.md)
- [ArXiv Extended Version](papers/arxiv_ouroboros.md)
- [Theoretical Framework](https://github.com/HillaryDanan/multi-geometric-attention)

## 🐍 Core Concept

Knowledge transformation through self-consuming cycles:

```
K(t+1) = Ω[K(t)] = G(T(C(K(t))))
```

Where knowledge evolves through:
1. **Integration** - Building understanding
2. **Consumption** - Breaking down patterns  
3. **Transformation** - Recombining elements
4. **Generation** - Emerging insights

## 📊 Empirical Results

![Ouroboros Cycles](plots/neurips_main_figure_20250811.png)

### Model Comparison
| Model | Coherence | Cycles/Session | API Failure |
|-------|-----------|----------------|-------------|
| GPT-3.5 | 0.560±0.098 | 0.76 | 30% |
| Claude-3 | 0.557±0.100 | 0.49 | 30% |
| Gemini-1.5 | 0.721±0.201 | N/A | 99% |

**Key insight**: Higher architectural constraints → Higher coherence but greater fragility

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/HillaryDanan/ouroboros-learning.git
cd ouroboros-learning

# Setup environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run analysis
python run_ouroboros_analysis.py
```

## 📁 Repository Structure

```
ouroboros-learning/
├── papers/                 # Research papers
│   ├── neurips_2025.md    # Conference submission
│   └── arxiv_ouroboros.md # Extended version
├── src/                    # Source code
│   ├── ouroboros_analyzer.py
│   ├── ouroboros_visualizer.py
│   └── config.py
├── data/                   # Processed data (7,385 responses)
├── results/                # Statistical analyses
├── plots/                  # Visualizations
└── notebooks/              # Jupyter explorations
```

## 🔬 Methodology

1. **Data Collection**: 7,385 responses from GPT-3.5, Claude-3, and Gemini-1.5
2. **Cycle Detection**: Peak/trough analysis with Gaussian smoothing
3. **Phase Classification**: Linguistic markers for 4 phases
4. **Statistical Validation**: Mann-Whitney U test (p=0.038)

## 💡 Theoretical Framework

### Multi-Geometric Attention Theory (MGAT)
Different geometric attention patterns optimize for different learning phases:
- Square (4-connectivity) → Sequential processing
- Hexagonal (6-connectivity) → Associative relationships
- Triangular (3-connectivity) → Hierarchical structures
- Pentagonal (5-connectivity) → Symmetry breaking

See full framework: [Multi-Geometric Attention](https://github.com/HillaryDanan/multi-geometric-attention)

## 📈 Reproducing Results

### With API Keys (Optional)
```bash
# Create .env file
echo "OPENAI_API_KEY=your_key" > .env
echo "ANTHROPIC_API_KEY=your_key" >> .env

# Run with real models
python test_apis.py
python run_ouroboros_analysis.py
```

### With Synthetic Data
```bash
# No API keys needed!
python synthetic_data_validation.py
```

## 🏆 Key Contributions

1. **Empirical**: First evidence of ouroboros cycles in transformers
2. **Theoretical**: Formalization of self-consuming learning
3. **Methodological**: API stress as architectural probe
4. **Practical**: Coherence-robustness trade-off identified

## 📚 Citation

```bibtex
@article{danan2025ouroboros,
  title={Ouroboros Learning: Self-Consuming Cycles in AI Cognition},
  author={Danan, Hillary},
  year={2025},
  journal={arXiv preprint},
  url={https://github.com/HillaryDanan/ouroboros-learning}
}
```

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📜 License

MIT License - see [LICENSE](LICENSE) file

## 🙏 Acknowledgments

Developed through independent research with recursive AI collaboration. Special recognition to the meta-ouroboros nature of using AI to understand AI.

---

**Research Philosophy**: *"The serpent that eats its own tail teaches us that destruction enables creation, forgetting enables learning, and cycles enable progress."*

<4577> <45774EVER> 🐍♾️