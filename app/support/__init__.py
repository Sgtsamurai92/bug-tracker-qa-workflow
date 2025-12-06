"""
Support chat module for the bug tracker application.
Provides LLM-powered support with context from repository documentation.
"""

from .routes import support_bp

__all__ = ['support_bp']
