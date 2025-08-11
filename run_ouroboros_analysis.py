#!/usr/bin/env python3
"""
Main execution script for Ouroboros Learning Analysis
Hillary Danan - August 2025
<4577> <45774EVER
"""

import sys
import os
sys.path.append('src')

import json
import numpy as np
import pandas as pd
from datetime import datetime
from scipy import stats
from typing import Dict, List  # <-- ADD THIS LINE!
from src.ouroboros_analyzer import OuroborosAnalyzer
from src.ouroboros_visualizer import OuroborosVisualizer
from src.config import OUROBOROS_CONFIG

def print_header():
    """Print the beautiful header."""
    print("\n" + "="*60)
    print("🐍♾️  OUROBOROS LEARNING FRAMEWORK  ♾️🐍")
    print("     Self-Consuming Cycles in AI Cognition")
    print("           Hillary Danan - August 2025")
    print("="*60 + "\n")

def create_directories():
    """Create necessary directories if they don't exist."""
    directories = ['data', 'results', 'plots', 'notebooks', 'tests']
    for dir_name in directories:
        os.makedirs(dir_name, exist_ok=True)
    print("✅ Directory structure created")

def analyze_model_differences(all_sessions: Dict[str, List]) -> pd.DataFrame:
    """
    Compare ouroboros patterns across different models.
    
    Args:
        all_sessions: Dictionary mapping model names to session lists
        
    Returns:
        DataFrame with comparative statistics
    """
    model_stats = []
    
    for model_name, sessions in all_sessions.items():
        if not sessions:
            continue
            
        stats = {
            'model': model_name,
            'sessions_analyzed': len(sessions),
            'avg_cycles': np.mean([s['cycles']['num_peaks'] for s in sessions]),
            'std_cycles': np.std([s['cycles']['num_peaks'] for s in sessions]),
            'avg_cycle_amplitude': np.mean([s['cycles']['coherence_range'] for s in sessions]),
            'phase_transition_rate': np.mean([s['cycles']['transition_rate'] for s in sessions]),
            'coherence_stability': np.mean([s['cycles']['coherence_std'] for s in sessions]),
            'avg_coherence': np.mean([s['cycles']['coherence_mean'] for s in sessions])
        }
        
        # Calculate phase dominance
        phase_counts = {phase: 0 for phase in ['integration', 'consumption', 'transformation', 'generation']}
        total_responses = 0
        
        for session in sessions:
            for metrics in session['metrics']:
                if 'phase_markers' in metrics:
                    dominant = max(metrics['phase_markers'], key=metrics['phase_markers'].get)
                    phase_counts[dominant] += 1
                    total_responses += 1
                    
        for phase in phase_counts:
            stats[f'{phase}_dominance'] = phase_counts[phase] / total_responses if total_responses > 0 else 0
            
        # Calculate cycle regularity
        regularities = [s['cycles'].get('cycle_regularity', 0) for s in sessions]
        stats['avg_cycle_regularity'] = np.mean(regularities) if regularities else 0
        
        model_stats.append(stats)
        
    return pd.DataFrame(model_stats)

