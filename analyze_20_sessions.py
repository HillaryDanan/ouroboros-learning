import json
import numpy as np

# Load the 20-session data
with open('data/intermediate_gpt-3.5-turbo_20250811_172113.json', 'r') as f:
    data = json.load(f)

print(f"🎯 GPT-3.5 ANALYSIS - 20 SESSIONS")
print("="*60)

# Overall stats
all_coherences = []
all_peaks = []
all_troughs = []
all_transitions = []

for session in data:
    coherences = [m['coherence'] for m in session['metrics']]
    all_coherences.extend(coherences)
    all_peaks.append(session['cycles']['num_peaks'])
    all_troughs.append(session['cycles']['num_troughs'])
    all_transitions.append(len(session['cycles']['phase_transitions']))

print(f"\n📊 COHERENCE STATS:")
print(f"  Overall range: {min(all_coherences):.3f} - {max(all_coherences):.3f}")
print(f"  Mean: {np.mean(all_coherences):.3f}")
print(f"  Std Dev: {np.std(all_coherences):.3f}")

print(f"\n🔄 CYCLE PATTERNS:")
print(f"  Avg peaks per session: {np.mean(all_peaks):.1f}")
print(f"  Avg troughs per session: {np.mean(all_troughs):.1f}")
print(f"  Sessions with cycles: {sum(1 for p in all_peaks if p > 0)}/20")

print(f"\n🎭 PHASE TRANSITIONS:")
print(f"  Avg per session: {np.mean(all_transitions):.1f}")
print(f"  Min-Max: {min(all_transitions)} - {max(all_transitions)}")

# Phase distribution
phase_counts = {'integration': 0, 'consumption': 0, 'transformation': 0, 'generation': 0}
for session in data:
    for metric in session['metrics']:
        dominant = max(metric['phase_markers'], key=metric['phase_markers'].get)
        phase_counts[dominant] += 1

total = sum(phase_counts.values())
print(f"\n🎨 PHASE DISTRIBUTION (400 responses):")
for phase, count in phase_counts.items():
    print(f"  {phase}: {count/total*100:.1f}%")

# Find most interesting session
coherence_ranges = []
for i, session in enumerate(data):
    coherences = [m['coherence'] for m in session['metrics']]
    range_val = max(coherences) - min(coherences)
    coherence_ranges.append((i, range_val, min(coherences)))

most_variable = max(coherence_ranges, key=lambda x: x[1])
print(f"\n🔥 MOST VARIABLE SESSION: #{most_variable[0]}")
print(f"  Coherence range: {most_variable[1]:.3f}")
print(f"  Minimum coherence: {most_variable[2]:.3f}")
