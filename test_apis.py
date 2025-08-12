#!/usr/bin/env python3
"""
Test API connections before running full analysis
Hillary Danan - August 2025
<4577> <45774EVER
"""

import sys
sys.path.append('src')

from src.api_integration import RealModelAPI

def main():
    print("\n🔬 TESTING API CONNECTIONS")
    print("="*50)
    
    # Initialize APIs
    api = RealModelAPI()
    
    # Check configuration
    status = api.verify_apis_configured()
    
    # Count configured APIs
    configured_count = sum(status.values())
    
    if configured_count == 0:
        print("\n❌ NO APIS CONFIGURED!")
        print("\nTo add API keys:")
        print("1. Edit .env file")
        print("2. Add your keys:")
        print("   OPENAI_API_KEY=your_key_here")
        print("   ANTHROPIC_API_KEY=your_key_here")
        print("   GOOGLE_API_KEY=your_key_here")
        return False
    
    print(f"\n✅ {configured_count}/3 APIs configured")
    
    # Test each API
    print("\n🧪 Testing API calls...")
    print("-"*50)
    
    test_results = api.test_apis()
    
    # Summary
    working_count = sum(test_results.values())
    print("-"*50)
    print(f"\n📊 RESULTS: {working_count}/{len(test_results)} APIs working")
    
    if working_count > 0:
        print("\n✅ Ready to collect REAL ouroboros data!")
        print("\nRun: python3 run_ouroboros_analysis.py")
        return True
    else:
        print("\n⚠️ Fix API issues before running analysis")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
