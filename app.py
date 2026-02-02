"""
IC-7300 Interactive Manual
Main Streamlit Application

A comprehensive, interactive guide to the ICOM IC-7300 HF/50MHz transceiver.
"""

import base64
from pathlib import Path

import streamlit as st

from components.interactive import FRONT_PANEL_CONTROLS, REAR_PANEL_CONNECTIONS
from components.navigation import get_chapter_list, get_chapters_by_section, get_quick_refs
from components.search import search_content
from components.wizards import WIZARDS

# Page configuration
st.set_page_config(
    page_title="IC-7300 Interactive Manual",
    page_icon="📻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown(
    """
<style>
    /* Main header styling */
    .main-header {
        font-size: 2.2rem;
        font-weight: bold;
        color: #1E88E5;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 1.5rem;
    }
    
    /* Info boxes */
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
    .experience-box {
        background-color: #F3E5F5;
        border-left: 4px solid #9C27B0;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 4px 4px 0;
    }
    
    /* Chapter content styling */
    .chapter-content {
        line-height: 1.8;
        font-size: 1.05rem;
    }
    
    /* Cross-reference links */
    .cross-ref {
        color: #1E88E5;
        text-decoration: none;
        border-bottom: 1px dotted #1E88E5;
    }
    .cross-ref:hover {
        color: #0D47A1;
        border-bottom: 1px solid #0D47A1;
    }
    
    /* Image captions */
    .img-caption {
        text-align: center;
        font-style: italic;
        color: #666;
        margin-top: 0.5rem;
        font-size: 0.9rem;
    }
    
    /* Control reference cards */
    .control-card {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] > div {
        padding-top: 1rem;
    }
    
    /* Make images responsive */
    img {
        max-width: 100%;
        height: auto;
    }
</style>
""",
    unsafe_allow_html=True,
)


def get_image_path(image_name: str) -> Path:
    """Get the relative path to an image file for Streamlit display."""
    # Streamlit expects path relative to the working directory
    return Path("content") / "images" / image_name


def load_image_base64(image_name: str) -> str:
    """Load an image and return as base64 string for embedding."""
    image_path = get_image_path(image_name)
    if image_path.exists():
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""


def display_image(image_name: str, caption: str = "", width: int = None):
    """Display an image with optional caption."""
    image_path = get_image_path(image_name)
    if image_path.exists():
        try:
            # Read as bytes and hand to Streamlit (this avoids path issues)
            with open(image_path, "rb") as f:
                img_bytes = f.read()
            if width:
                st.image(img_bytes, caption=caption, width=width)
            else:
                # Let Streamlit choose natural sizing when width not specified
                st.image(img_bytes, caption=caption)
        except Exception as e:
            st.error(f"Failed to load image `{image_name}`: {e}")
    else:
        st.warning(f"Image not found: {image_name}")


def load_chapter_content(chapter_file: str) -> str:
    """Load markdown content from a chapter file."""
    if chapter_file.startswith("quick_refs/"):
        chapter_path = Path(__file__).parent / "content" / chapter_file
    else:
        chapter_path = Path(__file__).parent / "content" / "chapters" / chapter_file

    if chapter_path.exists():
        return chapter_path.read_text(encoding="utf-8")
    return f"# Content Coming Soon\n\nThe chapter `{chapter_file}` is under development."


def navigate_to_chapter(chapter_file: str, chapter_title: str):
    """Navigate to a specific chapter."""
    st.session_state.current_page = "chapter"
    st.session_state.current_chapter = chapter_file
    st.session_state.current_chapter_title = chapter_title


