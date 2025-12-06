"""
Context builder for gathering relevant documentation and code from the repository.
"""

import os
from pathlib import Path
from typing import List, Set


# File extensions to include in context
RELEVANT_EXTENSIONS = {'.md', '.txt', '.py', '.html', '.css', '.js'}

# Directories to exclude from scanning
EXCLUDE_DIRS = {
    '__pycache__', 'node_modules', '.git', '.venv', 'venv',
    'env', 'instance', 'reports', 'screenshots', '.pytest_cache'
}


def scan_directory(directory: Path, extensions: Set[str], max_file_size: int = 100000) -> List[tuple]:
    """
    Recursively scan a directory for files with specific extensions.
    
    Args:
        directory: Path object pointing to the directory to scan
        extensions: Set of file extensions to include (e.g., {'.md', '.py'})
        max_file_size: Maximum file size in bytes (default 100KB)
        
    Returns:
        List of tuples: (file_path, file_content)
    """
    files_content = []
    
    try:
        for item in directory.rglob('*'):
            # Skip excluded directories
            if any(excluded in item.parts for excluded in EXCLUDE_DIRS):
                continue
            
            # Check if it's a file with relevant extension
            if item.is_file() and item.suffix in extensions:
                # Skip large files
                if item.stat().st_size > max_file_size:
                    continue
                
                try:
                    with open(item, 'r', encoding='utf-8') as f:
                        content = f.read()
                        relative_path = item.relative_to(directory.parent)
                        files_content.append((str(relative_path), content))
                except (UnicodeDecodeError, PermissionError):
                    # Skip files that can't be read
                    continue
    
    except Exception as e:
        print(f"Error scanning directory {directory}: {e}")
    
    return files_content


def build_context(
    base_path: str,
    query: str = "",
    include_docs: bool = True,
    include_code: bool = False,
    max_context_length: int = 15000
) -> str:
    """
    Build a context string from repository documentation and optionally code.
    
    Args:
        base_path: Root path of the repository
        query: Optional search query to filter relevant content
        include_docs: Whether to include documentation files
        include_code: Whether to include source code files
        max_context_length: Maximum length of context string (in characters)
        
    Returns:
        Formatted context string containing relevant content
    """
    context_parts = []
    total_length = 0
    
    base = Path(base_path)
    
    # Scan documentation directory
    if include_docs:
        docs_dir = base / 'docs'
        if docs_dir.exists():
            doc_files = scan_directory(docs_dir, {'.md', '.txt'})
            for file_path, content in doc_files:
                if total_length + len(content) > max_context_length:
                    break
                context_parts.append(f"## File: {file_path}\n\n{content}\n")
                total_length += len(content)
        
        # Also include root-level markdown files
        for md_file in base.glob('*.md'):
            if total_length >= max_context_length:
                break
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if total_length + len(content) <= max_context_length:
                        context_parts.append(f"## File: {md_file.name}\n\n{content}\n")
                        total_length += len(content)
            except (UnicodeDecodeError, PermissionError):
                continue
    
    # Scan help articles
    help_articles_dir = base / 'help_articles'
    if help_articles_dir.exists():
        article_files = scan_directory(help_articles_dir, {'.md'})
        for file_path, content in article_files:
            if total_length + len(content) > max_context_length:
                break
            context_parts.append(f"## Help Article: {file_path}\n\n{content}\n")
            total_length += len(content)
    
    # Optionally scan source code (be selective)
    if include_code and total_length < max_context_length:
        app_dir = base / 'app'
        if app_dir.exists():
            # Only include main app files, not everything
            key_files = ['app.py', 'models.py']
            for key_file in key_files:
                file_path = app_dir / key_file
                if file_path.exists() and total_length < max_context_length:
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if total_length + len(content) <= max_context_length:
                                context_parts.append(f"## Source Code: app/{key_file}\n\n{content}\n")
                                total_length += len(content)
                    except (UnicodeDecodeError, PermissionError):
                        continue
    
    if not context_parts:
        return "No documentation or context files found in the repository."
    
    return "\n---\n".join(context_parts)


def search_context(context: str, keywords: List[str]) -> str:
    """
    Filter context based on keyword relevance (simple implementation).
    
    Args:
        context: The full context string
        keywords: List of keywords to search for
        
    Returns:
        Filtered context containing relevant sections
    """
    if not keywords:
        return context
    
    # Simple keyword matching - split by file sections
    sections = context.split("## File:")
    relevant_sections = []
    
    for section in sections:
        section_lower = section.lower()
        if any(keyword.lower() in section_lower for keyword in keywords):
            relevant_sections.append(section)
    
    if relevant_sections:
        return "## File:".join(relevant_sections)
    
    return context  # Return full context if no matches
