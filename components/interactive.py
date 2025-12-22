"""
Interactive Component
Handles clickable diagrams, tooltips, and interactive elements.
"""

import streamlit as st
from typing import Dict, List, Tuple, Optional


# Front panel control definitions with positions and descriptions
FRONT_PANEL_CONTROLS = {
    "power": {
        "name": "POWER",
        "position": (50, 60),
        "size": (30, 30),
        "description": "Turns the transceiver ON or OFF. Press and hold for 1 second to power on.",
        "tips": [
            "Green LED indicates power is ON",
            "The radio remembers your last settings when powered off"
        ]
    },
    "transmit": {
        "name": "TRANSMIT",
        "position": (50, 120),
        "size": (30, 30),
        "description": "Toggles between transmit and receive mode.",
        "tips": [
            "Also known as PTT (Push-to-Talk)",
            "LED turns red when transmitting"
        ]
    },
    "vox_bk_in": {
        "name": "VOX/BK-IN",
        "position": (50, 180),
        "size": (30, 30),
        "description": "Activates Voice Operated Transmit (VOX) or CW break-in function.",
        "tips": [
            "VOX allows hands-free transmission",
            "BK-IN is for semi or full break-in CW operation"
        ]
    },
    "tuner": {
        "name": "TUNER",
        "position": (50, 240),
        "size": (30, 30),
        "description": "Controls the internal automatic antenna tuner.",
        "tips": [
            "Press to enable/disable the tuner",
            "Hold for 1 second to start tuning",
            "TUNE icon appears on screen during tuning"
        ]
    },
    "phones": {
        "name": "PHONES",
        "position": (100, 350),
        "size": (25, 25),
        "description": "Connects standard stereo headphones (3.5mm jack).",
        "tips": [
            "Use headphones to reduce ambient noise",
            "Speaker is muted when headphones are connected"
        ]
    },
    "mic_connector": {
        "name": "MIC",
        "position": (140, 350),
        "size": (25, 25),
        "description": "8-pin modular connector for microphone.",
        "tips": [
            "Use HM-219 supplied microphone or compatible",
            "Supports UP/DOWN buttons for frequency control"
        ]
    },
    "af_rf_sql": {
        "name": "AF/RF-SQL",
        "position": (200, 80),
        "size": (50, 50),
        "description": "Dual-function knob: Inner ring adjusts AF volume, outer ring adjusts RF gain and squelch.",
        "tips": [
            "Inner (AF): Adjusts speaker/headphone volume",
            "Outer left: Adjusts RF gain (reduce for strong signals)",
            "Outer right: Adjusts squelch threshold"
        ]
    },
    "menu": {
        "name": "MENU",
        "position": (280, 100),
        "size": (30, 30),
        "description": "Opens the MENU screen for accessing all settings.",
        "tips": [
            "Main settings are organized in categories",
            "Use touch screen to navigate menus"
        ]
    },
    "function": {
        "name": "FUNCTION",
        "position": (280, 160),
        "size": (30, 30),
        "description": "Displays the FUNCTION screen with quick access controls.",
        "tips": [
            "Quick access to NB, NR, NOTCH, COMP",
            "Press repeatedly to toggle functions"
        ]
    },
    "scope": {
        "name": "SCOPE",
        "position": (280, 220),
        "size": (30, 30),
        "description": "Displays the spectrum scope and waterfall.",
        "tips": [
            "Toggle between Mini Scope and full Spectrum Scope",
            "Touch signals on waterfall to tune to them"
        ]
    },
    "quick": {
        "name": "QUICK",
        "position": (280, 280),
        "size": (30, 30),
        "description": "Opens the QUICK MENU for frequently used settings.",
        "tips": [
            "Context-sensitive based on current mode",
            "Faster than navigating through MENU"
        ]
    },
    "main_dial": {
        "name": "MAIN DIAL",
        "position": (700, 200),
        "size": (100, 100),
        "description": "Large tuning dial for changing frequency.",
        "tips": [
            "Rotation speed affects tuning rate",
            "Push to access MULTI function options",
            "Friction is adjustable underneath the knob"
        ]
    },
    "exit": {
        "name": "EXIT",
        "position": (420, 100),
        "size": (30, 30),
        "description": "Exits the current screen and returns to previous level.",
        "tips": [
            "Use to back out of menus",
            "Returns to main operating screen from any menu"
        ]
    },
    "multi": {
        "name": "MULTI",
        "position": (420, 160),
        "size": (40, 40),
        "description": "Multi-function encoder for various adjustments.",
        "tips": [
            "Push to display available options on screen",
            "Options vary by operating mode (SSB, CW, etc.)",
            "Adjusts RF power, CW speed, sidetone, etc."
        ]
    },
    "touch_screen": {
        "name": "TOUCH SCREEN",
        "position": (470, 100),
        "size": (250, 180),
        "description": "4.3-inch color TFT touch LCD display.",
        "tips": [
            "Touch to interact with on-screen controls",
            "Displays frequency, mode, S-meter, spectrum",
            "Clean with soft, dry cloth only"
        ]
    },
    "mode_keys": {
        "name": "MODE KEYS",
        "position": (320, 330),
        "size": (180, 30),
        "description": "Direct access buttons for operating modes: SSB, CW, RTTY, AM, FM.",
        "tips": [
            "Press repeatedly to toggle sub-modes (USB/LSB)",
            "Hold to access DATA mode variations"
        ]
    },
    "filter": {
        "name": "FILTER",
        "position": (520, 330),
        "size": (40, 30),
        "description": "Opens filter selection and adjustment screen.",
        "tips": [
            "FIL1 = Wide, FIL2 = Medium, FIL3 = Narrow",
            "Touch screen to adjust bandwidth precisely"
        ]
    },
}