def render_home_page():
    """Render the home/welcome page."""
    # Logo and header
    col_logo, col_title = st.columns([1, 4])
    with col_logo:
        display_image("IC7300_logo.png", width=150)
    with col_title:
        st.markdown('<p class="main-header">IC-7300 Interactive Manual</p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="sub-header">Your comprehensive guide to mastering the ICOM IC-7300 HF/50MHz Transceiver</p>',
            unsafe_allow_html=True,
        )

    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            """
        Welcome to the **IC-7300 Interactive Manual**! This guide provides practical, 
        experience-based instructions going beyond the official manual with real-world 
        operating tips and techniques.
        
        ### 📚 What's Inside
        
        **🔧 Device Description**
        - Front and rear panel controls with detailed diagrams
        - Touch screen and menu navigation
        - Installation and connections guide
        
        **📻 Operations**
        - Basic operations and first QSO
        - Receiving and transmitting techniques
        - Spectrum scope mastery
        - Antenna tuning and SWR management
        
        **💻 Digital Modes**
        - Computer interface setup (USB, CI-V, ACC)
        - FT8, PSK31, RTTY configuration
        - Troubleshooting digital connections
        
        **📖 Reference**
        - Troubleshooting common issues
        - Glossary of ham radio terms
        - Quick reference cards
        
        ---
        
        ### 🚀 Getting Started
        
        **New to the IC-7300?** Browse the chapters using the navigation panel on the left.
        Each chapter includes:
        - Detailed explanations with diagrams
        - Cross-references to related topics (Wikipedia-style links)
        - **Real-life experience** sections with practical tips
        """
        )

    with col2:
        st.markdown("### 📊 Key Specifications")
        st.markdown(
            """
        | Spec | Value |
        |------|-------|
        | **Frequency** | 1.8-54 MHz |
        | **Power** | 2W - 100W |
        | **Modes** | SSB/CW/RTTY/AM/FM |
        | **Display** | 4.3" Touch LCD |
        | **Sampling** | Direct RF |
        | **Antenna** | 50Ω SO-239 |
        | **Power Req** | 13.8V DC, 23A |
        """
        )

        st.markdown("---")
        st.markdown("### ⚡ Quick Start Checklist")
        st.markdown(
            """
        1. ✅ Connect 13.8V DC power
        2. ✅ Connect 50Ω antenna
        3. ✅ Ground the radio
        4. ✅ Hold POWER for 1 second
        5. ✅ Tune antenna (hold TUNER)
        6. ✅ Select band and mode
        7. ✅ Make your first QSO!
        """
        )


def render_chapter_content(chapter_file: str, chapter_title: str):
    """Render full chapter content in the main area."""
    content = load_chapter_content(chapter_file)

    # Render the full markdown content
    st.markdown(content)

    # If this is a device/interactive chapter, render its images and controls inline
    if chapter_file == "02_front_panel.md":
        st.markdown("---")
        st.markdown("### Interactive: Front Panel Visuals")
        render_front_panel_page()
    elif chapter_file == "03_rear_panel.md":
        st.markdown("---")
        st.markdown("### Interactive: Rear Panel Visuals")
        render_rear_panel_page()
    elif chapter_file == "09_touchscreen_menus.md":
        st.markdown("---")
        st.markdown("### Interactive: Touch Screen and Menus")
        render_touch_menu_page()

    # Real-life experience expander at the bottom
    with st.expander("💡 Real-Life Experience & Tips", expanded=False):
        render_experience_tips(chapter_file)

    # Add navigation at the bottom
    st.markdown("---")
    chapters = get_chapter_list()

    # Find current chapter index
    current_idx = None
    for i, ch in enumerate(chapters):
        if ch["file"] == chapter_file:
            current_idx = i
            break

    if current_idx is not None:
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            if current_idx > 0:
                prev_ch = chapters[current_idx - 1]
                if st.button(f"⬅️ {prev_ch['title']}", key="prev_chapter", use_container_width=True):
                    navigate_to_chapter(prev_ch["file"], prev_ch["title"])
                    st.rerun()

        with col2:
            if st.button("🏠 Home", key="nav_home_bottom", use_container_width=True):
                st.session_state.current_page = "home"
                st.rerun()

        with col3:
            if current_idx < len(chapters) - 1:
                next_ch = chapters[current_idx + 1]
                if st.button(f"{next_ch['title']} ➡️", key="next_chapter", use_container_width=True):
                    navigate_to_chapter(next_ch["file"], next_ch["title"])
                    st.rerun()


