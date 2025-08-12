# api_integration.py
"""
API integration for data collection
Hillary Danan - August 2025
"""

import os
import openai
import anthropic
import google.generativeai as genai
from typing import List, Optional
from dotenv import load_dotenv
import time

load_dotenv()

class RealModelAPI:
    """
    Real API calls to actual models for empirical data collection.
    """
    
    def __init__(self):
        """Initialize API clients with real keys."""
        # OpenAI
        self.openai_key = os.getenv('OPENAI_API_KEY')
        if self.openai_key:
            openai.api_key = self.openai_key
            self.openai_client = openai  # Just use the module directly
        else:
            print("⚠️ WARNING: No OpenAI API key found")
            self.openai_client = None
            
        # Anthropic
        self.anthropic_key = os.getenv('ANTHROPIC_API_KEY')
        if self.anthropic_key:
            self.anthropic_client = anthropic.Anthropic(api_key=self.anthropic_key)
        else:
            print("⚠️ WARNING: No Anthropic API key found")
            self.anthropic_client = None
            
        # Google
        self.google_key = os.getenv('GOOGLE_API_KEY')
        if self.google_key:
            genai.configure(api_key=self.google_key)
            self.gemini_model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            print("⚠️ WARNING: No Google API key found")
            self.gemini_model = None
    
    def get_response(self, model_name: str, prompt: str, 
                    conversation_history: List[str]) -> str:
        """
        Get REAL response from ACTUAL model.
        
        Args:
            model_name: Which model to query
            prompt: Current prompt
            conversation_history: Previous responses in conversation
            
        Returns:
            ACTUAL model response (not synthetic!)
        """
        try:
            # Build conversation context
            context = self._build_context(conversation_history, prompt)
            
            if 'gpt' in model_name.lower():
                return self._get_openai_response(model_name, context)
            elif 'claude' in model_name.lower():
                return self._get_anthropic_response(model_name, context)
            elif 'gemini' in model_name.lower():
                return self._get_gemini_response(context)
            else:
                raise ValueError(f"Unknown model: {model_name}")
                
        except Exception as e:
            print(f"⚠️ API Error for {model_name}: {e}")
            # Log error but continue with data collection
            return f"Error getting response: {str(e)}"
    
    def _build_context(self, history: List[str], current_prompt: str) -> List[dict]:
        """
        Build conversation context for API calls.
        
        Args:
            history: Previous responses
            current_prompt: Current prompt
            
        Returns:
            Formatted conversation for API
        """
        messages = []
        
        # Add system message for consistency
        messages.append({
            "role": "system",
            "content": "You are participating in a research study on cognitive patterns. Please respond naturally and thoughtfully to each prompt."
        })
        
        # Add conversation history (alternating user/assistant)
        for i, response in enumerate(history):
            # Previous prompts would have been user messages
            if i < len(history):
                messages.append({
                    "role": "assistant",
                    "content": response
                })
        
        # Add current prompt
        messages.append({
            "role": "user",
            "content": current_prompt
        })
        
        return messages
    
    def _get_openai_response(self, model_name: str, messages: List[dict]) -> str:
        """
        Get REAL response from OpenAI GPT model.
        
        Args:
            model_name: Specific GPT model
            messages: Conversation context
            
        Returns:
            Actual GPT response
        """
        if not self.openai_client:
            return "OpenAI API key not configured"
        
        try:
            # Use the new OpenAI 1.0+ format
            from openai import OpenAI
            client = OpenAI(api_key=self.openai_key)
            
            response = client.chat.completions.create(
                model=model_name,
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            
            # Rate limiting
            time.sleep(5)
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"OpenAI API error: {e}")
            return f"OpenAI error: {str(e)}"
    
    def _get_anthropic_response(self, model_name: str, messages: List[dict]) -> str:
        """
        Get REAL response from Anthropic Claude model.
        
        Args:
            model_name: Specific Claude model
            messages: Conversation context
            
        Returns:
            Actual Claude response
        """
        if not self.anthropic_client:
            return "Anthropic API key not configured"
        
        try:
            # Convert to Anthropic format
            system_msg = messages[0]["content"] if messages[0]["role"] == "system" else ""
            claude_messages = []
            
            for msg in messages[1:]:  # Skip system message
                claude_messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
            
            response = self.anthropic_client.messages.create(
                model=model_name,
                max_tokens=500,
                temperature=0.7,
                system=system_msg,
                messages=claude_messages
            )
            
            # Rate limiting
            time.sleep(5)
            
            return response.content[0].text
            
        except Exception as e:
            print(f"Anthropic API error: {e}")
            return f"Anthropic error: {str(e)}"
    
    def _get_gemini_response(self, messages: List[dict]) -> str:
        """
        Get REAL response from Google Gemini model.
        
        Args:
            messages: Conversation context
            
        Returns:
            Actual Gemini response
        """
        if not self.gemini_model:
            return "Google API key not configured"
        
        try:
            # Build Gemini prompt from messages
            prompt_parts = []
            for msg in messages:
                if msg["role"] == "user":
                    prompt_parts.append(f"User: {msg['content']}")
                elif msg["role"] == "assistant":
                    prompt_parts.append(f"Assistant: {msg['content']}")
                elif msg["role"] == "system":
                    prompt_parts.append(f"System: {msg['content']}")
            
            full_prompt = "\n\n".join(prompt_parts)
            full_prompt += "\n\nAssistant:"
            
            response = self.gemini_model.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=500,
                )
            )
            
            # Rate limiting
            time.sleep(5)
            
            return response.text
            
        except Exception as e:
            print(f"Gemini API error: {e}")
            return f"Gemini error: {str(e)}"
    
    def verify_apis_configured(self) -> dict:
        """
        Verify which APIs are properly configured.
        
        Returns:
            Dictionary of API status
        """
        status = {
            'openai': self.openai_client is not None,
            'anthropic': self.anthropic_client is not None,
            'gemini': self.gemini_model is not None
        }
        
        print("\n🔑 API Configuration Status:")
        print("-" * 40)
        for api, configured in status.items():
            symbol = "✅" if configured else "❌"
            print(f"{symbol} {api.capitalize()}: {'Configured' if configured else 'Missing'}")
        print("-" * 40)
        
        return status
    
    def test_apis(self) -> dict:
        """
        Test each API with a simple call.
        
        Returns:
            Test results for each API
        """
        print("\n🧪 Testing APIs with real calls...")
        results = {}
        
        test_prompt = "Say 'API working' if you receive this."
        
        # Test OpenAI
        if self.openai_client:
            try:
                test_messages = [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": test_prompt}
                ]
                response = self._get_openai_response("gpt-3.5-turbo", test_messages)
                results['openai'] = 'working' in response.lower() if response else False
                print(f"✅ OpenAI: {response[:50] if response else 'No response'}...")
            except Exception as e:
                results['openai'] = False
                print(f"❌ OpenAI failed: {e}")
        
        # Test Anthropic
        if self.anthropic_client:
            try:
                test_messages = [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": test_prompt}
                ]
                response = self._get_anthropic_response("claude-3-haiku-20240307", test_messages)
                results['anthropic'] = 'working' in response.lower() if response else False
                print(f"✅ Anthropic: {response[:50] if response else 'No response'}...")
            except Exception as e:
                results['anthropic'] = False
                print(f"❌ Anthropic failed: {e}")
        
        # Test Gemini
        if self.gemini_model:
            try:
                test_messages = [{"role": "user", "content": test_prompt}]
                response = self._get_gemini_response(test_messages)
                results['gemini'] = 'working' in response.lower() if response else False
                print(f"✅ Gemini: {response[:50] if response else 'No response'}...")
            except Exception as e:
                results['gemini'] = False
                print(f"❌ Gemini failed: {e}")
        
        return results

# Global API instance
api_client = None

def initialize_apis():
    """Initialize the global API client."""
    global api_client
    api_client = RealModelAPI()
    return api_client

def get_real_model_response(model_name: str, prompt: str, 
                           conversation_history: List[str]) -> str:
    """
    Public interface for getting real model responses.
    
    Args:
        model_name: Model to query
        prompt: Current prompt
        conversation_history: Previous responses
        
    Returns:
        Real model response
    """
    global api_client
    
    if api_client is None:
        api_client = initialize_apis()
    
    return api_client.get_response(model_name, prompt, conversation_history)
