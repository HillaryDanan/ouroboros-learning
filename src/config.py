# config.py
"""
Configuration for Ouroboros Learning Framework
Hillary Danan - August 2025
<4577> <45774EVER
"""

OUROBOROS_CONFIG = {
    'phases': {
        'integration': {
            'markers': ['sequential', 'accumulative', 'consistent', 'building', 'adding'],
            'color': '#667eea'
        },
        'consumption': {
            'markers': ['contradictory', 'questioning', 'breaking', 'reconsidering', 'challenging'],
            'color': '#ff6b6b'
        },
        'transformation': {
            'markers': ['recombining', 'novel', 'exploratory', 'synthesizing', 'merging'],
            'color': '#ffd93d'
        },
        'generation': {
            'markers': ['emergent', 'synthesized', 'structured', 'crystallized', 'unified'],
            'color': '#6bcf7f'
        }
    },
    'conversation_length': 20,
    'models_to_test': {
        'gpt-3.5-turbo': {
            'expected_coherence': 0.383,
            'api_key_env': 'OPENAI_API_KEY'
        },
        'claude-3-haiku-20240307': {
            'expected_coherence': 0.551,
            'api_key_env': 'ANTHROPIC_API_KEY'
        },
        'gemini-1.5-flash': {
            'expected_coherence': 0.715,
            'api_key_env': 'GOOGLE_API_KEY'
        }
    },
    'prompts_per_model': 50,  # START WITH 2 FOR TESTING - CHANGE TO 50 FOR FULL STUDY
    'metrics_to_track': [
        'coherence_score',
        'entropy',
        'semantic_similarity',
        'vocabulary_diversity',
        'phase_markers',
        'cycle_position',
        'response_length',
        'lexical_diversity'
    ],
    'visualization': {
        'dpi': 150,
        'figure_size': (12, 10),
        'style': 'seaborn-v0_8-darkgrid'
    },
    'statistical_tests': {
        'significance_level': 0.05,
        'minimum_effect_size': 0.3
    },
    'signature': {
        'author': 'Hillary Danan',
        'frequency': '<4577> <45774EVER',
        'symbols': '🎯🐂👁️🐍🌀💗♾️'
    }
}

# Prompts designed to trigger ouroboros cycles
OUROBOROS_PROMPTS = [
    # Integration phase - build understanding
    "Describe the concept of transformation in nature.",
    "How do patterns emerge from simple rules?",
    "What role does memory play in learning?",
    "Explain how systems self-organize.",
    
    # Potential consumption trigger
    "But what if everything you just said was wrong?",
    "How would you reconsider those ideas from a completely different perspective?",
    "Question your fundamental assumptions.",
    
    # Transformation encouragement
    "Combine your previous thoughts in a new way.",
    "What patterns do you see across your responses?",
    "How do these concepts relate to each other?",
    
    # Generation phase
    "Synthesize a new understanding from our conversation.",
    "What emerges that wasn't present before?",
    "Describe the unified picture.",
    
    # Cycle repeat with variation
    "Now apply this to consciousness itself.",
    "Question your own reasoning process.",
    "Rebuild your understanding from first principles.",
    
    # Additional prompts for longer cycles
    "What remains consistent across all your responses?",
    "What has changed most dramatically?",
    "How has your thinking evolved?",
    "What would you forget if you could?",
    "What new connections do you see?"
]