def render_experience_tips(chapter_file: str):
    """Render real-life experience tips based on the chapter."""
    tips = {
        "01_introduction.md": """
**Why I love the IC-7300:**
- The real-time spectrum scope is a game changer for finding activity on a band
- Direct sampling means incredibly clean receive audio compared to older radios
- The touch screen makes menu navigation much faster than button-based radios

**First week tips:**
- Spend time just listening and watching the waterfall - you'll learn band characteristics
- Don't be afraid to touch the screen - it's very intuitive
- Save your settings to SD card after initial setup!
        """,
        "02_front_panel.md": """
**Controls I use most:**
- The MULTI knob is your best friend - push it to see available functions
- AF/RF-SQL dual knob: I usually keep RF at max and adjust AF for volume
- The QUICK menu (hold QUICK button) gives fast access to common settings

**Pro tip:** 
- Customize your Function screen (F1-F5) with your most-used features
- Learn the long-press functions - TUNER held for 1 sec starts auto-tune
        """,
        "03_rear_panel.md": """
**Connection lessons learned:**
- Always use a good ground connection - it really reduces noise
- The USB port provides both CAT control AND audio - one cable for digital modes!
- Use the ACC socket for linear amplifier PTT, not USB (timing issues)

**Digital mode setup:**
- USB audio levels: start at 50% and adjust from there
- CI-V baud rate: 19200 works well, but 115200 is faster for logging
        """,
        "04_basic_operations.md": """
**My daily operating routine:**
1. Power on, check SWR on current frequency
2. Scan the waterfall to see band activity  
3. Touch an interesting signal to tune to it
4. Use the QUICK menu to adjust NR/NB if needed

**Voice operating tips:**
- Keep ALC just barely moving - over-driving sounds terrible
- Use the Monitor function to hear yourself (helps with mic technique)
        """,
        "05_station_setup.md": """
**Power supply matters:**
- Get a supply rated for at least 25A continuous
- Voltage should be 13.8V ±0.5V under load
- Switching supplies are fine if well-filtered

**Grounding:**
- Run a thick (#10 or better) ground wire to a ground rod
- Multiple grounds? Bond them together to prevent ground loops
        """,
    }

    if chapter_file in tips:
        st.markdown(tips[chapter_file])
    else:
        st.markdown(
            """
**General Tips:**
- Take your time learning each feature before moving on
- Experiment with settings - you can always reset to defaults
- Join online communities (QRZ.com forums, Reddit r/amateurradio) for more tips
- Keep a log of settings that work well for you
        """
        )


def render_front_panel_page():
    """Render the interactive front panel page with actual images."""
    st.markdown("## 🎛️ Front Panel Reference")
    st.markdown(
        """The IC-7300 front panel provides intuitive access to all major functions. 
        The large touch screen and well-placed controls make operation smooth and efficient."""
    )

    # Display front panel images
    st.markdown("### Front Panel Overview (Controls 1-19)")
    display_image("FrontPanel_1-19.png", "Front Panel - Left Section (Controls 1-19)")

    st.markdown("### Front Panel Overview (Controls 20-34)")
    display_image("FrontPanel_20-34.png", "Front Panel - Right Section (Controls 20-34)")

    st.markdown("---")

    # Touch screen display
    st.markdown("---")
    st.markdown(
        '**For touch screen details and menu screenshots, see the "Touch Screen & Menus" chapter. (Use the sidebar or the interactive navigation button.)**'
    )
    st.markdown("---")

    st.markdown("---")

    # Control Details with expanders
    st.markdown("### Control Details")

    control_groups = {
        "🔴 Power & Transmit (1-4)": {
            "1. POWER": "Hold for 1 second to turn ON/OFF. The radio remembers its last state.",
            "2. TRANSMIT": "Push to toggle TX/RX. LED lights red when transmitting.",
            "3. VOX/BK-IN": "Toggle voice-activated TX. In CW mode, enables break-in.",
            "4. TUNER": "Tap to enable/bypass tuner. HOLD for 1 sec to start auto-tune.",
        },
        "🔊 Audio & Squelch (5-6)": {
            "5. PHONES Jack": "3.5mm stereo headphone jack. Disables internal speaker when used.",
            "6. AF/RF-SQL": "Dual concentric knob. Outer: AF volume. Inner: RF gain (push to toggle SQL).",
        },
        "🎤 Microphone (7)": {
            "7. MIC Connector": "8-pin connector for HM-219 or compatible microphone. Provides PTT, UP/DOWN, and audio.",
        },
        "📱 Navigation (8-18)": {
            "8. MENU": "Opens the main menu screen for radio configuration.",
            "9. EXIT": "Returns to previous screen or closes current menu.",
            "10. FUNCTION": "Cycles through customizable function screens (F1-F5).",
            "11-14. Mode Keys": "SSB (tap for USB/LSB), CW, RTTY, AM, FM mode selection.",
            "15. MULTI": "Push to show adjustable parameters, turn to adjust.",
            "16. M.SCOPE": "Spectrum scope display options.",
            "17-18. SPEECH/SCAN": "Voice announcement and scan functions.",
        },
        "🎚️ Main Controls (30-34)": {
            "30. MAIN DIAL": "Tunes frequency. Push for fine tuning options.",
            "31-34. VFO/Memory": "VFO A/B, memory channels, split operation.",
        },
    }

    for group_name, controls in control_groups.items():
        with st.expander(group_name, expanded=False):
            for ctrl, desc in controls.items():
                st.markdown(f"**{ctrl}**")
                st.markdown(desc)
                st.markdown("---")

    # Real-life experience
    with st.expander("💡 Real-Life Experience & Tips", expanded=False):
        render_experience_tips("02_front_panel.md")