# Rear panel connection definitions
REAR_PANEL_CONNECTIONS = {
    "antenna": {
        "name": "ANT (Antenna)",
        "position": (100, 150),
        "description": "50Ω SO-239 (PL-259) antenna connector.",
        "tips": [
            "Use quality coax cable (RG-213, LMR-400)",
            "Ensure connector is tight but not over-tightened",
            "SWR should be below 2:1 for safe operation"
        ]
    },
    "ground": {
        "name": "GND (Ground)",
        "position": (160, 150),
        "description": "Ground terminal for station ground connection.",
        "tips": [
            "Connect to station ground for safety",
            "Helps reduce RF interference"
        ]
    },
    "usb": {
        "name": "USB (Type B)",
        "position": (250, 150),
        "description": "USB port for computer connection (CAT control and audio).",
        "tips": [
            "Install ICOM USB driver before connecting",
            "Provides both CAT control and audio interface",
            "Single cable solution for digital modes"
        ]
    },
    "acc": {
        "name": "ACC Socket",
        "position": (350, 150),
        "description": "13-pin DIN accessory connector.",
        "tips": [
            "Connect to external TNC, linear amplifier, etc.",
            "Provides audio in/out and PTT control"
        ]
    },
    "key": {
        "name": "KEY Jack",
        "position": (400, 150),
        "description": "3.5mm key jack for CW paddle or straight key.",
        "tips": [
            "Supports paddle and straight key",
            "Configure in MENU > SET > CW settings"
        ]
    },
    "ext_sp": {
        "name": "EXT SP (External Speaker)",
        "position": (450, 150),
        "description": "3.5mm jack for external speaker.",
        "tips": [
            "Use 8Ω external speaker for best audio",
            "Internal speaker is disabled when connected"
        ]
    },
    "dc_power": {
        "name": "DC 13.8V",
        "position": (550, 150),
        "description": "DC power input (13.8V ±15%).",
        "tips": [
            "Use power supply rated for at least 23A",
            "Ensure correct polarity (center positive)",
            "Fused at 30A"
        ]
    },
    "remote": {
        "name": "REMOTE",
        "position": (300, 200),
        "description": "3.5mm CI-V remote control jack.",
        "tips": [
            "Alternative to USB for CAT control",
            "Connect CI-V cable for computer control"
        ]
    },
    "tuner_control": {
        "name": "TUNER",
        "position": (180, 200),
        "description": "Control port for optional AH-4/AH-2b antenna tuner.",
        "tips": [
            "Use for external antenna tuner control",
            "Required for automatic antenna tuner operation"
        ]
    }
}


def render_interactive_panel(panel_type: str = "front") -> Optional[Dict]:
    """
    Render an interactive panel diagram.
    
    Args:
        panel_type: Either 'front' or 'rear'.
        
    Returns:
        Selected control info if any control was clicked.
    """
    controls = FRONT_PANEL_CONTROLS if panel_type == "front" else REAR_PANEL_CONNECTIONS
    
    st.markdown(f"### Interactive {panel_type.title()} Panel")
    st.markdown("*Click on any control below for detailed information:*")
    
    # Create columns for controls
    cols = st.columns(4)
    
    selected = None
    for i, (key, control) in enumerate(controls.items()):
        col_idx = i % 4
        with cols[col_idx]:
            if st.button(
                f"🔘 {control['name']}", 
                key=f"ctrl_{key}",
                use_container_width=True
            ):
                selected = control
    
    # Display selected control info
    if selected:
        st.markdown("---")
        st.markdown(f"## {selected['name']}")
        st.markdown(selected['description'])
        
        if 'tips' in selected:
            st.markdown("### 💡 Tips")
            for tip in selected['tips']:
                st.markdown(f"- {tip}")
    
    return selected


def create_control_reference_table(panel_type: str = "front") -> str:
    """
    Create a markdown table of all controls.
    
    Args:
        panel_type: Either 'front' or 'rear'.
        
    Returns:
        Markdown table string.
    """
    controls = FRONT_PANEL_CONTROLS if panel_type == "front" else REAR_PANEL_CONNECTIONS
    
    table = "| Control | Description |\n|---------|-------------|\n"
    
    for key, control in controls.items():
        table += f"| **{control['name']}** | {control['description']} |\n"
    
    return table


def render_clickable_image(image_path: str, hotspots: List[Dict]) -> Optional[str]:
    """
    Render an image with clickable hotspots.
    
    Args:
        image_path: Path to the image file.
        hotspots: List of hotspot definitions with x, y, width, height, and id.
        
    Returns:
        ID of clicked hotspot or None.
    """
    # This would use streamlit-image-coordinates in production
    st.image(image_path, use_container_width=True)
    st.info("Interactive hotspots coming soon. Use the buttons above to explore controls.")
    return None


def render_tooltip(control_name: str) -> str:
    """
    Generate HTML tooltip for a control.
    
    Args:
        control_name: Name of the control.
        
    Returns:
        HTML string for tooltip.
    """
    all_controls = {**FRONT_PANEL_CONTROLS, **REAR_PANEL_CONNECTIONS}
    
    for key, control in all_controls.items():
        if control['name'] == control_name:
            tips_html = "".join(f"<li>{tip}</li>" for tip in control.get('tips', []))
            return f"""
            <div class="tooltip">
                <strong>{control['name']}</strong>
                <p>{control['description']}</p>
                <ul>{tips_html}</ul>
            </div>
            """
    
    return ""
