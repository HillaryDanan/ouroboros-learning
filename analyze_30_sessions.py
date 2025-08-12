import json
import numpy as np
from collections import Counter

print("🐍♾️ OUROBOROS LEARNING ANALYSIS - 30 SESSIONS GPT-3.5")
print("="*70)

# Load the 30-session data
with open('data/intermediate_gpt-3.5-turbo_20250811_174301.json', 'r') as f:
    data = json.load(f)

print(f"Sessions analyzed: {len(data)}")
print(f"Total responses: {len(data) * 20} real API calls")

# === COHERENCE ANALYSIS ===
print("\n📊 COHERENCE PATTERNS")
print("-"*50)
all_coherences = []
session_ranges = []
session_mins = []

for i, session in enumerate(data):
    coherences = [m['coherence'] for m in session['metrics']]
    all_coherences.extend(coherences)
    range_val = max(coherences) - min(coherences)
    session_ranges.append((i, range_val, min(coherences), max(coherences)))
    session_mins.append(min(coherences))

print(f"Overall coherence: {np.mean(all_coherences):.3f} ± {np.std(all_coherences):.3f}")
print(f"Absolute range: {min(all_coherences):.3f} - {max(all_coherences):.3f}")
print(f"Sessions with coherence < 0.8: {sum(1 for m in session_mins if m < 0.8)}")
print(f"Sessions with coherence < 0.7: {sum(1 for m in session_mins if m < 0.7)}")

# Find outlier sessions
outliers = sorted(session_ranges, key=lambda x: x[2])[:3]  # Lowest min coherence
print("\n🔥 OUTLIER SESSIONS (lowest coherence):")
for sess_id, range_val, min_coh, max_coh in outliers:
    print(f"  Session {sess_id}: {min_coh:.3f} - {max_coh:.3f} (range: {range_val:.3f})")

# === CYCLE DETECTION ===
print("\n🔄 CYCLE PATTERNS")
print("-"*50)
peaks = []
troughs = []
for session in data:
    peaks.append(session['cycles']['num_peaks'])
    troughs.append(session['cycles']['num_troughs'])

print(f"Sessions with peaks: {sum(1 for p in peaks if p > 0)}/30 ({sum(1 for p in peaks if p > 0)/30*100:.1f}%)")
print(f"Sessions with troughs: {sum(1 for t in troughs if t > 0)}/30 ({sum(1 for t in troughs if t > 0)/30*100:.1f}%)")
print(f"Sessions with full cycles (peak+trough): {sum(1 for p, t in zip(peaks, troughs) if p > 0 and t > 0)}/30")
print(f"Average peaks per session: {np.mean(peaks):.2f}")
print(f"Average troughs per session: {np.mean(troughs):.2f}")

# === PHASE ANALYSIS ===
print("\n🎭 PHASE DISTRIBUTION (600 responses)")
print("-"*50)
phase_counts = {'integration': 0, 'consumption': 0, 'transformation': 0, 'generation': 0}
phase_by_position = {i: {'integration': 0, 'consumption': 0, 'transformation': 0, 'generation': 0} 
                     for i in range(20)}

for session in data:
    for i, metric in enumerate(session['metrics']):
        dominant = max(metric['phase_markers'], key=metric['phase_markers'].get)
        phase_counts[dominant] += 1
        phase_by_position[i][dominant] += 1

total = sum(phase_counts.values())
for phase, count in phase_counts.items():
    pct = count/total*100
    bar = '█' * int(pct/2)
    print(f"  {phase:15s}: {pct:5.1f}% {bar}")

# === TRANSFORMATION ANALYSIS ===
print("\n🔮 TRANSFORMATION DEEP DIVE")
print("-"*50)
transformation_sessions = []
for i, session in enumerate(data):
    trans_count = sum(1 for m in session['metrics'] 
                     if max(m['phase_markers'], key=m['phase_markers'].get) == 'transformation')
    transformation_sessions.append((i, trans_count))

transformation_sessions.sort(key=lambda x: x[1], reverse=True)
print("Top transformation sessions:")
for sess_id, count in transformation_sessions[:5]:
    print(f"  Session {sess_id}: {count}/20 transformation responses ({count/20*100:.0f}%)")

# Find where transformation happens in conversations
trans_positions = []
for session in data:
    for i, metric in enumerate(session['metrics']):
        if max(metric['phase_markers'], key=metric['phase_markers'].get) == 'transformation':
            trans_positions.append(i)

if trans_positions:
    print(f"\nTransformation position distribution:")
    print(f"  Most common at position: {Counter(trans_positions).most_common(3)}")
    print(f"  Average position: {np.mean(trans_positions):.1f}")

# === PHASE TRANSITIONS ===
print("\n🔀 PHASE TRANSITIONS")
print("-"*50)
transitions = []
transition_types = []
for session in data:
    trans_count = len(session['cycles']['phase_transitions'])
    transitions.append(trans_count)
    for t in session['cycles']['phase_transitions']:
        transition_types.append(f"{t['from_phase'][:3]}→{t['to_phase'][:3]}")

print(f"Average transitions per session: {np.mean(transitions):.1f}")
print(f"Range: {min(transitions)} - {max(transitions)}")
print(f"Sessions with >15 transitions: {sum(1 for t in transitions if t > 15)}")

print("\nMost common transition types:")
for trans_type, count in Counter(transition_types).most_common(5):
    print(f"  {trans_type}: {count} times")

# === KEY INSIGHTS ===
print("\n✨ KEY INSIGHTS FROM 30 SESSIONS")
print("="*70)
print(f"1. Coherence is remarkably stable: {np.mean(all_coherences):.1%} average")
print(f"2. Transformation is suppressed: only {phase_counts['transformation']/total*100:.1f}% of responses")
print(f"3. Cycling is minimal: {sum(1 for p in peaks if p > 0)/30*100:.0f}% show peaks")
print(f"4. Phase transitions are frequent but shallow: {np.mean(transitions):.1f} per session")
print(f"5. GPT-3.5 appears to be 'transformation-averse' rather than 'chaotic'")

# === HYPOTHESIS UPDATE ===
print("\n🎯 HYPOTHESIS STATUS")
print("-"*50)
print("❌ Original: GPT-3.5 would show 38.3% coherence with chaotic patterns")
print(f"✅ Actual: GPT-3.5 shows {np.mean(all_coherences):.1%} coherence with rigid patterns")
print("💡 Discovery: Models differ in TRANSFORMATION WILLINGNESS, not coherence!")
