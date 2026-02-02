"""Basic tests for the IC-7300 Manual application."""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_imports():
    """Test that main modules can be imported."""
    from components.interactive import FRONT_PANEL_CONTROLS, REAR_PANEL_CONNECTIONS
    from components.navigation import get_chapter_list, get_quick_refs
    from components.search import search_content
    from components.wizards import WIZARDS

    assert callable(get_chapter_list)
    assert callable(get_quick_refs)
    assert callable(search_content)
    assert isinstance(FRONT_PANEL_CONTROLS, dict)
    assert isinstance(REAR_PANEL_CONNECTIONS, dict)
    assert isinstance(WIZARDS, dict)


def test_chapter_list():
    """Test that chapter list returns expected structure."""
    from components.navigation import get_chapter_list

    chapters = get_chapter_list()
    assert isinstance(chapters, list)
    assert len(chapters) > 0

    for chapter in chapters:
        assert "file" in chapter
        assert "title" in chapter
        assert "icon" in chapter


def test_quick_refs():
    """Test that quick refs returns expected structure."""
    from components.navigation import get_quick_refs

    refs = get_quick_refs()
    assert isinstance(refs, list)
    assert len(refs) > 0

    for ref in refs:
        assert "file" in ref
        assert "title" in ref
        assert "icon" in ref


def test_front_panel_controls():
    """Test that front panel controls have required fields."""
    from components.interactive import FRONT_PANEL_CONTROLS

    required_controls = ["power", "transmit", "main_dial", "touch_screen"]

    for ctrl_id in required_controls:
        assert ctrl_id in FRONT_PANEL_CONTROLS
        ctrl = FRONT_PANEL_CONTROLS[ctrl_id]
        assert "name" in ctrl
        assert "description" in ctrl


def test_rear_panel_connections():
    """Test that rear panel connections have required fields."""
    from components.interactive import REAR_PANEL_CONNECTIONS

    required_connections = ["antenna", "usb", "dc_power"]

    for conn_id in required_connections:
        assert conn_id in REAR_PANEL_CONNECTIONS
        conn = REAR_PANEL_CONNECTIONS[conn_id]
        assert "name" in conn
        assert "description" in conn


def test_wizards():
    """Test that wizards have required structure."""
    from components.wizards import WIZARDS

    assert "first_power_on" in WIZARDS
    assert "tune_antenna" in WIZARDS

    for wizard_id, wizard in WIZARDS.items():
        assert "title" in wizard
        assert "description" in wizard
        assert "steps" in wizard
        assert isinstance(wizard["steps"], list)
        assert len(wizard["steps"]) > 0

        for step in wizard["steps"]:
            assert "title" in step
            assert "content" in step


def test_search_content():
    """Test search functionality."""
    from components.search import search_content

    # Search for a term that should exist
    results = search_content("antenna")
    assert isinstance(results, list)

    # Each result should have required fields
    for result in results:
        assert "file" in result
        assert "title" in result
        assert "excerpt" in result


def test_content_files_exist():
    """Test that content files exist."""
    content_dir = Path(__file__).parent.parent / "content" / "chapters"

    assert content_dir.exists()

    md_files = list(content_dir.glob("*.md"))
    assert len(md_files) > 0


def test_quick_ref_files_exist():
    """Test that quick reference files exist."""
    quick_ref_dir = Path(__file__).parent.parent / "content" / "quick_refs"

    assert quick_ref_dir.exists()

    md_files = list(quick_ref_dir.glob("*.md"))
    assert len(md_files) > 0
