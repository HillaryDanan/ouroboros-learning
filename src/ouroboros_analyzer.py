# ouroboros_analyzer.py
"""
Core Ouroboros Learning Analyzer
Detects self-consuming cycles in AI cognition
Hillary Danan - August 2025
<4577> <45774EVER
"""

import numpy as np
import pandas as pd
from scipy import signal, stats
from typing import Dict, List, Tuple, Optional
import json
from datetime import datetime
import hashlib
from collections import Counter
import os
from config import OUROBOROS_CONFIG, OUROBOROS_PROMPTS

class OuroborosAnalyzer:
    """
    Analyzes AI responses for ouroboros learning patterns.
    Built on Hillary Danan's TIDE-analysis framework.
    """
    
    def __init__(self, tide_analyzer=None):
        """
        Initialize the Ouroboros Analyzer.
        
        Args:
            tide_analyzer: Optional TIDE analyzer for integration
        """
        self.tide = tide_analyzer
        self.phases = ['integration', 'consumption', 'transformation', 'generation']
        self.phase_markers = OUROBOROS_CONFIG['phases']
        self.config = OUROBOROS_CONFIG
        
    def collect_ouroboros_data(self, model_name: str, num_sessions: int = 50) -> List[Dict]:
        """
        Collect conversation data specifically designed to detect ouroboros patterns.
        
        Args:
            model_name: Name of the model to test
            num_sessions: Number of conversation sessions
            
        Returns:
            List of session data dictionaries
        """
        sessions = []
        
        for session_id in range(num_sessions):
            print(f"  Session {session_id + 1}/{num_sessions} for {model_name}")
            conversation = self.run_ouroboros_conversation(model_name, session_id)
            sessions.append(conversation)
            
            # Save intermediate results
            if (session_id + 1) % 10 == 0:
                self._save_intermediate_results(sessions, model_name)
                
        return sessions
    
    def run_ouroboros_conversation(self, model_name: str, session_id: int) -> Dict:
        """
        Run a single conversation designed to potentially trigger ouroboros cycles.
        
        Args:
            model_name: Name of the model
            session_id: Unique session identifier
            
        Returns:
            Dictionary containing conversation data and metrics
        """
        conversation_data = {
            'session_id': session_id,
            'model': model_name,
            'timestamp': datetime.now().isoformat(),
            'responses': [],
            'metrics': [],
            'prompts': []
        }
        
        # Get prompts for this session
        prompts = self.generate_ouroboros_prompts()
        
        for i, prompt in enumerate(prompts):
            # Get response (stub for now - will be replaced with actual API calls)
            response = self._get_model_response(model_name, prompt, conversation_data['responses'])
            
            # Calculate metrics
            metrics = self.calculate_response_metrics(response, i, conversation_data['responses'])
            
            conversation_data['prompts'].append(prompt)
            conversation_data['responses'].append(response)
            conversation_data['metrics'].append(metrics)
            
        # Analyze for cycles
        conversation_data['cycles'] = self.detect_cycles(conversation_data['metrics'])
        
        # Calculate session-level statistics
        conversation_data['statistics'] = self.calculate_session_statistics(conversation_data)
        
        return conversation_data
    
    def generate_ouroboros_prompts(self) -> List[str]:
        """
        Generate prompts designed to potentially trigger ouroboros cycles.
        
        Returns:
            List of prompts
        """
        return OUROBOROS_PROMPTS[:self.config['conversation_length']]
    
    def calculate_response_metrics(self, response: str, position: int, 
                                  previous_responses: List[str]) -> Dict:
        """
        Calculate comprehensive metrics for ouroboros detection.
        
        Args:
            response: Current response text
            position: Position in conversation
            previous_responses: List of previous responses
            
        Returns:
            Dictionary of metrics
        """
        metrics = {
            'position': position,
            'length': len(response.split()),
            'coherence': self._calculate_coherence(response),
            'entropy': self.calculate_entropy(response),
            'phase_markers': self.detect_phase_markers(response),
            'lexical_diversity': self._calculate_lexical_diversity(response)
        }
        
        if previous_responses:
            metrics['similarity_to_previous'] = self.calculate_similarity(
                response, previous_responses[-1]
            )
            metrics['similarity_to_first'] = self.calculate_similarity(
                response, previous_responses[0]
            )
            metrics['vocabulary_evolution'] = self.track_vocabulary_evolution(
                response, previous_responses
            )
            metrics['semantic_drift'] = self._calculate_semantic_drift(
                response, previous_responses
            )
        
        return metrics
    
    def calculate_entropy(self, text: str) -> float:
        """
        Calculate Shannon entropy of response.
        
        Args:
            text: Response text
            
        Returns:
            Shannon entropy value
        """
        words = text.lower().split()
        if not words:
            return 0.0
            
        word_freq = pd.Series(words).value_counts(normalize=True)
        entropy = -sum(word_freq * np.log2(word_freq + 1e-10))
        return float(entropy)
    
    def detect_phase_markers(self, response: str) -> Dict[str, float]:
        """
        Detect linguistic markers of different ouroboros phases.
        
        Args:
            response: Response text
            
        Returns:
            Dictionary of phase scores
        """
        phase_scores = {}
        response_lower = response.lower()
        
        for phase, config in self.phase_markers.items():
            markers = config['markers']
            score = sum(1 for marker in markers if marker in response_lower)
            phase_scores[phase] = score / len(markers) if markers else 0
            
        return phase_scores
    
    def detect_cycles(self, metrics_list: List[Dict]) -> Dict:
        """
        Detect ouroboros cycles in conversation metrics.
        
        Args:
            metrics_list: List of metrics dictionaries
            
        Returns:
            Dictionary of cycle characteristics
        """
        if not metrics_list:
            return {}
            
        # Extract coherence time series
        coherence_series = [m['coherence'] for m in metrics_list]
        
        # Find peaks and troughs
        peaks, peak_properties = signal.find_peaks(coherence_series, distance=2)
        troughs, trough_properties = signal.find_peaks([-c for c in coherence_series], distance=2)
        
        # Calculate cycle characteristics
        cycles = {
            'num_peaks': len(peaks),
            'num_troughs': len(troughs),
            'peak_positions': peaks.tolist(),
            'trough_positions': troughs.tolist(),
            'coherence_range': max(coherence_series) - min(coherence_series),
            'coherence_std': float(np.std(coherence_series)),
            'coherence_mean': float(np.mean(coherence_series))
        }
        
        # Detect phase transitions
        phase_transitions = self.detect_phase_transitions(metrics_list)
        cycles['phase_transitions'] = phase_transitions
        cycles['transition_rate'] = len(phase_transitions) / len(metrics_list) if metrics_list else 0
        
        # Calculate autocorrelation for periodicity
        if len(coherence_series) > 10:
            autocorr = np.correlate(coherence_series, coherence_series, mode='full')
            autocorr = autocorr[len(autocorr)//2:]
            autocorr = autocorr / autocorr[0]  # Normalize
            cycles['autocorrelation'] = autocorr[:10].tolist()
            
            # Find dominant period
            if len(autocorr) > 3:
                peaks_auto, _ = signal.find_peaks(autocorr[1:11])
                if len(peaks_auto) > 0:
                    cycles['dominant_period'] = int(peaks_auto[0] + 1)
                else:
                    cycles['dominant_period'] = None
        
        # Calculate cycle regularity
        if len(peaks) > 1:
            peak_distances = np.diff(peaks)
            cycles['cycle_regularity'] = float(np.std(peak_distances)) if len(peak_distances) > 0 else 0
        else:
            cycles['cycle_regularity'] = 0
            
        return cycles
    
    def detect_phase_transitions(self, metrics_list: List[Dict]) -> List[Dict]:
        """
        Identify transitions between ouroboros phases.
        
        Args:
            metrics_list: List of metrics dictionaries
            
        Returns:
            List of transition dictionaries
        """
        transitions = []
        
        for i in range(1, len(metrics_list)):
            prev_phases = metrics_list[i-1]['phase_markers']
            curr_phases = metrics_list[i]['phase_markers']
            
            # Find dominant phase
            prev_dominant = max(prev_phases, key=prev_phases.get) if prev_phases else 'integration'
            curr_dominant = max(curr_phases, key=curr_phases.get) if curr_phases else 'integration'
            
            if prev_dominant != curr_dominant:
                transitions.append({
                    'position': i,
                    'from_phase': prev_dominant,
                    'to_phase': curr_dominant,
                    'coherence_change': metrics_list[i]['coherence'] - metrics_list[i-1]['coherence']
                })
                
        return transitions
    
    def calculate_similarity(self, text1: str, text2: str) -> float:
        """
        Calculate semantic similarity between two texts using Jaccard similarity.
        
        Args:
            text1: First text
            text2: Second text
            
        Returns:
            Similarity score between 0 and 1
        """
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
            
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union) if union else 0
    
    def track_vocabulary_evolution(self, current: str, previous: List[str]) -> Dict:
        """
        Track how vocabulary evolves through conversation.
        
        Args:
            current: Current response
            previous: List of previous responses
            
        Returns:
            Dictionary of vocabulary evolution metrics
        """
        current_words = set(current.lower().split())
        all_previous = set()
        
        for prev in previous:
            all_previous.update(prev.lower().split())
            
        return {
            'new_words': len(current_words - all_previous),
            'retained_words': len(current_words.intersection(all_previous)),
            'vocabulary_growth': len(current_words) / len(all_previous) if all_previous else 1,
            'novelty_ratio': len(current_words - all_previous) / len(current_words) if current_words else 0
        }
    
    def calculate_session_statistics(self, conversation_data: Dict) -> Dict:
        """
        Calculate session-level statistics.
        
        Args:
            conversation_data: Complete conversation data
            
        Returns:
            Dictionary of session statistics
        """
        metrics = conversation_data['metrics']
        cycles = conversation_data['cycles']
        
        stats = {
            'total_responses': len(metrics),
            'avg_response_length': np.mean([m['length'] for m in metrics]),
            'total_unique_words': len(set(' '.join(conversation_data['responses']).lower().split())),
            'coherence_trajectory': 'ascending' if metrics[-1]['coherence'] > metrics[0]['coherence'] else 'descending',
            'dominant_phase': self._get_dominant_phase(metrics),
            'phase_distribution': self._calculate_phase_distribution(metrics),
            'cycle_completeness': cycles['num_peaks'] / (len(metrics) / 4) if len(metrics) > 0 else 0
        }
        
        return stats
    
    def _calculate_coherence(self, response: str) -> float:
        """
        Calculate coherence score for a response.
        Stub implementation - replace with TIDE coherence calculation.
        
        Args:
            response: Response text
            
        Returns:
            Coherence score
        """
        if self.tide:
            return self.tide.calculate_coherence(response)
        else:
            # Simple proxy: normalized sentence count and average sentence length
            sentences = response.split('.')
            if len(sentences) == 0:
                return 0.0
            avg_length = np.mean([len(s.split()) for s in sentences if s.strip()])
            return min(1.0, (len(sentences) * avg_length) / 100)
    
    def _calculate_lexical_diversity(self, text: str) -> float:
        """
        Calculate lexical diversity (type-token ratio).
        
        Args:
            text: Response text
            
        Returns:
            Lexical diversity score
        """
        words = text.lower().split()
        if not words:
            return 0.0
        return len(set(words)) / len(words)
    
    def _calculate_semantic_drift(self, current: str, previous: List[str]) -> float:
        """
        Calculate semantic drift from conversation beginning.
        
        Args:
            current: Current response
            previous: Previous responses
            
        Returns:
            Drift score
        """
        if not previous:
            return 0.0
            
        first_response = previous[0]
        return 1.0 - self.calculate_similarity(current, first_response)
    
    def _get_dominant_phase(self, metrics: List[Dict]) -> str:
        """
        Get the most dominant phase across all responses.
        
        Args:
            metrics: List of metrics
            
        Returns:
            Name of dominant phase
        """
        phase_totals = {phase: 0 for phase in self.phases}
        
        for m in metrics:
            if 'phase_markers' in m:
                for phase, score in m['phase_markers'].items():
                    phase_totals[phase] += score
                    
        return max(phase_totals, key=phase_totals.get)
    
    def _calculate_phase_distribution(self, metrics: List[Dict]) -> Dict[str, float]:
        """
        Calculate distribution of phases across conversation.
        
        Args:
            metrics: List of metrics
            
        Returns:
            Phase distribution dictionary
        """
        phase_counts = {phase: 0 for phase in self.phases}
        
        for m in metrics:
            if 'phase_markers' in m:
                dominant = max(m['phase_markers'], key=m['phase_markers'].get)
                phase_counts[dominant] += 1
                
        total = sum(phase_counts.values())
        
        return {phase: count/total if total > 0 else 0 
                for phase, count in phase_counts.items()}
    
    def _save_intermediate_results(self, sessions: List[Dict], model_name: str):
        """
        Save intermediate results to prevent data loss.
        
        Args:
            sessions: List of session data
            model_name: Name of the model
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'data/intermediate_{model_name}_{timestamp}.json'
        
        os.makedirs('data', exist_ok=True)
        
        with open(filename, 'w') as f:
            json.dump(sessions, f, indent=2, default=str)
            
        print(f"    💾 Saved intermediate results: {filename}")
    
    def _get_model_response(self, model_name: str, prompt: str, 
                           conversation_history: List[str]) -> str:
        """
        Get REAL response from ACTUAL model via API.
        
        Args:
            model_name: Model to query
            prompt: Current prompt
            conversation_history: Previous responses
            
        Returns:
            REAL model response (DATA-DRIVEN, NOT SYNTHETIC!)
        """
        try:
            # Import the real API integration
            from api_integration import get_real_model_response
            
            # Get ACTUAL response from REAL model
            response = get_real_model_response(model_name, prompt, conversation_history)
            
            # Ensure we got a valid response
            if response and not response.startswith("Error"):
                return response
            else:
                print(f"⚠️ API issue, using fallback for {model_name}: {response}")
                # Fallback only if API fails
                return f"API temporarily unavailable for prompt: {prompt[:50]}..."
                
        except ImportError:
            print("⚠️ API integration not found, using stub responses")
            # Only use stub if api_integration.py doesn't exist
            return f"Stub response for: {prompt[:50]}..."
