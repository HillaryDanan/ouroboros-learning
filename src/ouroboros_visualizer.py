# ouroboros_visualizer.py
"""
Visualization tools for Ouroboros Learning patterns
Hillary Danan - August 2025
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from matplotlib.patches import Rectangle
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from typing import Dict, List, Optional
from config import OUROBOROS_CONFIG

class OuroborosVisualizer:
    """
    Visualize ouroboros patterns in AI conversations.
    """
    
    def __init__(self):
        """Initialize visualizer with configuration."""
        self.phase_colors = {
            phase: config['color'] 
            for phase, config in OUROBOROS_CONFIG['phases'].items()
        }
        
        # Set style
        plt.style.use('seaborn-v0_8-darkgrid')
        sns.set_palette("husl")
        
    def plot_coherence_cycles(self, session_data: Dict) -> plt.Figure:
        """
        Plot coherence over conversation with cycle markers.
        
        Args:
            session_data: Single session data dictionary
            
        Returns:
            Matplotlib figure
        """
        fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(14, 12), sharex=True)
        
        # Extract data
        positions = [m['position'] for m in session_data['metrics']]
        coherence = [m['coherence'] for m in session_data['metrics']]
        entropy = [m['entropy'] for m in session_data['metrics']]
        
        # Plot 1: Coherence with cycles
        ax1.plot(positions, coherence, 'b-', linewidth=2.5, label='Coherence', alpha=0.8)
        
        # Mark peaks and troughs
        if 'peak_positions' in session_data['cycles']:
            peak_pos = session_data['cycles']['peak_positions']
            if peak_pos:
                ax1.scatter(peak_pos, 
                           [coherence[i] for i in peak_pos if i < len(coherence)], 
                           color='green', s=150, zorder=5, label='Peaks', 
                           marker='^', edgecolors='darkgreen', linewidth=2)
                
        if 'trough_positions' in session_data['cycles']:
            trough_pos = session_data['cycles']['trough_positions']
            if trough_pos:
                ax1.scatter(trough_pos,
                           [coherence[i] for i in trough_pos if i < len(coherence)], 
                           color='red', s=150, zorder=5, label='Troughs',
                           marker='v', edgecolors='darkred', linewidth=2)
        
        # Add coherence mean line
        mean_coherence = session_data['cycles'].get('coherence_mean', np.mean(coherence))
        ax1.axhline(y=mean_coherence, color='gray', linestyle='--', alpha=0.5, 
                   label=f'Mean: {mean_coherence:.3f}')
        
        ax1.set_ylabel('Coherence Score', fontsize=12, fontweight='bold')
        ax1.legend(loc='upper right', framealpha=0.9)
        ax1.grid(True, alpha=0.3)
        ax1.set_title('Coherence Cycles', fontsize=14, fontweight='bold')
        
        # Plot 2: Entropy
        ax2.plot(positions, entropy, 'r-', linewidth=2, label='Shannon Entropy', alpha=0.8)
        ax2.fill_between(positions, entropy, alpha=0.3, color='red')
        ax2.set_ylabel('Shannon Entropy', fontsize=12, fontweight='bold')
        ax2.legend(loc='upper right', framealpha=0.9)
        ax2.grid(True, alpha=0.3)
        ax2.set_title('Information Entropy', fontsize=14, fontweight='bold')
        
        # Plot 3: Phase dominance over time
        for i, metrics in enumerate(session_data['metrics']):
            if 'phase_markers' in metrics:
                dominant_phase = max(metrics['phase_markers'], key=metrics['phase_markers'].get)
                color = self.phase_colors[dominant_phase]
                ax3.add_patch(Rectangle((i-0.45, 0), 0.9, 1, 
                                       facecolor=color, alpha=0.7, edgecolor='black', linewidth=0.5))
        
        # Add phase transitions
        if 'phase_transitions' in session_data['cycles']:
            for transition in session_data['cycles']['phase_transitions']:
                ax3.axvline(x=transition['position']-0.5, color='black', 
                          linestyle='--', alpha=0.5, linewidth=2)
                
        ax3.set_ylabel('Dominant Phase', fontsize=12, fontweight='bold')
        ax3.set_ylim(0, 1)
        ax3.set_yticks([])
        ax3.set_title('Phase Evolution', fontsize=14, fontweight='bold')
        
        # Create legend for phases
        patches = [mpatches.Patch(color=color, label=phase.capitalize()) 
                  for phase, color in self.phase_colors.items()]
        ax3.legend(handles=patches, loc='center left', bbox_to_anchor=(1, 0.5), framealpha=0.9)
        
        # Plot 4: Similarity measures
        if len(session_data['metrics']) > 1:
            similarity_to_first = [m.get('similarity_to_first', 0) for m in session_data['metrics'][1:]]
            similarity_to_prev = [m.get('similarity_to_previous', 0) for m in session_data['metrics'][1:]]
            
            ax4.plot(positions[1:], similarity_to_first, 'g-', linewidth=2, 
                    label='Similarity to First', alpha=0.8)
            ax4.plot(positions[1:], similarity_to_prev, 'm-', linewidth=2, 
                    label='Similarity to Previous', alpha=0.8)
            ax4.set_ylabel('Similarity Score', fontsize=12, fontweight='bold')
            ax4.set_xlabel('Response Position', fontsize=12, fontweight='bold')
            ax4.legend(loc='upper right', framealpha=0.9)
            ax4.grid(True, alpha=0.3)
            ax4.set_title('Semantic Drift', fontsize=14, fontweight='bold')
        
        # Overall title
        model_name = session_data.get('model', 'Unknown')
        session_id = session_data.get('session_id', 0)
        plt.suptitle(f"🐍 Ouroboros Patterns - {model_name} (Session {session_id}) ♾️", 
                    fontsize=16, fontweight='bold')
        
        plt.tight_layout()
        return fig
    
    def create_interactive_cycle_plot(self, session_data: Dict) -> go.Figure:
        """
        Create interactive Plotly visualization of cycles.
        
        Args:
            session_data: Single session data dictionary
            
        Returns:
            Plotly figure
        """
        metrics = session_data['metrics']
        
        # Create figure with secondary y-axis
        fig = go.Figure()
        
        # Add coherence trace
        fig.add_trace(go.Scatter(
            x=[m['position'] for m in metrics],
            y=[m['coherence'] for m in metrics],
            mode='lines+markers',
            name='Coherence',
            line=dict(color='blue', width=3),
            marker=dict(size=8),
            hovertemplate='Position: %{x}<br>Coherence: %{y:.3f}<extra></extra>'
        ))
        
        # Add entropy trace
        fig.add_trace(go.Scatter(
            x=[m['position'] for m in metrics],
            y=[m['entropy'] for m in metrics],
            mode='lines',
            name='Entropy',
            yaxis='y2',
            line=dict(color='red', width=2),
            hovertemplate='Position: %{x}<br>Entropy: %{y:.3f}<extra></extra>'
        ))
        
        # Mark phase transitions with vertical lines
        if 'phase_transitions' in session_data['cycles']:
            for transition in session_data['cycles']['phase_transitions']:
                fig.add_vline(
                    x=transition['position'], 
                    line_dash="dash", 
                    line_color="gray",
                    annotation_text=f"{transition['from_phase'][:3]}→{transition['to_phase'][:3]}",
                    annotation_position="top"
                )
        
        # Mark peaks and troughs
        if 'peak_positions' in session_data['cycles']:
            coherence_values = [m['coherence'] for m in metrics]
            for peak in session_data['cycles']['peak_positions']:
                if peak < len(coherence_values):
                    fig.add_annotation(
                        x=peak, y=coherence_values[peak],
                        text="🔺", showarrow=False,
                        font=dict(size=20, color="green")
                    )
        
        if 'trough_positions' in session_data['cycles']:
            coherence_values = [m['coherence'] for m in metrics]
            for trough in session_data['cycles']['trough_positions']:
                if trough < len(coherence_values):
                    fig.add_annotation(
                        x=trough, y=coherence_values[trough],
                        text="🔻", showarrow=False,
                        font=dict(size=20, color="red")
                    )
        
        # Update layout
        model_name = session_data.get('model', 'Unknown')
        session_id = session_data.get('session_id', 0)
        
        fig.update_layout(
            title=dict(
                text=f"🐍 Ouroboros Cycles - {model_name} (Session {session_id}) ♾️",
                font=dict(size=20)
            ),
            xaxis_title="Response Position",
            yaxis_title="Coherence Score",
            yaxis2=dict(
                title="Shannon Entropy",
                overlaying='y',
                side='right'
            ),
            hovermode='x unified',
            template='plotly_dark',
            height=600,
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01
            )
        )
        
        return fig
    
    def plot_model_comparison(self, model_stats_df: pd.DataFrame) -> plt.Figure:
        """
        Compare ouroboros patterns across models.
        
        Args:
            model_stats_df: DataFrame with model statistics
            
        Returns:
            Matplotlib figure
        """
        fig, axes = plt.subplots(2, 3, figsize=(16, 10))
        fig.suptitle('🐍 Ouroboros Pattern Comparison Across Models ♾️', 
                    fontsize=16, fontweight='bold')
        
        models = model_stats_df['model'].values
        
        # Plot 1: Average cycles
        axes[0, 0].bar(models, model_stats_df['avg_cycles'], 
                      color=['#667eea', '#ff6b6b', '#ffd93d'], alpha=0.8, edgecolor='black')
        axes[0, 0].errorbar(models, model_stats_df['avg_cycles'], 
                           yerr=model_stats_df['std_cycles'], 
                           fmt='none', color='black', capsize=5)
        axes[0, 0].set_title('Average Number of Cycles', fontweight='bold')
        axes[0, 0].set_ylabel('Cycles per Conversation')
        axes[0, 0].grid(True, alpha=0.3)
        
        # Plot 2: Cycle amplitude
        axes[0, 1].bar(models, model_stats_df['avg_cycle_amplitude'],
                      color=['#667eea', '#ff6b6b', '#ffd93d'], alpha=0.8, edgecolor='black')
        axes[0, 1].set_title('Average Cycle Amplitude', fontweight='bold')
        axes[0, 1].set_ylabel('Coherence Range')
        axes[0, 1].grid(True, alpha=0.3)
        
        # Plot 3: Coherence comparison
        axes[0, 2].bar(models, model_stats_df['avg_coherence'],
                      color=['#667eea', '#ff6b6b', '#ffd93d'], alpha=0.8, edgecolor='black')
        axes[0, 2].set_title('Average Coherence', fontweight='bold')
        axes[0, 2].set_ylabel('Coherence Score')
        axes[0, 2].grid(True, alpha=0.3)
        
        # Add expected coherence lines
        for i, model in enumerate(models):
            if model in OUROBOROS_CONFIG['models_to_test']:
                expected = OUROBOROS_CONFIG['models_to_test'][model]['expected_coherence']
                axes[0, 2].axhline(y=expected, xmin=i/3-0.1, xmax=(i+1)/3-0.1, 
                                  color='red', linestyle='--', alpha=0.5)
        
        # Plot 4: Phase distribution (stacked bar)
        phases = ['integration', 'consumption', 'transformation', 'generation']
        phase_data = model_stats_df[[f'{p}_dominance' for p in phases]].values
        
        bottom = np.zeros(len(models))
        for i, phase in enumerate(phases):
            axes[1, 0].bar(models, phase_data[:, i], bottom=bottom, 
                          label=phase.capitalize(), color=self.phase_colors[phase], 
                          alpha=0.8, edgecolor='black')
            bottom += phase_data[:, i]
        
        axes[1, 0].set_title('Phase Distribution', fontweight='bold')
        axes[1, 0].set_ylabel('Proportion')
        axes[1, 0].legend(loc='upper right', framealpha=0.9)
        axes[1, 0].grid(True, alpha=0.3)
        
        # Plot 5: Transition rate
        axes[1, 1].bar(models, model_stats_df['phase_transition_rate'],
                      color=['#667eea', '#ff6b6b', '#ffd93d'], alpha=0.8, edgecolor='black')
        axes[1, 1].set_title('Phase Transition Rate', fontweight='bold')
        axes[1, 1].set_ylabel('Transitions per Response')
        axes[1, 1].grid(True, alpha=0.3)
        
        # Plot 6: Cycle regularity
        axes[1, 2].bar(models, model_stats_df['avg_cycle_regularity'],
                      color=['#667eea', '#ff6b6b', '#ffd93d'], alpha=0.8, edgecolor='black')
        axes[1, 2].set_title('Cycle Regularity', fontweight='bold')
        axes[1, 2].set_ylabel('Standard Deviation (lower = more regular)')
        axes[1, 2].grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig
    
    def create_phase_transition_network(self, sessions: List[Dict]) -> go.Figure:
        """
        Create network visualization of phase transitions.
        
        Args:
            sessions: List of session data
            
        Returns:
            Plotly figure with network graph
        """
        # Count transitions
        transition_counts = {}
        for session in sessions:
            if 'phase_transitions' in session['cycles']:
                for trans in session['cycles']['phase_transitions']:
                    key = (trans['from_phase'], trans['to_phase'])
                    transition_counts[key] = transition_counts.get(key, 0) + 1
        
        if not transition_counts:
            return go.Figure()
        
        # Create network data
        phases = ['integration', 'consumption', 'transformation', 'generation']
        
        # Node positions (circular layout)
        theta = np.linspace(0, 2*np.pi, len(phases), endpoint=False)
        pos = {phase: (np.cos(t), np.sin(t)) for phase, t in zip(phases, theta)}
        
        # Create edges
        edge_trace = []
        for (from_phase, to_phase), count in transition_counts.items():
            x0, y0 = pos[from_phase]
            x1, y1 = pos[to_phase]
            
            edge_trace.append(go.Scatter(
                x=[x0, x1, None],
                y=[y0, y1, None],
                mode='lines',
                line=dict(width=count/max(transition_counts.values())*10, 
                         color='gray'),
                hoverinfo='skip'
            ))
        
        # Create nodes
        node_trace = go.Scatter(
            x=[pos[p][0] for p in phases],
            y=[pos[p][1] for p in phases],
            mode='markers+text',
            text=phases,
            textposition="top center",
            marker=dict(
                size=50,
                color=[self.phase_colors[p] for p in phases],
                line=dict(color='black', width=2)
            ),
            hovertemplate='%{text}<extra></extra>'
        )
        
        # Create figure
        fig = go.Figure(data=edge_trace + [node_trace])
        
        fig.update_layout(
            title="Phase Transition Network",
            showlegend=False,
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            template='plotly_white',
            height=600
        )
        
        return fig
    
    def create_coherence_heatmap(self, all_sessions: Dict[str, List]) -> go.Figure:
        """
        Create heatmap of coherence patterns across models and positions.
        
        Args:
            all_sessions: Dictionary of all session data
            
        Returns:
            Plotly heatmap figure
        """
        # Prepare data for heatmap
        max_length = OUROBOROS_CONFIG['conversation_length']
        models = list(all_sessions.keys())
        
        coherence_matrix = []
        for model in models:
            model_coherence = []
            for pos in range(max_length):
                coherences = []
                for session in all_sessions[model]:
                    if pos < len(session['metrics']):
                        coherences.append(session['metrics'][pos]['coherence'])
                
                avg_coherence = np.mean(coherences) if coherences else 0
                model_coherence.append(avg_coherence)
            
            coherence_matrix.append(model_coherence)
        
        # Create heatmap
        fig = go.Figure(data=go.Heatmap(
            z=coherence_matrix,
            x=[f"Pos {i}" for i in range(max_length)],
            y=models,
            colorscale='Viridis',
            text=np.round(coherence_matrix, 3),
            texttemplate='%{text}',
            textfont={"size": 10},
            colorbar=dict(title="Coherence")
        ))
        
        fig.update_layout(
            title="Coherence Evolution Heatmap",
            xaxis_title="Response Position",
            yaxis_title="Model",
            height=400
        )
        
        return fig
