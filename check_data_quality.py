import json
import glob

for file in sorted(glob.glob('data/ouroboros_*_2025*.json')):
    with open(file, 'r') as f:
        data = json.load(f)
    
    model = file.split('_')[1]
    
    # Count error responses
    error_count = 0
    total = 0
    for session in data:
        for response in session['responses']:
            total += 1
            if 'error' in response.lower() or 'api' in response.lower() or len(response) < 50:
                error_count += 1
    
    print(f"{model}: {error_count}/{total} error responses ({error_count/total*100:.1f}%)")
    
    # Show sample
    if data and data[0]['responses']:
        print(f"  Sample: {data[0]['responses'][0][:100]}...")
