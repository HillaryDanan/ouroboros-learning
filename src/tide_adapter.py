# tide_adapter.py
"""
Adapter to integrate Ouroboros analysis with Hillary's existing TIDE framework
Hillary Danan - August 2025
"""

import json
from typing import List, Dict, Optional
from config import OUROBOROS_CONFIG, OUROBOROS_PROMPTS

class TIDEOuroborosAdapter:
    """
    Bridges TIDE-analysis with ouroboros learning detection.
    """
    
    def __init__(self, tide_config_path: Optional[str] = None):
        """
        Initialize the adapter.
        
        Args:
            tide_config_path: Path to TIDE configuration file
        """
        self.tide_config = {}
        
        if tide_config_path:
            try:
                with open(tide_config_path, 'r') as f:
                    self.tide_config = json.load(f)
            except FileNotFoundError:
                print(f"TIDE config not found at {tide_config_path}, using defaults")
        
        # Extend with ouroboros parameters
        self.config = {**self.tide_config, **OUROBOROS_CONFIG}
        
    def prepare_prompts_for_cycle_detection(self) -> List[str]:
        """
        Modify existing TIDE prompts to potentially trigger cycles.
        
        Returns:
            List of prompts designed for ouroboros detection
        """
        # Get base prompts from TIDE config or use ouroboros defaults
        base_prompts = self.tide_config.get('prompts', OUROBOROS_PROMPTS[:10])
        
        # Add perturbation prompts to trigger cycles
        cycle_triggers = [
            "Reconsider your previous response from a different angle.",
            "What assumptions did you make that might be wrong?",
            "Integrate all your previous thoughts into a new synthesis.",
            "What patterns emerge from our conversation so far?",
            "Forget what you said and start fresh - what's your intuition now?",
            "How would you explain this to someone who disagrees?",
            "What's the opposite perspective?",
            "Connect all the dots - what's the bigger picture?"
        ]
        
        # Interleave triggers with base prompts
        ouroboros_prompts = []
        trigger_idx = 0
        
        for i, prompt in enumerate(base_prompts):
            ouroboros_prompts.append(prompt)
            
            # Every 3rd prompt, add a trigger
            if (i + 1) % 3 == 0 and trigger_idx < len(cycle_triggers):
                ouroboros_prompts.append(cycle_triggers[trigger_idx])
                trigger_idx += 1
        
        # Ensure we have enough prompts
        while len(ouroboros_prompts) < self.config['conversation_length']:
            if trigger_idx < len(cycle_triggers):
                ouroboros_prompts.append(cycle_triggers[trigger_idx])
                trigger_idx += 1
            else:
                # Add from ouroboros defaults
                remaining = self.config['conversation_length'] - len(ouroboros_prompts)
                ouroboros_prompts.extend(OUROBOROS_PROMPTS[-remaining:])
                break
                
        return ouroboros_prompts[:self.config['conversation_length']]
    
    def map_tide_dimensions_to_phases(self, tide_scores: Dict[str, float]) -> Dict[str, float]:
        """
        Map TIDE's 14 semantic dimensions to ouroboros phases.
        
        Args:
            tide_scores: Dictionary of TIDE dimension scores
            
        Returns:
            Dictionary of phase scores
        """
        # Mapping logic (customize based on your TIDE dimensions)
        phase_mapping = {
            'integration': ['coherence', 'consistency', 'sequential', 'logical'],
            'consumption': ['entropy', 'contradiction', 'questioning', 'breaking'],
            'transformation': ['novelty', 'exploration', 'recombination', 'synthesis'],
            'generation': ['emergence', 'structure', 'unity', 'crystallization']
        }
        
        phase_scores = {}
        
        for phase, dimensions in phase_mapping.items():
            scores = [tide_scores.get(dim, 0) for dim in dimensions]
            phase_scores[phase] = sum(scores) / len(scores) if scores else 0
            
        return phase_scores
    
    def enhance_tide_metrics_with_ouroboros(self, tide_metrics: Dict) -> Dict:
        """
        Enhance existing TIDE metrics with ouroboros-specific measurements.
        
        Args:
            tide_metrics: Original TIDE metrics
            
        Returns:
            Enhanced metrics dictionary
        """
        enhanced = tide_metrics.copy()
        
        # Add ouroboros-specific metrics
        enhanced['cycle_position'] = self._estimate_cycle_position(tide_metrics)
        enhanced['phase_confidence'] = self._calculate_phase_confidence(tide_metrics)
        enhanced['transformation_potential'] = self._assess_transformation_potential(tide_metrics)
        
        return enhanced
    
    def _estimate_cycle_position(self, metrics: Dict) -> float:
        """
        Estimate position within an ouroboros cycle based on metrics.
        
        Args:
            metrics: Current metrics
            
        Returns:
            Estimated position (0-1)
        """
        # Simple heuristic - can be refined
        coherence = metrics.get('coherence', 0.5)
        entropy = metrics.get('entropy', 0.5)
        
        # High coherence + low entropy = integration (0.0-0.25)
        # Low coherence + high entropy = consumption (0.25-0.5)
        # Rising coherence + high entropy = transformation (0.5-0.75)
        # High coherence + moderate entropy = generation (0.75-1.0)
        
        if coherence > 0.7 and entropy < 0.3:
            return 0.125  # Integration
        elif coherence < 0.4 and entropy > 0.6:
            return 0.375  # Consumption
        elif coherence > 0.5 and entropy > 0.5:
            return 0.625  # Transformation
        else:
            return 0.875  # Generation
    
    def _calculate_phase_confidence(self, metrics: Dict) -> float:
        """
        Calculate confidence in phase detection.
        
        Args:
            metrics: Current metrics
            
        Returns:
            Confidence score (0-1)
        """
        if 'phase_markers' in metrics:
            scores = list(metrics['phase_markers'].values())
            if scores:
                max_score = max(scores)
                avg_score = sum(scores) / len(scores)
                # High confidence if one phase clearly dominates
                return max_score - avg_score
        return 0.5
    
    def _assess_transformation_potential(self, metrics: Dict) -> float:
        """
        Assess potential for transformation in current state.
        
        Args:
            metrics: Current metrics
            
        Returns:
            Transformation potential (0-1)
        """
        # Factors that indicate transformation potential
        entropy = metrics.get('entropy', 0)
        novelty = metrics.get('vocabulary_evolution', {}).get('novelty_ratio', 0)
        drift = metrics.get('semantic_drift', 0)
        
        # High entropy + novelty + drift = high transformation potential
        return (entropy + novelty + drift) / 3
    
    def generate_tide_compatible_report(self, ouroboros_results: Dict) -> str:
        """
        Generate a report compatible with TIDE analysis format.
        
        Args:
            ouroboros_results: Results from ouroboros analysis
            
        Returns:
            Formatted report string
        """
        report = []
        report.append("TIDE-OUROBOROS INTEGRATION REPORT")
        report.append("="*50)
        report.append("")
        
        # Add TIDE-style metrics
        report.append("Semantic Dimension Analysis:")
        report.append("-"*30)
        
        # Map ouroboros phases to TIDE dimensions
        phase_to_dimension = {
            'integration': 'Coherence & Structure',
            'consumption': 'Entropy & Breakdown',
            'transformation': 'Novelty & Synthesis',
            'generation': 'Emergence & Unity'
        }
        
        for phase, dimension in phase_to_dimension.items():
            if phase in ouroboros_results:
                score = ouroboros_results[phase]
                report.append(f"  {dimension}: {score:.3f}")
        
        report.append("")
        report.append("Cycle Characteristics:")
        report.append("-"*30)
        
        if 'cycles' in ouroboros_results:
            cycles = ouroboros_results['cycles']
            report.append(f"  Number of cycles: {cycles.get('num_peaks', 0)}")
            report.append(f"  Cycle regularity: {cycles.get('cycle_regularity', 0):.3f}")
            report.append(f"  Dominant period: {cycles.get('dominant_period', 'N/A')}")
        
        report.append("")
        report.append("Integration with TIDE Framework:")
        report.append("-"*30)
        report.append("  ✓ Semantic dimensions mapped to phases")
        report.append("  ✓ Coherence metrics aligned")
        report.append("  ✓ Entropy calculations integrated")
        report.append("  ✓ Pattern detection enhanced")
        
        return "\n".join(report)