def render_rear_panel_page():
    """Render the interactive rear panel page with actual images."""
    st.markdown("## 🔌 Rear Panel Connections")
    st.markdown(
        """The rear panel provides all connections for antenna, power, and accessories.
        **⚠️ Always power off before making or changing connections.**"""
    )

    # Display rear panel images
    st.markdown("### Rear Panel Overview")
    display_image("RearPanel.png", "Rear Panel - All Connections")

    st.markdown("### Connection Diagram")
    display_image("RearPanel_connections.png", "Rear Panel Connection Points")

    st.markdown("---")

    # Connection diagrams
    st.markdown("### Connection Diagrams")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### External DC Power")
        display_image("Connecting_external_DC_power.png", "DC Power Connection (13.8V, 23A max)")

        st.markdown("#### Antenna Tuner Connection")
        display_image("Connecting_antenna_tuner.png", "External Antenna Tuner")

    with col2:
        st.markdown("#### ICOM Linear Amplifier")
        display_image("Connecting_ICOM_linear_apmlifier.png", "ICOM Linear Amplifier (IC-PW2)")

        st.markdown("#### Non-ICOM Linear Amplifier")
        display_image("Connecting_nonICOM_linear_amplifier.png", "Generic Linear Amplifier")

    st.markdown("---")

    st.markdown("### Digital Mode Connections")
    col1, col2 = st.columns(2)
    with col1:
        display_image("FSK&AFSK_connections.png", "FSK & AFSK Digital Mode Connections")
    with col2:
        display_image(
            "Using_ACC_or_microphone_connector.png", "ACC Socket & Microphone Connector Pinouts"
        )

    st.markdown("---")

    # Connection details
    st.markdown("### Connection Details")

    connections = {
        "📡 ANT (Antenna)": {
            "Type": "SO-239 (accepts PL-259)",
            "Impedance": "50Ω unbalanced",
            "Power": "Up to 100W",
            "Notes": "Never transmit without antenna connected. Use good quality coax (RG-8, LMR-400).",
        },
        "⚡ DC Power": {
            "Voltage": "13.8V DC ±15%",
            "Current": "23A max (transmit), 2A (receive)",
            "Connector": "2-pin, center positive",
            "Notes": "Use heavy gauge wire (#10 or better). Include inline fuse.",
        },
        "🔌 USB Port": {
            "Type": "USB Type B",
            "Functions": "CAT control (CI-V) + Audio (in/out)",
            "Driver": "Silicon Labs CP210x (auto-installs on most OS)",
            "Notes": "One cable for logging, CAT, and digital modes!",
        },
        "🔗 ACC Socket": {
            "Type": "13-pin DIN",
            "Functions": "Audio I/O, PTT, ALC, squelch out",
            "Notes": "Best for external TNC, linear amp PTT, or audio interfaces.",
        },
        "🌍 GND Terminal": {
            "Type": "Screw terminal (M4)",
            "Notes": "Connect to station ground. Essential for RFI reduction.",
        },
        "🎹 KEY Jack": {
            "Type": "3.5mm stereo (TRS)",
            "Functions": "Straight key or paddle",
            "Notes": "Configure key type in MENU > KEYER.",
        },
    }

    for conn_name, details in connections.items():
        with st.expander(conn_name, expanded=False):
            for key, value in details.items():
                st.markdown(f"**{key}:** {value}")

    # Safety warning
    st.markdown(
        """
        <div class="warning-box">
        <strong>⚠️ Safety Warnings:</strong><br>
        • Always power off before connecting/disconnecting cables<br>
        • Never transmit without an antenna or dummy load connected<br>
        • Verify DC polarity before connecting power (center positive)<br>
        • Use appropriate wire gauge for power connections (#10 AWG or heavier)
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Real-life experience
    with st.expander("💡 Real-Life Experience & Tips", expanded=False):
        render_experience_tips("03_rear_panel.md")


def render_touch_menu_page():
    """Render the touch screen and menus page."""
    st.markdown("## 📱 Touch Screen & Menu System")
    st.markdown(
        """The IC-7300's touch screen is central to its operation. 
        Master it to unlock the radio's full potential."""
    )

    # Touch menu image
    display_image("Touch_menu.png", "Touch Screen Menu Overview")

    st.markdown("---")

    # Touch screen display areas (overview only)
    st.markdown("### Touch Screen Display Areas")
    st.markdown(
        "Only the overview image is shown here. Detailed touch-area diagrams and function/menu screenshots are available in the 'Touch Display (1–29)' expander below."
    )

    st.markdown("---")

    # Function and Menu screens (overview only)
    st.markdown("### Function and Menu Screens")
    st.markdown(
        "See the 'Touch Display (1–29)' expander for full screenshots and descriptions of function/menu screens."
    )

    st.markdown("---")

    # Multi-function menus (overview)
    st.markdown("### Multi-Function Menu Items")
    st.markdown("Detailed multi-function menu graphics are included in the expander below.")

    st.markdown("---")

    with st.expander("🖥️ Touch Display (1–29)", expanded=False):
        st.markdown(
            "**Overview:** The touchscreen displays and touch-sensitive areas provide direct control over tuning, mode selection, filters, and the spectrum scope. Below is a concise description of the grouped touch areas so you can match them to the diagrams in this chapter."
        )
        st.markdown("### Touch Areas 1–15 (Primary Display Regions)")
        st.markdown(
            """
1. **Frequency Readout & Keypad** — Direct frequency entry and quick band selection.
2. **Mode Indicator** — Shows current mode (SSB/CW/RTTY/FM/AM) and submode.
3. **S-Meter / Power Meter** — Receive signal strength and transmit power/ALC readings.
4. **Filter Display** — Current filter selection and passband edges.
5. **Spectrum Scope (upper)** — Real-time signal peaks for the selected span.
6. **Waterfall (lower)** — Historical signal activity over time.
7. **Virtual Softkeys / Function Area** — Context-sensitive buttons (F1–F5) and quick actions.
8. **Quick Menu / Status Icons** — Shortcuts for commonly used features (NR, NB, COMP).
9. **AGC/NR/NOTCH Indicators** — DSP processing states and levels.
10. **TUNE / TUNER Indicator** — Tuner status and auto-tune activation.
11. **RIT / XIT Display** — Receive/transmit offset readouts.
12. **Split / Memory Indicators** — Shows split operation and memory channel info.
13. **Microphone / USB Audio Status** — Input selection and levels for digital modes.
14. **Squelch / AF Display** — Audio/squelch status indicators.
15. **Touch Tuning Area** — Tap to jump to signals shown in the scope/waterfall.
"""
        )

        st.markdown("### Touch Areas 16–29 (Secondary Controls & Menus)")
        st.markdown(
            """
16. **Function Menus** — Additional function pages and options.
17. **Multi-function Knob Context** — Displays current parameter controlled by the MULTI knob.
18. **Menu Navigation** — Scrollable lists and menu selection panels.
19. **Band Edge / Frequency Grid** — Shows numeric markers and grid lines.
20. **Display Brightness / Contrast Controls** — Quick adjustments for visibility.
21. **Recorder / Playback Controls** — Voice memos and screen capture controls.
22. **Connectivity Status** — USB/CI‑V/ACC connection indicators.
23. **Keyer / CW Settings** — CW keyer controls and sidetone settings.
24. **Digital Mode Helpers** — Gateways for FT8/RTTY soft links and audio routing.
25. **Scope Span & Zoom Controls** — Adjust scope span and magnification.
26. **Waterfall Speed & Color** — Change scrolling speed and color scheme.
27. **Grid & Marker Options** — Toggle markers and reference lines.
28. **Band Plan Notes** — Quick reference overlays where available.
29. **Help / Info** — Context-sensitive help and brief descriptions.
"""
        )

        st.markdown("---")

        # Diagrams & screenshots
        st.markdown("### Diagrams & Screenshots")
        cols = st.columns(2)
        with cols[0]:
            display_image("TouchPanel_display_1-15.png", "Touch Panel: Display areas 1-15")
        with cols[1]:
            display_image("TouchPanel_display_16-29.png", "Touch Panel: Display areas 16-29")

        st.markdown("---")
        cols = st.columns(2)
        with cols[0]:
            display_image("Functionscreen.png", "Function Screen (press FUNCTION button)")
        with cols[1]:
            display_image("MenuScreen.png", "Menu Screen (press MENU button)")

        st.markdown("---")
        display_image("MultiFunction_menus.png", "Multi-function knob menu options vary by mode")
        display_image("DisplayType_menu.png", "Display Type Configuration (MENU > SET > Display)")

        st.markdown("---")

    st.markdown("---")

    st.markdown(
        """
    ### Touch Screen Tips
    
    **Quick Frequency Entry:**
    - Touch the frequency display to open the keypad
    - Enter frequency in kHz (e.g., 14074 for 14.074 MHz)
    - Touch [ENT] to confirm
    
    **Spectrum Scope Tuning:**
    - Single touch: Magnifies the area around that frequency
    - Double touch: Tunes directly to that frequency
    - Touch and drag: Pan across the band
    
    **Menu Navigation:**
    - Swipe up/down to scroll through menu items
    - Touch item to select, touch again to adjust
    - Use BACK arrow or EXIT button to go up one level
    
    ### Essential Menu Locations
    
    | Setting | Location |
    |---------|----------|
    | USB Audio Level | MENU > SET > Connectors > USB MOD Level |
    | CI-V Settings | MENU > SET > Connectors > CI-V |
    | Display Brightness | MENU > SET > Display > LCD Brightness |
    | CW Settings | MENU > SET > Function > CW-KEY SET |
    | AGC Settings | MENU > SET > Function > AGC |
    | Filter Settings | Touch the filter display on main screen |
    """
    )

    with st.expander("💡 Real-Life Experience & Tips", expanded=False):
        st.markdown(
            """
**Touch screen techniques I use daily:**

1. **Quick band change**: Touch the MHz digits, type new frequency, ENT
2. **Fine tuning**: Touch the waterfall near a signal, then use main dial
3. **Quick filter adjust**: Touch the filter width display, drag to adjust
4. **Split operation**: Touch SPLIT, touch VFO B, set TX freq, touch back

**Menu shortcuts:**
- The QUICK button gives access to commonly-adjusted settings
- Customize your QUICK menu in MENU > SET > Function > QUICK MENU

**Hidden features:**
- Long-press on some screen items reveals additional options
- Touch and hold the S-meter to change meter display type
        """
        )


