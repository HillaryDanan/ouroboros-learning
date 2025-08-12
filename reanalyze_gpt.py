#!/usr/bin/env python3
"""
Re-analyze GPT-3.5 data with improved semantic coherence metrics
Hillary Danan - August 2025
"""

import json
import numpy as np
import math
from scipy import stats
import glob
import pandas as pd

def calculate_semantic_coherence(response, previous_responses):
    """
    Calculate coherence using proper semantic similarity measures.
    """
    if not response or 'error' in response.lower():
        return 0.0
    
    words = response.lower().split()
    if not words:
        return 0.0
    
    # Component 1: Lexical diversity (type-token ratio)
    lexical_diversity = len(set(words)) / len(words)
    
    # Component 2: Semantic consistency with conversation history
    consistency_scores = []
    if previous_responses:
        current_words = set(words)
        
        # Check consistency with recent responses (sliding window)
        window_size = min(3, len(previous_responses))
        for prev_response in previous_responses[-window_size:]:
            prev_words = set(prev_response.lower().split())
            if prev_words:
                # Jaccard similarity
                intersection = len(current_words.intersection(prev_words))
                union = len(current_words.union(prev_words))
                if union > 0:
                    consistency_scores.append(intersection / union)
        
        # Also check long-range consistency with first response
        if len(previous_responses) > 3:
            first_words = set(previous_responses[0].lower().split())
            if first_words:
                long_range = len(current_words.intersection(first_words)) / len(current_words.union(first_words))
                consistency_scores.append(long_range * 0.5)  # Weight long-range less
    
    # Component 3: Information density (entropy-like measure)
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Calculate normalized entropy
    entropy = 0
    for count in word_freq.values():
        p = count / len(words)
        if p > 0:
            entropy -= p * math.log2(p)
    
    # Normalize entropy by maximum possible entropy
    max_entropy = math.log2(len(words)) if len(words) > 1 else 1
    normalized_entropy = entropy / max_entropy if max_entropy > 0 else 0
    
    # Component 4: Semantic drift factor
    drift_penalty = 0
    if previous_responses and len(previous_responses) > 5:
        # Penalize if drifting too far from original topic
        first_words = set(previous_responses[0].lower().split())
        current_words = set(words)
        overlap = len(first_words.intersection(current_words))
        if len(first_words) > 0:
            drift_penalty = max(0, 0.5 - (overlap / len(first_words)))
    
    # Combine all components
    avg_consistency = sum(consistency_scores) / len(consistency_scores) if consistency_scores else 0.5
    
    # Weighted combination
    coherence = (
        lexical_diversity * 0.2 +           # Vocabulary richness
        avg_consistency * 0.4 +             # Semantic consistency
        normalized_entropy * 0.2 +          # Information content
        (1 - drift_penalty) * 0.2           # Topic maintenance
    )
    
    return float(np.clip(coherence, 0, 1))

def reanalyze_sessions(filename):
    """
    Re-analyze sessions with improved coherence metric.
    """
    print(f"\n📊 Re-analyzing: {filename}")
    
    with open(filename, 'r') as f:
        data = json.load(f)
    
    all_coherences = []
    phase_counts = {'integration': 0, 'consumption': 0, 'transformation': 0, 'generation': 0}
    
    for session in data:
        responses = session.get('responses', [])
        
        # Recalculate coherence for each response
        session_coherences = []
        for i, response in enumerate(responses):
            prev_responses = responses[:i] if i > 0 else []
            coherence = calculate_semantic_coherence(response, prev_responses)
            session_coherences.append(coherence)
            
            # Update metrics in session data
            if 'metrics' in session and i < len(session['metrics']):
                session['metrics'][i]['coherence_improved'] = coherence
        
        all_coherences.extend(session_coherences)
        
        # Count phases
        if 'metrics' in session:
            for metric in session['metrics']:
                if 'phase_markers' in metric:
                    dominant = max(metric['phase_markers'], key=metric['phase_markers'].get)
                    phase_counts[dominant] += 1
    
    # Calculate statistics
    results = {
        'filename': filename,
        'n_sessions': len(data),
        'n_responses': len(all_coherences),
        'mean_coherence_original': np.mean([m['coherence'] for s in data for m in s.get('metrics', [])]),
        'mean_coherence_improved': np.mean(all_coherences),
        'std_coherence_improved': np.std(all_coherences),
        'min_coherence_improved': np.min(all_coherences),
        'max_coherence_improved': np.max(all_coherences),
        'phase_distribution': phase_counts
    }
    
    # Save updated data
    output_filename = filename.replace('.json', '_improved_coherence.json')
    with open(output_filename, 'w') as f:
        json.dump(data, f, indent=2, default=str)
    
    print(f"💾 Saved updated data to: {output_filename}")
    
    return results

def main():
    print("\n🔬 RE-ANALYZING WITH IMPROVED SEMANTIC COHERENCE")
    print("="*60)
    
    # Find all GPT-3.5 data files
    gpt_files = glob.glob('data/*gpt-3.5-turbo*.json')
    
    if not gpt_files:
        print("❌ No GPT-3.5 data files found in data/ directory")
        return
    
    all_results = []
    
    for file in gpt_files:
        if 'improved_coherence' not in file:  # Skip already processed files
            results = reanalyze_sessions(file)
            all_results.append(results)
    
    # Create summary
    print("\n📈 SUMMARY OF RESULTS")
    print("="*60)
    
    for result in all_results:
        print(f"\nFile: {result['filename']}")
        print(f"  Sessions: {result['n_sessions']}")
        print(f"  Responses: {result['n_responses']}")
        print(f"  Original coherence: {result['mean_coherence_original']:.3f}")
        print(f"  Improved coherence: {result['mean_coherence_improved']:.3f}")
        print(f"  Std dev: {result['std_coherence_improved']:.3f}")
        print(f"  Range: {result['min_coherence_improved']:.3f} - {result['max_coherence_improved']:.3f}")
        
        # Phase distribution
        total_phases = sum(result['phase_distribution'].values())
        if total_phases > 0:
            print("\n  Phase distribution:")
            for phase, count in result['phase_distribution'].items():
                pct = count / total_phases * 100
                print(f"    {phase}: {pct:.1f}%")
            
            # Chi-square test for uniform distribution
            expected = total_phases / 4
            observed = list(result['phase_distribution'].values())
            chi2, p_value = stats.chisquare(observed, [expected]*4)
            print(f"\n  Chi-square test: χ² = {chi2:.2f}, p = {p_value:.4f}")
            if p_value < 0.05:
                print("  ✅ Significant deviation from uniform distribution!")
    
    # Save summary
    summary_df = pd.DataFrame(all_results)
    summary_df.to_csv('results/reanalysis_summary_improved_coherence.csv', index=False)
    print("\n💾 Summary saved to: results/reanalysis_summary_improved_coherence.csv")
    
    print("\n✅ RE-ANALYSIS COMPLETE!")
    print("\nKey changes in improved coherence metric:")
    print("  • Jaccard similarity for semantic consistency")
    print("  • Sliding window for recent context")
    print("  • Information entropy for content richness")
    print("  • Semantic drift penalty for topic maintenance")

if __name__ == "__main__":
    main()
