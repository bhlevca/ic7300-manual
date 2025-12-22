"""
IC-7300 Interactive Manual
Main Streamlit Application

A comprehensive, interactive guide to the ICOM IC-7300 HF/50MHz transceiver.
"""

import streamlit as st
from pathlib import Path
import markdown
from components.navigation import render_sidebar, get_chapter_list
from components.search import search_content
from components.interactive import render_interactive_panel
from components.wizards import render_wizard

# Page configuration
st.set_page_config(
    page_title="IC-7300 Interactive Manual",
    page_icon="📻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E88E5;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .info-box {
        background-color: #E3F2FD;
        border-left: 4px solid #1E88E5;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 4px 4px 0;
    }
    .warning-box {
        background-color: #FFF3E0;
        border-left: 4px solid #FF9800;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 4px 4px 0;
    }
    .tip-box {
        background-color: #E8F5E9;
        border-left: 4px solid #4CAF50;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 4px 4px 0;
    }
    .step-number {
        display: inline-block;
        width: 30px;
        height: 30px;
        background-color: #1E88E5;
        color: white;
        border-radius: 50%;
        text-align: center;
        line-height: 30px;
        margin-right: 10px;
        font-weight: bold;
    }
    .button-reference {
        font-family: monospace;
        background-color: #f0f0f0;
        padding: 2px 6px;
        border-radius: 3px;
        border: 1px solid #ccc;
    }
    .frequency-display {
        font-family: 'Courier New', monospace;
        font-size: 1.5rem;
        background-color: #000;
        color: #0f0;
        padding: 0.5rem 1rem;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)


def load_chapter_content(chapter_file: str) -> str:
    """Load markdown content from a chapter file."""
    chapter_path = Path(__file__).parent / "content" / "chapters" / chapter_file
    if chapter_path.exists():
        return chapter_path.read_text(encoding='utf-8')
    return f"# Content Coming Soon\n\nThis chapter is under development."


