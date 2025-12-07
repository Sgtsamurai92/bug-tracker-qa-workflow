"""
LLM integration helper for OpenAI API.
"""

import os
from openai import OpenAI
from typing import Optional, List, Dict

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def call_llm(
    system_prompt: str,
    user_message: str,
    context: Optional[str] = None,
    model: str = "gpt-4o-mini",
    temperature: float = 0.7,
    max_tokens: int = 2000
) -> str:
    """
    Call the OpenAI API with a system prompt and user message.
    
    Args:
        system_prompt: The system prompt defining the assistant's role
        user_message: The user's question or input
        context: Optional context string (docs, code) to inject into system prompt
        model: OpenAI model to use (default: gpt-4o-mini)
        temperature: Sampling temperature (0-1)
        max_tokens: Maximum tokens in response
        
    Returns:
        The LLM's response as a string
    """
    try:
        # Inject context into system prompt if provided
        if context:
            system_prompt = system_prompt.format(context=context)
        else:
            system_prompt = system_prompt.format(context="No additional context provided.")
        
        # Create chat completion
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error in LLM call: {e}")
        return "I'm sorry, I encountered an error processing your request. Please try again later."


def call_llm_with_history(
    system_prompt: str,
    conversation_history: List[Dict[str, str]],
    context: Optional[str] = None,
    model: str = "gpt-4o-mini",
    temperature: float = 0.7,
    max_tokens: int = 2000
) -> str:
    """
    Call the OpenAI API with conversation history for multi-turn conversations.
    
    Args:
        system_prompt: The system prompt defining the assistant's role
        conversation_history: List of message dicts with 'role' and 'content'
        context: Optional context string (docs, code) to inject
        model: OpenAI model to use
        temperature: Sampling temperature
        max_tokens: Maximum tokens in response
        
    Returns:
        The LLM's response as a string
    """
    try:
        # Inject context into system prompt if provided
        if context:
            system_prompt = system_prompt.format(context=context)
        else:
            system_prompt = system_prompt.format(context="No additional context provided.")
        
        # Build messages list
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(conversation_history)
        
        # Create chat completion
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error in LLM call: {e}")
        return "I'm sorry, I encountered an error processing your request. Please try again later."
