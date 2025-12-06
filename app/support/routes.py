"""
Flask routes for support chat functionality.
"""

import os
import json
from datetime import datetime
from pathlib import Path
from flask import Blueprint, request, jsonify, current_app

from .llm_helper import call_llm, call_llm_with_history
from .context_builder import build_context
from .prompts import SUPPORT_ASSISTANT_PROMPT, ARTICLE_GENERATION_PROMPT

support_bp = Blueprint('support', __name__, url_prefix='/api/support')


def extract_proposed_article(response_text):
    """
    Extract the proposed help article from the assistant's response.
    
    Args:
        response_text: The full response from the LLM
        
    Returns:
        tuple: (has_article: bool, article_content: str or None, title: str or None)
    """
    start_marker = '=== PROPOSED_HELP_ARTICLE ==='
    end_marker = '=== END_PROPOSED_HELP_ARTICLE ==='
    
    if start_marker in response_text and end_marker in response_text:
        start_idx = response_text.index(start_marker) + len(start_marker)
        end_idx = response_text.index(end_marker)
        
        article_block = response_text[start_idx:end_idx].strip()
        
        # Extract title
        title_match = None
        for line in article_block.split('\n'):
            if line.strip().startswith('Title:'):
                title_match = line.split('Title:', 1)[1].strip()
                break
        
        return True, article_block, title_match or 'Help Article'
    
    return False, None, None


@support_bp.route('/chat', methods=['POST'])
def chat():
    """
    Handle incoming chat messages from the support widget.
    
    Expected JSON payload:
    {
        "message": "How do I create a bug report?",
        "conversation": [  // Optional: conversation history
            {"role": "user", "content": "..."},
            {"role": "assistant", "content": "..."}
        ]
    }
    
    Returns:
    {
        "reply": "To create a bug report...",
        "timestamp": "2025-12-06T10:30:00"
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400
        
        user_message = data['message']
        conversation_history = data.get('conversation', [])
        
        # Get repository base path
        base_path = current_app.config.get('BASE_PATH', os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        
        # Build context from documentation and code
        context = build_context(
            base_path=base_path,
            query=user_message,
            include_docs=True,
            include_code=True
        )
        
        # Call LLM
        if conversation_history:
            # Add current message to history
            conversation_history.append({"role": "user", "content": user_message})
            reply = call_llm_with_history(
                system_prompt=SUPPORT_ASSISTANT_PROMPT,
                conversation_history=conversation_history,
                context=context
            )
        else:
            reply = call_llm(
                system_prompt=SUPPORT_ASSISTANT_PROMPT,
                user_message=user_message,
                context=context
            )
        
        return jsonify({
            'reply': reply,
            'timestamp': datetime.utcnow().isoformat()
        })
    
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@support_bp.route('/generate-article', methods=['POST'])
def generate_article():
    """
    Generate a new help article based on the conversation and topic.
    
    Expected JSON payload:
    {
        "topic": "Creating a Bug Report",
        "conversation": [
            {"role": "user", "content": "..."},
            {"role": "assistant", "content": "..."}
        ]
    }
    
    Returns:
    {
        "success": true,
        "article_path": "help_articles/creating-a-bug-report.md",
        "title": "Creating a Bug Report"
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'topic' not in data:
            return jsonify({'error': 'Topic is required'}), 400
        
        topic = data['topic']
        conversation = data.get('conversation', [])
        
        # Get repository base path
        base_path = current_app.config.get('BASE_PATH', os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        
        # Check if the last assistant message contains a proposed article
        article_content = None
        if conversation:
            for msg in reversed(conversation):
                if msg.get('role') == 'assistant':
                    has_article, extracted_content, extracted_title = extract_proposed_article(msg.get('content', ''))
                    if has_article:
                        # Use the extracted article content directly
                        article_content = extracted_content
                        # Update topic if we found a better title
                        if extracted_title:
                            topic = extracted_title
                        break
        
        # If no proposed article was found in conversation, generate a new one
        if not article_content:
            # Build context
            context = build_context(
                base_path=base_path,
                query=topic,
                include_docs=True,
                include_code=True
            )
            
            # Format conversation history as string
            conversation_text = "\n".join([
                f"{msg['role'].upper()}: {msg['content']}"
                for msg in conversation
            ])
            
            # Generate article using LLM
            article_prompt = ARTICLE_GENERATION_PROMPT.format(
                context=context,
                conversation=conversation_text,
                topic=topic
            )
            
            article_content = call_llm(
                system_prompt="You are a technical documentation writer.",
                user_message=article_prompt,
                temperature=0.7
            )
        
        # Save article to file
        help_articles_dir = Path(base_path) / 'help_articles'
        help_articles_dir.mkdir(exist_ok=True)
        
        # Create filename from topic
        filename = topic.lower().replace(' ', '-').replace('/', '-')
        filename = ''.join(c for c in filename if c.isalnum() or c in ('-', '_'))
        filename = f"{filename}.md"
        
        article_path = help_articles_dir / filename
        
        with open(article_path, 'w', encoding='utf-8') as f:
            f.write(f"# {topic}\n\n")
            f.write(f"_Generated on {datetime.utcnow().strftime('%Y-%m-%d')}_\n\n")
            f.write(article_content)
        
        return jsonify({
            'success': True,
            'article_path': f"help_articles/{filename}",
            'title': topic,
            'content': article_content
        })
    
    except Exception as e:
        print(f"Error in generate-article endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@support_bp.route('/articles', methods=['GET'])
def list_articles():
    """
    List all available help articles.
    
    Returns:
    {
        "articles": [
            {
                "title": "Creating a Bug Report",
                "path": "help_articles/creating-a-bug-report.md",
                "created": "2025-12-06T10:30:00"
            }
        ]
    }
    """
    try:
        base_path = current_app.config.get('BASE_PATH', os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        help_articles_dir = Path(base_path) / 'help_articles'
        
        articles = []
        
        if help_articles_dir.exists():
            for article_file in help_articles_dir.glob('*.md'):
                try:
                    with open(article_file, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        # Extract title from first heading
                        title = article_file.stem.replace('-', ' ').title()
                        for line in lines:
                            if line.startswith('# '):
                                title = line[2:].strip()
                                break
                        
                        articles.append({
                            'title': title,
                            'path': f"help_articles/{article_file.name}",
                            'created': datetime.fromtimestamp(article_file.stat().st_mtime).isoformat()
                        })
                except Exception as e:
                    print(f"Error reading article {article_file}: {e}")
                    continue
        
        return jsonify({'articles': articles})
    
    except Exception as e:
        print(f"Error in list-articles endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@support_bp.route('/article/<path:filename>', methods=['GET'])
def get_article(filename):
    """
    Get the content of a specific help article.
    
    Returns:
    {
        "title": "Creating a Bug Report",
        "content": "# Creating a Bug Report\n\n..."
    }
    """
    try:
        base_path = current_app.config.get('BASE_PATH', os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        article_path = Path(base_path) / 'help_articles' / filename
        
        if not article_path.exists() or not article_path.is_file():
            return jsonify({'error': 'Article not found'}), 404
        
        with open(article_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract title
            title = filename.replace('-', ' ').replace('.md', '').title()
            lines = content.split('\n')
            for line in lines:
                if line.startswith('# '):
                    title = line[2:].strip()
                    break
        
        return jsonify({
            'title': title,
            'content': content
        })
    
    except Exception as e:
        print(f"Error in get-article endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500