def render_home():
    """Render the home page."""
    st.markdown('<p class="main-header">📻 IC-7300 Interactive Manual</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your comprehensive guide to mastering the ICOM IC-7300</p>', unsafe_allow_html=True)
    
    # Welcome section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Welcome to the **IC-7300 Interactive Manual**! This guide is designed specifically 
        for beginners, providing step-by-step instructions for every function of your 
        IC-7300 transceiver.
        
        ### What You'll Learn
        
        - **Hardware Orientation**: Understanding every button, knob, and connection
        - **Basic Operations**: From power-on to making your first QSO
        - **Spectrum Scope**: Mastering the waterfall display
        - **Antenna & SWR**: Using the built-in tuner and understanding SWR
        - **Digital Modes**: Setting up FT8, PSK31, and more
        - **Software Setup**: Windows and Linux configuration guides
        
        ### Getting Started
        
        Use the **sidebar navigation** to explore different topics, or try the 
        **search function** to find specific information quickly.
        """)
        
        st.markdown('<div class="tip-box"><strong>💡 Tip:</strong> New to ham radio? Start with the "Introduction" chapter for an overview of the IC-7300\'s features.</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Quick Links")
        if st.button("🎛️ Front Panel Guide", use_container_width=True):
            st.session_state.current_chapter = "02_front_panel.md"
            st.rerun()
        if st.button("📡 Antenna & SWR", use_container_width=True):
            st.session_state.current_chapter = "06_antenna_swr.md"
            st.rerun()
        if st.button("💻 Digital Modes Setup", use_container_width=True):
            st.session_state.current_chapter = "07_digital_modes.md"
            st.rerun()
        if st.button("📶 WSJT-X / FT8 Guide", use_container_width=True):
            st.session_state.current_chapter = "08_wsjt_ft8.md"
            st.rerun()
    
    st.divider()
    
    # Feature highlights
    st.markdown("### 🌟 Key Features of This Manual")
    
    feat_col1, feat_col2, feat_col3 = st.columns(3)
    
    with feat_col1:
        st.markdown("""
        #### 🖱️ Interactive Diagrams
        Click on any button or control to see its function and usage instructions.
        """)
    
    with feat_col2:
        st.markdown("""
        #### 📋 Step-by-Step Wizards
        Follow guided procedures with Next/Previous navigation for complex tasks.
        """)
    
    with feat_col3:
        st.markdown("""
        #### 📄 Export to PDF/Word
        Generate printable documentation to keep near your radio.
        """)


def render_chapter(chapter_file: str):
    """Render a specific chapter."""
    content = load_chapter_content(chapter_file)
    
    # Convert markdown to HTML and display
    html_content = markdown.markdown(
        content, 
        extensions=['tables', 'fenced_code', 'toc', 'attr_list']
    )
    
    st.markdown(content)


def main():
    """Main application entry point."""
    # Initialize session state
    if 'current_chapter' not in st.session_state:
        st.session_state.current_chapter = None
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False
    if 'search_query' not in st.session_state:
        st.session_state.search_query = ""
    
    # Render sidebar navigation
    with st.sidebar:
        st.image("https://www.icomamerica.com/lineup/products/IC-7300/images/IC-7300_main.png", 
                 use_container_width=True)
        st.markdown("---")
        
        # Search box
        search_query = st.text_input("🔍 Search manual...", key="search_input")
        if search_query:
            st.session_state.search_query = search_query
        
        st.markdown("---")
        
        # Navigation menu
        st.markdown("### 📖 Chapters")
        
        chapters = [
            ("🏠 Home", None),
            ("📘 Introduction", "01_introduction.md"),
            ("🎛️ Front Panel", "02_front_panel.md"),
            ("🔌 Rear Panel", "03_rear_panel.md"),
            ("⚙️ Basic Operations", "04_basic_operations.md"),
            ("📊 Spectrum Scope", "05_spectrum_scope.md"),
            ("📡 Antenna & SWR", "06_antenna_swr.md"),
            ("💻 Digital Modes Overview", "07_digital_modes.md"),
            ("📶 WSJT-X / FT8", "08_wsjt_ft8.md"),
            ("🔧 Fldigi Setup", "09_fldigi_setup.md"),
            ("📨 JS8Call", "10_js8call.md"),
            ("🛠️ Troubleshooting", "11_troubleshooting.md"),
        ]
        
        for label, chapter_file in chapters:
            if st.button(label, key=f"nav_{chapter_file}", use_container_width=True):
                st.session_state.current_chapter = chapter_file
                st.rerun()
        
        st.markdown("---")
        
        # Quick reference section
        st.markdown("### 📋 Quick Reference")
        quick_refs = [
            ("⌨️ Button Shortcuts", "button_shortcuts.md"),
            ("📑 Menu Tree", "menu_tree.md"),
            ("📻 Band Frequencies", "band_frequencies.md"),
        ]
        
        for label, ref_file in quick_refs:
            if st.button(label, key=f"ref_{ref_file}", use_container_width=True):
                st.session_state.current_chapter = f"quick_refs/{ref_file}"
                st.rerun()
        
        st.markdown("---")
        
        # Export options
        st.markdown("### 📤 Export")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📄 PDF", use_container_width=True):
                st.info("PDF export - Coming soon!")
        with col2:
            if st.button("📝 Word", use_container_width=True):
                st.info("Word export - Coming soon!")
        
        st.markdown("---")
        
        # Settings
        st.markdown("### ⚙️ Settings")
        dark_mode = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode)
        if dark_mode != st.session_state.dark_mode:
            st.session_state.dark_mode = dark_mode
            st.rerun()
    
    # Main content area
    if st.session_state.search_query:
        st.markdown(f"### 🔍 Search Results for: *{st.session_state.search_query}*")
        results = search_content(st.session_state.search_query)
        if results:
            for result in results:
                with st.expander(f"📄 {result['title']}"):
                    st.markdown(result['excerpt'])
                    if st.button(f"Go to {result['title']}", key=f"goto_{result['file']}"):
                        st.session_state.current_chapter = result['file']
                        st.session_state.search_query = ""
                        st.rerun()
        else:
            st.info("No results found. Try different keywords.")
        
        if st.button("Clear Search"):
            st.session_state.search_query = ""
            st.rerun()
    
    elif st.session_state.current_chapter is None:
        render_home()
    else:
        render_chapter(st.session_state.current_chapter)
        
        # Navigation buttons at bottom
        st.divider()
        chapters = get_chapter_list()
        current_idx = next(
            (i for i, c in enumerate(chapters) if c['file'] == st.session_state.current_chapter), 
            -1
        )
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if current_idx > 0:
                if st.button("⬅️ Previous", use_container_width=True):
                    st.session_state.current_chapter = chapters[current_idx - 1]['file']
                    st.rerun()
        
        with col2:
            if st.button("🏠 Back to Home", use_container_width=True):
                st.session_state.current_chapter = None
                st.rerun()
        
        with col3:
            if current_idx < len(chapters) - 1:
                if st.button("Next ➡️", use_container_width=True):
                    st.session_state.current_chapter = chapters[current_idx + 1]['file']
                    st.rerun()


if __name__ == "__main__":
    main()
