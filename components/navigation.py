"""
Navigation Component
Handles sidebar navigation and chapter management.
"""

from pathlib import Path
from typing import List, Dict, Optional


def get_chapter_list() -> List[Dict]:
    """
    Get ordered list of chapters with metadata.
    
    Returns:
        List of chapter dictionaries with 'file', 'title', and 'icon' keys.
    """
    chapters = [
        # Getting Started
        {"file": "01_introduction.md", "title": "Introduction", "icon": "📘", "section": "Getting Started"},
        {"file": "05_station_setup.md", "title": "Station Setup", "icon": "🏠", "section": "Getting Started"},
        
        # Device Description (renamed from Hardware)
        {"file": "02_front_panel.md", "title": "Front Panel", "icon": "🎛️", "section": "Device Description"},
        {"file": "03_rear_panel.md", "title": "Rear Panel", "icon": "🔌", "section": "Device Description"},
        {"file": "09_touchscreen_menus.md", "title": "Touch Screen & Menus", "icon": "📱", "section": "Device Description"},
        {"file": "15_installation_connections.md", "title": "Installation & Connections", "icon": "🔗", "section": "Device Description"},
        
        # Operation
        {"file": "04_basic_operations.md", "title": "Basic Operations", "icon": "⚙️", "section": "Operation"},
        {"file": "16_receiving_transmitting.md", "title": "Receiving & Transmitting", "icon": "📡", "section": "Operation"},
        {"file": "17_scope_operation.md", "title": "Scope Operation", "icon": "📊", "section": "Operation"},
        {"file": "10_operating_scenarios.md", "title": "Operating Scenarios", "icon": "📻", "section": "Operation"},
        {"file": "06_antenna_swr.md", "title": "Antenna & SWR", "icon": "🔧", "section": "Operation"},
        
        # Digital Modes
        {"file": "07_digital_modes.md", "title": "Digital Modes Overview", "icon": "💻", "section": "Digital"},
        {"file": "11_digital_modes_detailed.md", "title": "Digital Modes In-Depth", "icon": "🖥️", "section": "Digital"},
        {"file": "08_wsjt_ft8.md", "title": "WSJT-X / FT8", "icon": "📶", "section": "Digital"},
        
        # Reference
        {"file": "12_troubleshooting.md", "title": "Troubleshooting", "icon": "🛠️", "section": "Reference"},
        {"file": "13_glossary.md", "title": "Glossary", "icon": "📖", "section": "Reference"},
        {"file": "14_quick_reference_card.md", "title": "Quick Reference Card", "icon": "📋", "section": "Reference"},
    ]
    return chapters


def get_chapters_by_section() -> Dict[str, List[Dict]]:
    """
    Get chapters organized by section.
    
    Returns:
        Dictionary with section names as keys and chapter lists as values.
    """
    chapters = get_chapter_list()
    sections = {}
    for chapter in chapters:
        section = chapter.get("section", "Other")
        if section not in sections:
            sections[section] = []
        sections[section].append(chapter)
    return sections


def get_quick_refs() -> List[Dict]:
    """
    Get list of quick reference documents.
    
    Returns:
        List of quick reference dictionaries.
    """
    return [
        {"file": "quick_refs/button_shortcuts.md", "title": "Button Shortcuts", "icon": "⌨️"},
        {"file": "quick_refs/menu_tree.md", "title": "Menu Tree", "icon": "📑"},
        {"file": "quick_refs/band_frequencies.md", "title": "Band Frequencies", "icon": "📻"},
    ]


def get_chapter_by_file(filename: str) -> Optional[Dict]:
    """
    Get chapter metadata by filename.
    
    Args:
        filename: The chapter filename.
        
    Returns:
        Chapter dictionary or None if not found.
    """
    chapters = get_chapter_list()
    for chapter in chapters:
        if chapter['file'] == filename:
            return chapter
    return None


def get_next_chapter(current_file: str) -> Optional[Dict]:
    """
    Get the next chapter after the current one.
    
    Args:
        current_file: Current chapter filename.
        
    Returns:
        Next chapter dictionary or None if at end.
    """
    chapters = get_chapter_list()
    for i, chapter in enumerate(chapters):
        if chapter['file'] == current_file:
            if i < len(chapters) - 1:
                return chapters[i + 1]
    return None


def get_prev_chapter(current_file: str) -> Optional[Dict]:
    """
    Get the previous chapter before the current one.
    
    Args:
        current_file: Current chapter filename.
        
    Returns:
        Previous chapter dictionary or None if at start.
    """
    chapters = get_chapter_list()
    for i, chapter in enumerate(chapters):
        if chapter['file'] == current_file:
            if i > 0:
                return chapters[i - 1]
    return None


def render_sidebar():
    """
    Render the sidebar navigation.
    This is called from the main app.
    """
    # Implementation moved to main app.py for Streamlit context
    pass


def build_toc(content: str) -> List[Dict]:
    """
    Build a table of contents from markdown content.
    
    Args:
        content: Markdown content string.
        
    Returns:
        List of TOC entries with 'level', 'title', and 'anchor' keys.
    """
    toc = []
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('#'):
            # Count heading level
            level = 0
            for char in line:
                if char == '#':
                    level += 1
                else:
                    break
            
            # Extract title
            title = line[level:].strip()
            
            # Create anchor
            anchor = title.lower().replace(' ', '-').replace('/', '-')
            anchor = ''.join(c for c in anchor if c.isalnum() or c == '-')
            
            toc.append({
                'level': level,
                'title': title,
                'anchor': anchor
            })
    
    return toc
