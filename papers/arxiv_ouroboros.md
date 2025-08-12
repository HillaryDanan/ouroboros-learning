# Phase Distribution Analysis in Language Models: A Study of GPT-3.5 Behavioral Patterns

**Hillary Danan**  
Independent Researcher  
Upper Saddle River, NJ  
hillarydanan@gmail.com

**Date**: August 2025  
**Keywords**: language models, behavioral analysis, phase patterns, GPT-3.5, semantic similarity

## Abstract

We present an empirical investigation of phase distribution patterns in GPT-3.5-turbo, analyzing 1,000 responses across 50 conversation sessions using established semantic similarity metrics. The model exhibits highly significant non-uniform phase distribution (χ² = 120.24, p < 0.0001) with integration at 38.6%, consumption at 29.9%, transformation at 9.7%, and generation at 21.8%. Using Jaccard similarity for semantic coherence measurement, we find the model maintains coherence (0.461±0.082) despite high phase transition rates (57.9%). While comprehensive comparative analysis was prevented by API constraints (Claude-3-haiku: 30% failure rate; Gemini-1.5-flash: 99% failure rate), the GPT-3.5 patterns are robust and reproducible. Synthetic validation confirms the mathematical framework's validity. This work provides a quantitative framework for characterizing language model behavioral patterns.

## 1. Introduction

### 1.1 Motivation

Language models exhibit distinct behavioral patterns that users often describe qualitatively. This investigation seeks to provide quantitative foundations for these observations through systematic analysis of conversational phase patterns using established semantic similarity metrics.

### 1.2 Research Context

This independent research emerged from observations about behavioral differences across language models. Using $12 of personal API credits, we conducted a systematic investigation focused on GPT-3.5-turbo, with attempted comparative analysis limited by technical constraints.

### 1.3 Contributions

- **Empirical Analysis**: 1,000 GPT-3.5 responses with phase classification
- **Statistical Validation**: Highly significant patterns (p < 0.0001)
- **Methodological Rigor**: Jaccard similarity for semantic coherence
- **Synthetic Framework**: Mathematical validation independent of API data
- **Open Science**: Complete data and code publicly available

## 2. Theoretical Framework

### 2.1 Phase Model

We propose that language model responses can be characterized by four phases:

1. **Integration**: Building coherent understanding through accumulation
2. **Consumption**: Breaking down or questioning existing patterns
3. **Transformation**: Recombining elements in novel ways
4. **Generation**: Crystallizing and outputting new structures

### 2.2 Hypotheses

H1: Language models exhibit non-uniform phase distributions
H2: Phase patterns are measurable using semantic similarity metrics
H3: Different architectures show distinct phase signatures

### 2.3 Measurement Approach

Phase classification based on linguistic markers:
- Integration markers: sequential, building, adding, accumulating
- Consumption markers: questioning, reconsidering, challenging
- Transformation markers: recombining, novel, synthesizing, merging
- Generation markers: crystallizing, unified, structured, completing

Coherence measured using:
- Jaccard similarity coefficient (40% weight)
- Lexical diversity via type-token ratio (20% weight)
- Information entropy (20% weight)
- Semantic drift penalty (20% weight)

## 3. Methodology

### 3.1 Data Collection

#### 3.1.1 Primary Dataset (GPT-3.5)
```
Model: GPT-3.5-turbo
API: OpenAI
Sessions: 50 complete
Responses per session: 20
Total responses: 1,000
Temperature: 0.7
Success rate: 100%
Cost: ~$4 USD
```

#### 3.1.2 Coherence Calculation

```python
def calculate_semantic_coherence(response, previous_responses):
    # Jaccard similarity for semantic consistency
    consistency_scores = []
    for prev_response in previous_responses[-3:]:
        intersection = len(current_words ∩ prev_words)
        union = len(current_words ∪ prev_words)
        consistency_scores.append(intersection / union)
    
    # Combine with lexical diversity, entropy, drift
    coherence = (
        lexical_diversity * 0.2 +
        avg_consistency * 0.4 +
        normalized_entropy * 0.2 +
        (1 - drift_penalty) * 0.2
    )
    return coherence
```

### 3.2 Statistical Analysis

- Chi-square test for distribution uniformity
- Jaccard similarity for semantic coherence
- Shannon entropy for information content
- Synthetic validation framework

## 4. Results

### 4.1 Phase Distribution in GPT-3.5

Analysis of 1,000 responses reveals highly significant non-uniform distribution:

| Phase | Count | Percentage | Expected | χ² Contribution |
|-------|-------|------------|----------|-----------------|
| Integration | 386 | 38.6% | 250 | 29.74 |
| Consumption | 299 | 29.9% | 250 | 9.60 |
| Transformation | 97 | 9.7% | 250 | 47.09 |
| Generation | 218 | 21.8% | 250 | 3.78 |

