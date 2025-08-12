import json
import glob

for file in sorted(glob.glob('data/ouroboros_*_*.json')):
    with open(file, 'r') as f:
        data = json.load(f)
    
    model = file.split('_')[1]
    
    # Count transformations
    total_transform = 0
    for session in data[:10]:  # First 10 sessions
        for metric in session['metrics']:
            if max(metric['phase_markers'], key=metric['phase_markers'].get) == 'transformation':
                total_transform += 1
    
    transform_rate = total_transform / (len(data[:10]) * 20) * 100
    print(f"{model}: {transform_rate:.1f}% transformation rate")