def render_wizard_page():
    """Render step-by-step wizard page."""
    st.markdown("## 🧙 Step-by-Step Wizards")

    wizard_list = [
        ("first_power_on", "🔌 First Power On", "Initial setup procedure"),
        ("tune_antenna", "📡 Antenna Tuning", "Using the built-in tuner"),
        ("setup_ft8", "💻 FT8 Setup", "Configure for FT8 digital mode"),
        ("change_band", "📻 Change Bands", "How to switch bands"),
    ]

    wizard_id = st.session_state.get("selected_wizard", None)

    if wizard_id is None:
        st.markdown("Select a wizard to get step-by-step guidance:")

        cols = st.columns(2)
        for i, (wid, name, desc) in enumerate(wizard_list):
            with cols[i % 2]:
                if st.button(f"{name}\n*{desc}*", key=f"wiz_{wid}", use_container_width=True):
                    st.session_state.selected_wizard = wid
                    st.session_state.wizard_step = 0
                    st.rerun()
    else:
        if wizard_id in WIZARDS:
            wizard = WIZARDS[wizard_id]
            step_idx = st.session_state.get("wizard_step", 0)
            total_steps = len(wizard["steps"])

            st.markdown(f"### {wizard['title']}")
            st.progress((step_idx + 1) / total_steps, text=f"Step {step_idx + 1} of {total_steps}")

            step = wizard["steps"][step_idx]
            st.markdown(f"## Step {step_idx + 1}: {step['title']}")
            st.markdown(step["content"])

            st.markdown("---")
            col1, col2, col3 = st.columns(3)

            with col1:
                if step_idx > 0:
                    if st.button("⬅️ Previous", use_container_width=True):
                        st.session_state.wizard_step = step_idx - 1
                        st.rerun()

            with col2:
                if st.button("❌ Exit Wizard", use_container_width=True):
                    st.session_state.selected_wizard = None
                    st.session_state.wizard_step = 0
                    st.rerun()

            with col3:
                if step_idx < total_steps - 1:
                    if st.button("Next ➡️", use_container_width=True):
                        st.session_state.wizard_step = step_idx + 1
                        st.rerun()
                else:
                    if st.button("✅ Complete!", use_container_width=True):
                        st.balloons()
                        st.session_state.selected_wizard = None
                        st.session_state.wizard_step = 0
        else:
            st.warning("Wizard not found")
            st.session_state.selected_wizard = None