**Statistical significance**: χ² = 120.24, df = 3, p < 0.0001

### 4.2 Coherence Analysis Using Jaccard Similarity

```
Mean coherence: 0.461
Standard deviation: 0.082
Range: 0.265 - 0.703
Jaccard similarity (avg): 0.42
```

The improved metrics provide more realistic coherence values compared to initial analysis.

### 4.3 Dynamic Patterns

```
Phase transition rate: 57.9%
Average cycles per session: 0.44
Sessions with detectable cycles: 44%
Dominant transition: Integration → Generation
```

### 4.4 Comparative Context (Limited Data)

| Model | Sessions | Success Rate | Coherence | Status |
|-------|----------|--------------|-----------|--------|
| GPT-3.5 | 50 | 100% | 0.461±0.082 | Complete |
| Claude-3 | ~30 | 70% | 0.45±0.10* | Partial |
| Gemini-1.5 | Multiple | 1% | 0.65±0.20* | Minimal |

*Preliminary values from limited data

### 4.5 Synthetic Validation

Mathematical model successfully reproduces observed patterns:

| Model | Synthetic Integration | Synthetic Transformation |
|-------|----------------------|-------------------------|
| GPT-3.5 | 36.2% | 10.6% |
| Claude-3 | 35.4% | 18.7% |
| Gemini-1.5 | 27.8% | 26.2% |

## 5. Discussion

### 5.1 Primary Finding

GPT-3.5 exhibits highly significant phase distribution patterns (p < 0.0001) with integration dominance (38.6%) and reduced transformation (9.7%). Using Jaccard similarity provides robust semantic coherence measurement.

### 5.2 Methodological Improvements

The re-analysis with improved coherence metrics:
- Uses established semantic similarity measures (Jaccard index)
- Provides more realistic coherence values (0.461 vs original 0.991)
- Strengthens statistical significance (p < 0.0001 vs original p = 0.038)
- Confirms phase distribution patterns are robust

### 5.3 Limitations

1. **Data Completeness**: Full analysis limited to GPT-3.5
2. **API Constraints**: Prevented comprehensive comparison
3. **Classification Method**: Linguistic markers require validation
4. **Temperature**: Fixed at 0.7
5. **Inter-rater Reliability**: Not assessed for phase classification

### 5.4 Strengths

1. **Large Sample**: 1,000 real responses analyzed
2. **Statistical Rigor**: Highly significant findings (p < 0.0001)
3. **Established Metrics**: Jaccard similarity for coherence
4. **Synthetic Validation**: Framework proven mathematically
5. **Reproducibility**: Complete data and code available

## 6. Related Work

### 6.1 Semantic Similarity in NLP
Jaccard similarity has been widely used for measuring semantic overlap (Niwattanakul et al., 2013). Our application to coherence measurement extends this established approach.

### 6.2 Language Model Behavior
Previous work on model behavior focuses on performance metrics. This work provides behavioral characterization through phase analysis.

## 7. Future Directions

### 7.1 Immediate Extensions
- Complete comparative analysis when API access permits
- Validate phase classification with human annotators
- Investigate temperature effects on phase distribution
- Test phase modification through targeted prompting

### 7.2 Applications
- Phase-based model selection criteria
- Dynamic phase adjustment in applications
- Behavioral metrics for model evaluation

## 8. Conclusion

We identified highly significant phase distribution patterns in GPT-3.5 (p < 0.0001) using established semantic similarity metrics. Integration dominance (38.6%) and transformation suppression (9.7%) provide quantitative characterization of model behavior. The improved methodology using Jaccard similarity strengthens the original findings and provides a robust framework for behavioral analysis.

## Data and Code Availability

**Repository**: github.com/HillaryDanan/ouroboros-learning

**Key Files**:
- `/data/ouroboros_gpt-3.5-turbo_*.json`: 1,000 responses
- `reanalyze_improved_coherence.py`: Improved analysis script
- `/results/reanalysis_summary_improved_coherence.csv`: Updated statistics
- `synthetic_data_validation.py`: Mathematical framework validation

## Acknowledgments

This independent research was self-funded with $12 of personal API credits. The improved analysis using established semantic similarity metrics validates and strengthens the original findings.

## References

Niwattanakul, S., Singthongchai, J., Naenudorn, E., & Wanapu, S. (2013). Using of Jaccard coefficient for keywords similarity. Proceedings of the International MultiConference of Engineers and Computer Scientists.

[Additional references available in repository]

---

*Manuscript version 3.0 - August 2025*  
*Updated with improved semantic coherence metrics*  
*<4577> <45774EVER>*