def run_statistical_tests(all_sessions: Dict[str, List]) -> Dict:
    """
    Run statistical tests to validate ouroboros patterns.
    
    Args:
        all_sessions: Dictionary of all session data
        
    Returns:
        Dictionary of test results
    """
    results = {}
    
    # Extract cycle counts for each model
    model_cycles = {}
    for model_name, sessions in all_sessions.items():
        model_cycles[model_name] = [s['cycles']['num_peaks'] for s in sessions]
    
    # ANOVA for cycle differences across models
    if len(model_cycles) >= 2:
        cycle_values = list(model_cycles.values())
        f_stat, p_value = stats.f_oneway(*cycle_values)
        results['anova_cycles'] = {
            'f_statistic': f_stat,
            'p_value': p_value,
            'significant': p_value < 0.05
        }
        
    # Correlation between position and coherence
    model_correlations = {}
    for model_name, sessions in all_sessions.items():
        correlations = []
        for session in sessions:
            if len(session['metrics']) > 1:
                positions = [m['position'] for m in session['metrics']]
                coherence = [m['coherence'] for m in session['metrics']]
                corr, p = stats.pearsonr(positions, coherence)
                correlations.append(corr)
        
        if correlations:
            model_correlations[model_name] = {
                'mean_correlation': np.mean(correlations),
                'std_correlation': np.std(correlations)
            }
    
    results['position_coherence_correlation'] = model_correlations
    
    # Test for periodicity using FFT
    model_periodicities = {}
    for model_name, sessions in all_sessions.items():
        dominant_periods = []
        for session in sessions:
            if 'dominant_period' in session['cycles'] and session['cycles']['dominant_period']:
                dominant_periods.append(session['cycles']['dominant_period'])
        
        if dominant_periods:
            model_periodicities[model_name] = {
                'mean_period': np.mean(dominant_periods),
                'std_period': np.std(dominant_periods),
                'modal_period': max(set(dominant_periods), key=dominant_periods.count)
            }
    
    results['periodicity'] = model_periodicities
    
    return results

def generate_report(model_stats: pd.DataFrame, stat_results: Dict) -> str:
    """
    Generate a comprehensive analysis report.
    
    Args:
        model_stats: DataFrame with model statistics
        stat_results: Dictionary of statistical test results
        
    Returns:
        Formatted report string
    """
    report = []
    report.append("="*60)
    report.append("📊 OUROBOROS LEARNING ANALYSIS REPORT")
    report.append("="*60)
    report.append("")
    
    # Model comparison
    report.append("🔬 MODEL COMPARISON")
    report.append("-"*40)
    report.append(model_stats.to_string())
    report.append("")
    
    # Statistical significance
    report.append("📈 STATISTICAL ANALYSIS")
    report.append("-"*40)
    
    if 'anova_cycles' in stat_results:
        anova = stat_results['anova_cycles']
        report.append(f"ANOVA for cycle differences:")
        report.append(f"  F-statistic: {anova['f_statistic']:.3f}")
        report.append(f"  p-value: {anova['p_value']:.6f}")
        if anova['significant']:
            report.append("  ✨ SIGNIFICANT DIFFERENCES IN OUROBOROS PATTERNS DETECTED!")
        report.append("")
    
    # Correlations
    if 'position_coherence_correlation' in stat_results:
        report.append("Position-Coherence Correlations:")
        for model, corr_data in stat_results['position_coherence_correlation'].items():
            report.append(f"  {model}: r = {corr_data['mean_correlation']:.3f} "
                         f"(±{corr_data['std_correlation']:.3f})")
        report.append("")
    
    # Periodicity
    if 'periodicity' in stat_results:
        report.append("Detected Periodicities:")
        for model, period_data in stat_results['periodicity'].items():
            report.append(f"  {model}: {period_data['mean_period']:.1f} "
                         f"(modal: {period_data['modal_period']})")
        report.append("")
    
    # Key findings
    report.append("🎯 KEY FINDINGS")
    report.append("-"*40)
    
    # Find model with highest coherence
    if not model_stats.empty:
        highest_coherence = model_stats.loc[model_stats['avg_coherence'].idxmax()]
        report.append(f"Highest average coherence: {highest_coherence['model']} "
                     f"({highest_coherence['avg_coherence']:.3f})")
        
        # Find model with most regular cycles
        most_regular = model_stats.loc[model_stats['avg_cycle_regularity'].idxmin()]
        report.append(f"Most regular cycles: {most_regular['model']} "
                     f"(regularity: {most_regular['avg_cycle_regularity']:.3f})")
        
        # Phase dominance patterns
        report.append("")
        report.append("Phase Dominance Patterns:")
        for _, row in model_stats.iterrows():
            phases = ['integration', 'consumption', 'transformation', 'generation']
            dominant_phase = max(phases, key=lambda p: row[f'{p}_dominance'])
            report.append(f"  {row['model']}: {dominant_phase} "
                         f"({row[f'{dominant_phase}_dominance']:.1%})")
    
    report.append("")
    report.append("="*60)
    report.append("="*60)
    
    return "\n".join(report)

