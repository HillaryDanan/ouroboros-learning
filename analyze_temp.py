import json
import numpy as np

with open('data/intermediate_gpt-3.5-turbo_20250811_165839.json', 'r') as f:
    data = json.load(f)

print(f"Sessions analyzed: {len(data)}")

for session in data[:3]:
    coherences = [m['coherence'] for m in session['metrics']]
    print(f"\nSession {session['session_id']}:")
    print(f"  Coherence range: {min(coherences):.3f} - {max(coherences):.3f}")
    print(f"  Cycles: {session['cycles']['num_peaks']} peaks, {session['cycles']['num_troughs']} troughs")
    print(f"  Phase transitions: {len(session['cycles']['phase_transitions'])}")