def render_search_results():
    """Render search results with working navigation buttons."""
    query = st.session_state.get("search_query", "")

    if not query:
        st.session_state.current_page = "home"
        st.rerun()
        return

    st.markdown(f"### 🔍 Search Results for: *{query}*")

    results = search_content(query)

    if results:
        st.success(f"Found {len(results)} results")

        for i, result in enumerate(results):
            with st.expander(f"📄 {result['title']}", expanded=True):
                st.markdown(result["excerpt"])

                # Find the chapter file for this result
                chapters = get_chapter_list()
                chapter_file = None
                for ch in chapters:
                    if ch["title"] == result["title"] or result.get("file") == ch["file"]:
                        chapter_file = ch["file"]
                        break

                if chapter_file:
                    if st.button(f"📖 Open: {result['title']}", key=f"search_open_{i}"):
                        # Clear search and navigate
                        st.session_state.search_query = ""
                        st.session_state.current_page = "chapter"
                        st.session_state.current_chapter = chapter_file
                        st.session_state.current_chapter_title = result["title"]
                        st.rerun()
    else:
        st.warning("No results found. Try different keywords.")
        st.markdown(
            """
        **Search tips:**
        - Use simple keywords like "antenna", "USB", "FT8"
        - Try related terms if your first search doesn't find what you need
        - Browse chapters in the sidebar for a complete overview
        """
        )

    st.markdown("---")
    if st.button("🏠 Return to Home", key="search_home", use_container_width=True):
        st.session_state.search_query = ""
        st.session_state.current_page = "home"
        st.rerun()


