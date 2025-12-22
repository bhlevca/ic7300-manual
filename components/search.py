"""
Search Component
Full-text search functionality for the manual.
"""

from pathlib import Path
from typing import List, Dict
import re


def search_content(query: str, max_results: int = 10) -> List[Dict]:
    """
    Search all chapter content for the query.
    
    Args:
        query: Search query string.
        max_results: Maximum number of results to return.
        
    Returns:
        List of search result dictionaries.
    """
    results = []
    query_lower = query.lower()
    query_words = query_lower.split()
    
    # Get content directory
    content_dir = Path(__file__).parent.parent / "content" / "chapters"
    
    if not content_dir.exists():
        return results
    
    for chapter_file in content_dir.glob("*.md"):
        try:
            content = chapter_file.read_text(encoding='utf-8')
            content_lower = content.lower()
            
            # Check if any query words appear in content
            matches = sum(1 for word in query_words if word in content_lower)
            
            if matches > 0:
                # Extract title from first heading
                title = chapter_file.stem.replace('_', ' ').title()
                for line in content.split('\n'):
                    if line.startswith('# '):
                        title = line[2:].strip()
                        break
                
                # Find excerpt around first match
                excerpt = extract_excerpt(content, query_words)
                
                results.append({
                    'file': chapter_file.name,
                    'title': title,
                    'excerpt': excerpt,
                    'score': matches
                })
        except Exception as e:
            continue
    
    # Sort by score (number of matches)
    results.sort(key=lambda x: x['score'], reverse=True)
    
    return results[:max_results]


def extract_excerpt(content: str, query_words: List[str], context_chars: int = 150) -> str:
    """
    Extract an excerpt from content around the first match.
    
    Args:
        content: Full content text.
        query_words: List of query words to find.
        context_chars: Number of characters to include before/after match.
        
    Returns:
        Excerpt string with match highlighted.
    """
    content_lower = content.lower()
    
    # Find first occurrence of any query word
    first_pos = len(content)
    matched_word = ""
    
    for word in query_words:
        pos = content_lower.find(word)
        if pos != -1 and pos < first_pos:
            first_pos = pos
            matched_word = word
    
    if first_pos == len(content):
        # No match found, return beginning of content
        return content[:context_chars * 2] + "..."
    
    # Extract context around match
    start = max(0, first_pos - context_chars)
    end = min(len(content), first_pos + len(matched_word) + context_chars)
    
    excerpt = content[start:end]
    
    # Clean up excerpt
    excerpt = excerpt.replace('\n', ' ').replace('  ', ' ').strip()
    
    # Add ellipsis if truncated
    if start > 0:
        excerpt = "..." + excerpt
    if end < len(content):
        excerpt = excerpt + "..."
    
    return excerpt


def build_search_index(content_dir: Path) -> Dict:
    """
    Build a search index for faster searching.
    
    Args:
        content_dir: Path to content directory.
        
    Returns:
        Search index dictionary.
    """
    index = {
        'documents': [],
        'word_index': {}
    }
    
    for chapter_file in content_dir.glob("**/*.md"):
        try:
            content = chapter_file.read_text(encoding='utf-8')
            
            # Extract title
            title = chapter_file.stem.replace('_', ' ').title()
            for line in content.split('\n'):
                if line.startswith('# '):
                    title = line[2:].strip()
                    break
            
            doc_id = len(index['documents'])
            index['documents'].append({
                'id': doc_id,
                'file': str(chapter_file.relative_to(content_dir)),
                'title': title,
                'content': content
            })
            
            # Build word index
            words = re.findall(r'\b\w+\b', content.lower())
            for word in set(words):
                if word not in index['word_index']:
                    index['word_index'][word] = []
                if doc_id not in index['word_index'][word]:
                    index['word_index'][word].append(doc_id)
                    
        except Exception as e:
            continue
    
    return index


def search_index(index: Dict, query: str) -> List[Dict]:
    """
    Search using the pre-built index.
    
    Args:
        index: Search index dictionary.
        query: Search query string.
        
    Returns:
        List of matching documents.
    """
    query_words = re.findall(r'\b\w+\b', query.lower())
    
    if not query_words:
        return []
    
    # Find documents matching all query words
    matching_docs = None
    
    for word in query_words:
        if word in index['word_index']:
            word_docs = set(index['word_index'][word])
            if matching_docs is None:
                matching_docs = word_docs
            else:
                matching_docs = matching_docs.intersection(word_docs)
        else:
            matching_docs = set()
            break
    
    if not matching_docs:
        return []
    
    # Return matching documents
    results = []
    for doc_id in matching_docs:
        doc = index['documents'][doc_id]
        excerpt = extract_excerpt(doc['content'], query_words)
        results.append({
            'file': doc['file'],
            'title': doc['title'],
            'excerpt': excerpt
        })
    
    return results