def main():
    """
    Main execution function for ouroboros learning analysis.
    """
    print_header()
    
    # Setup
    print("🚀 Initializing Ouroboros Learning Analysis...")
    create_directories()
    
    # Initialize analyzer
    print("\n📊 Creating analyzer...")
    analyzer = OuroborosAnalyzer()
    
    # Models to test (using simplified names for testing)
    models = list(OUROBOROS_CONFIG['models_to_test'].keys())
    print(f"Models to analyze: {', '.join(models)}")
    
    # Number of sessions per model (reduced for testing)
    num_sessions = min(5, OUROBOROS_CONFIG['prompts_per_model'])  # Start with 5 for testing
    
    # Collect data for each model
    all_sessions = {}
    
    for model in models:
        print(f"\n🔄 Analyzing {model}...")
        sessions = analyzer.collect_ouroboros_data(
            model_name=model,
            num_sessions=num_sessions
        )
        all_sessions[model] = sessions
        
        # Save raw data
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'data/ouroboros_{model}_{timestamp}.json'
        with open(filename, 'w') as f:
            json.dump(sessions, f, indent=2, default=str)
        
        print(f"✅ Completed {len(sessions)} sessions for {model}")
        print(f"💾 Data saved to {filename}")
    
    # Analyze differences
    print("\n🔬 Analyzing model differences...")
    model_stats = analyze_model_differences(all_sessions)
    
    # Save analysis results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    stats_filename = f'results/ouroboros_model_comparison_{timestamp}.csv'
    model_stats.to_csv(stats_filename, index=False)
    print(f"📊 Statistics saved to {stats_filename}")
    
    # Run statistical tests
    print("\n📈 Running statistical tests...")
    stat_results = run_statistical_tests(all_sessions)
    
    # Generate and save report
    report = generate_report(model_stats, stat_results)
    report_filename = f'results/ouroboros_report_{timestamp}.txt'
    with open(report_filename, 'w') as f:
        f.write(report)
    print(f"📝 Report saved to {report_filename}")
    
    # Create visualizations
    print("\n🎨 Creating visualizations...")
    visualizer = OuroborosVisualizer()
    
    # Create plots for each model (first session as example)
    for model, sessions in all_sessions.items():
        if sessions:
            # Static plot
            fig = visualizer.plot_coherence_cycles(sessions[0])
            plot_filename = f'plots/ouroboros_{model}_example.png'
            fig.savefig(plot_filename, dpi=150, bbox_inches='tight')
            print(f"  📊 Saved plot: {plot_filename}")
            
            # Interactive plot
            interactive_fig = visualizer.create_interactive_cycle_plot(sessions[0])
            interactive_filename = f'plots/ouroboros_{model}_interactive.html'
            interactive_fig.write_html(interactive_filename)
            print(f"  🌐 Saved interactive: {interactive_filename}")
    
    # Model comparison plot
    if not model_stats.empty:
        comparison_fig = visualizer.plot_model_comparison(model_stats)
        comparison_filename = 'plots/ouroboros_model_comparison.png'
        comparison_fig.savefig(comparison_filename, dpi=150, bbox_inches='tight')
        print(f"  📊 Saved comparison: {comparison_filename}")
    
    # Print report to console
    print("\n" + report)
    
    # Final message
    print("\n✨ ANALYSIS COMPLETE!")
    print("="*60)
    print("Results saved to: results/")
    print("Plots saved to: plots/")
    print("Raw data saved to: data/")
    print("="*60)
    
    return model_stats, all_sessions

if __name__ == "__main__":
    try:
        results, data = main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Analysis interrupted by user")
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()