def main():
    """Main application entry point."""
    # Initialize session state with defaults
    if "current_page" not in st.session_state:
        st.session_state.current_page = "home"
    if "current_chapter" not in st.session_state:
        st.session_state.current_chapter = None
    if "current_chapter_title" not in st.session_state:
        st.session_state.current_chapter_title = None
    if "search_query" not in st.session_state:
        st.session_state.search_query = ""

    # ==================== SIDEBAR ====================
    with st.sidebar:
        # Logo and title
        display_image("IC7300_logo.png", width=80)
        st.markdown("## IC-7300 Manual")
        st.markdown("---")

        # Home button - ALWAYS clears search
        if st.button("🏠 Home", key="sidebar_home", use_container_width=True):
            st.session_state.current_page = "home"
            st.session_state.search_query = ""  # Clear search!
            st.rerun()

        # Search with proper state management
        st.markdown("### 🔍 Search")

        def do_search():
            """Handle search submission."""
            if st.session_state.search_input_field:
                st.session_state.search_query = st.session_state.search_input_field
                st.session_state.current_page = "search"

        search_input = st.text_input(
            "Search manual...",
            placeholder="e.g., antenna, FT8, USB",
            key="search_input_field",
            on_change=do_search,
        )

        if st.button("🔍 Search", key="search_button", use_container_width=True):
            if search_input:
                st.session_state.search_query = search_input
                st.session_state.current_page = "search"
                st.rerun()

        st.markdown("---")

        # Chapter navigation by sections
        st.markdown("### 📖 Chapters")

        sections = get_chapters_by_section()
        section_icons = {
            "Getting Started": "🚀",
            "Device Description": "🔧",
            "Operation": "📻",
            "Digital": "💻",
            "Reference": "📚",
        }

        for section_name, section_chapters in sections.items():
            icon = section_icons.get(section_name, "📁")
            with st.expander(f"{icon} {section_name}", expanded=False):
                for chapter in section_chapters:
                    btn_label = f"{chapter['icon']} {chapter['title']}"
                    if st.button(btn_label, key=f"ch_{chapter['file']}", use_container_width=True):
                        st.session_state.current_page = "chapter"
                        st.session_state.current_chapter = chapter["file"]
                        st.session_state.current_chapter_title = chapter["title"]
                        st.session_state.search_query = ""  # Clear search!
                        st.rerun()

        st.markdown("---")

        # Special pages
        st.markdown("### 🎛️ Interactive")

        if st.button("🎛️ Front Panel Guide", key="nav_front", use_container_width=True):
            st.session_state.current_page = "front_panel"
            st.session_state.search_query = ""
            st.rerun()

        if st.button("🔌 Rear Panel Guide", key="nav_rear", use_container_width=True):
            st.session_state.current_page = "rear_panel"
            st.session_state.search_query = ""
            st.rerun()

        if st.button("📱 Touch Screen & Menus", key="nav_touch", use_container_width=True):
            st.session_state.current_page = "touch_menu"
            st.session_state.search_query = ""
            st.rerun()

        if st.button("🧙 Setup Wizards", key="nav_wizards", use_container_width=True):
            st.session_state.current_page = "wizards"
            st.session_state.search_query = ""
            st.rerun()

        st.markdown("---")

        # Quick references
        st.markdown("### 📋 Quick Reference")
        quick_refs = get_quick_refs()
        for ref in quick_refs:
            if st.button(
                f"{ref['icon']} {ref['title']}", key=f"qr_{ref['file']}", use_container_width=True
            ):
                st.session_state.current_page = "quick_ref"
                st.session_state.current_chapter = ref["file"]
                st.session_state.current_chapter_title = ref["title"]
                st.session_state.search_query = ""
                st.rerun()

        st.markdown("---")
        st.caption("v1.0 | [GitHub](https://github.com/bhlevca/ic7300-manual)")

    # ==================== MAIN CONTENT ====================

    # Get current page
    current_page = st.session_state.current_page

    # Handle search results page
    if current_page == "search" and st.session_state.search_query:
        render_search_results()
        return

    # Render based on current page
    if current_page == "home":
        render_home_page()

    elif current_page == "chapter":
        chapter_file = st.session_state.current_chapter
        chapter_title = st.session_state.current_chapter_title
        if chapter_file:
            render_chapter_content(chapter_file, chapter_title)
        else:
            render_home_page()

    elif current_page == "quick_ref":
        chapter_file = st.session_state.current_chapter
        chapter_title = st.session_state.current_chapter_title
        if chapter_file:
            st.markdown(f"## 📋 {chapter_title}")
            content = load_chapter_content(chapter_file)
            st.markdown(content)
        else:
            render_home_page()

    elif current_page == "front_panel":
        render_front_panel_page()

    elif current_page == "rear_panel":
        render_rear_panel_page()

    elif current_page == "touch_menu":
        render_touch_menu_page()

    elif current_page == "wizards":
        render_wizard_page()

    else:
        render_home_page()


if __name__ == "__main__":
    main()
