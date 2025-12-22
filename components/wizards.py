"""
Wizards Component
Step-by-step guided procedures with navigation.
"""

import streamlit as st
from typing import List, Dict, Optional, Callable


# Wizard definitions
WIZARDS = {
    "first_power_on": {
        "title": "First Power On",
        "description": "Initial setup when powering on your IC-7300 for the first time.",
        "steps": [
            {
                "title": "Connect Power Supply",
                "content": """
Before powering on, ensure your power supply is properly connected:

1. Connect the power cable to the DC 13.8V connector on the rear panel
2. Ensure the power supply is rated for at least **23 Amps**
3. Check polarity: **Center pin is positive (+)**
4. Turn on your power supply first

⚠️ **Warning**: Using incorrect voltage or polarity can damage the transceiver!
                """,
                "image": None
            },
            {
                "title": "Connect Antenna",
                "content": """
Connect your antenna before transmitting:

1. Connect your antenna feed line to the **ANT** connector (SO-239)
2. Use quality coaxial cable (RG-213, LMR-400, etc.)
3. Ensure the connector is snug but not over-tightened
4. If using a new antenna, you'll want to check SWR before transmitting

💡 **Tip**: Never transmit without an antenna connected - it can damage the finals!
                """,
                "image": None
            },
            {
                "title": "Power On",
                "content": """
Now power on the transceiver:

1. Press and hold the **POWER** button for about 1 second
2. The display will light up and show the startup screen
3. The power LED will glow green

The radio will start on the last frequency and mode you were using 
(or factory defaults if this is truly the first power-on).
                """,
                "image": None
            },
            {
                "title": "Set Date and Time",
                "content": """
Setting the correct time is important, especially for digital modes:

1. Press **MENU**
2. Touch **SET**
3. Scroll to **Time Set**
4. Touch **Date/Time**
5. Set the correct date and time using the touch screen
6. Press **EXIT** to save

💡 **Tip**: For FT8/digital modes, time must be accurate within ±1 second!
                """,
                "image": None
            },
            {
                "title": "Adjust Volume",
                "content": """
Set a comfortable audio level:

1. Rotate the inner ring of the **AF/RF-SQL** knob to adjust volume
2. Start at about 9 o'clock position
3. Fine-tune to your preference

The volume affects both the internal speaker and headphones.
                """,
                "image": None
            }
        ]
    },
    
    "tune_antenna": {
        "title": "Using the Antenna Tuner",
        "description": "How to use the built-in automatic antenna tuner to match your antenna.",
        "steps": [
            {
                "title": "Check SWR First",
                "content": """
Before using the tuner, check the antenna's natural SWR:

1. Set the desired frequency and band
2. Press **TUNER** to ensure the tuner is **OFF** (no icon shown)
3. Select a mode that produces constant carrier (RTTY works well)
4. Touch the TX meter area to show **SWR**
5. Key the transmitter briefly and observe the SWR reading

📊 **SWR Reading Guide**:
- 1.0 - 1.5: Excellent, no tuning needed
- 1.5 - 2.0: Good, tuner optional
- 2.0 - 3.0: Fair, use the tuner
- 3.0+: High, antenna needs adjustment or use Emergency mode
                """,
                "image": None
            },
            {
                "title": "Enable the Tuner",
                "content": """
Enable the antenna tuner:

1. Press **TUNER** button once
2. The **TUNE** icon appears on screen (not highlighted)
3. The tuner is now in the signal path

This puts the previously memorized tuning in line. If you've tuned 
this frequency before, you may not need to retune.
                """,
                "image": None
            },
            {
                "title": "Start Tuning",
                "content": """
Initiate the automatic tuning process:

1. Hold down **TUNER** for about 1 second
2. The **TUNE** icon will blink during tuning
3. The radio will transmit briefly while finding the best match
4. Tuning takes 2-3 seconds typically

⚠️ The radio transmits during tuning - ensure the frequency is clear!

When complete, the **TUNE** icon stops blinking and remains lit.
                """,
                "image": None
            },
            {
                "title": "Verify SWR",
                "content": """
Check the SWR after tuning:

1. Key the transmitter again
2. Observe the SWR meter
3. It should now show 1.5:1 or better

The tuner memorizes settings for each frequency segment, so it will 
recall these settings when you return to this frequency.

💡 **Tip**: If SWR is still high, your antenna may have issues that 
the tuner cannot compensate for.
                """,
                "image": None
            }
        ]
    },
    
    "setup_ft8": {
        "title": "Setting Up FT8 with WSJT-X",
        "description": "Complete guide to configuring your IC-7300 for FT8 digital mode operation.",
        "steps": [
            {
                "title": "Install USB Driver",
                "content": """
First, install the ICOM USB driver:

**Windows:**
1. Download the driver from [ICOM website](https://www.icomamerica.com/support)
2. Run the installer **before** connecting the USB cable
3. Follow the installation prompts

**Linux:**
- The driver is usually included in the kernel (CP210x)
- Check with: `lsmod | grep cp210x`

**Mac:**
- Download Silicon Labs driver from ICOM website
- Install and restart

⚠️ Do NOT connect the USB cable until the driver is installed!
                """,
                "image": None
            },
            {
                "title": "Connect USB Cable",
                "content": """
Connect the radio to your computer:

1. Use a USB A to USB B cable (like a printer cable)
2. Connect the B end to the **USB** port on the radio's rear panel
3. Connect the A end to your computer
4. Windows will detect new hardware

Check Device Manager (Windows) for:
- **Silicon Labs CP210x USB to UART Bridge (COM#)**

Note the COM port number - you'll need it for WSJT-X.
                """,
                "image": None
            },
            {
                "title": "Configure Radio Settings",
                "content": """
Set up the IC-7300 for digital mode operation:

1. Press **MENU** → **SET** → **Connectors**
2. Configure these settings:

| Setting | Value |
|---------|-------|
| DATA MOD | USB |
| USB MOD Level | 40-50% |
| DATA OFF MOD | MIC,ACC |
| ACC/USB Output Level | 50% |

3. Scroll to **CI-V** section:

| Setting | Value |
|---------|-------|
| CI-V USB Baud Rate | 115200 |
| CI-V USB Echo Back | ON |

4. Press **EXIT** to save
                """,
                "image": None
            },
            {
                "title": "Set Operating Mode",
                "content": """
Set the radio to DATA mode:

1. Press the **SSB** mode button
2. Touch **DATA** on the screen
3. The display should show **USB-D**

This enables the USB audio interface for transmit.

Also set the filter:
1. Press **FILTER**
2. Select **FIL1** (3.6 kHz wide)
                """,
                "image": None
            },
            {
                "title": "Install WSJT-X",
                "content": """
Download and install WSJT-X:

1. Download from: https://wsjt.sourceforge.io/
2. Choose your operating system version
3. Run the installer

**Windows**: Run the .exe installer
**Linux**: Use the .deb or .rpm package
**Mac**: Use the .dmg file

After installation, run WSJT-X for initial setup.
                """,
                "image": None
            },
            {
                "title": "Configure WSJT-X - General",
                "content": """
Configure WSJT-X basic settings:

1. Go to **File** → **Settings**
2. On the **General** tab:
   - Enter your **Call Sign**
   - Enter your **Grid Square** (e.g., FN03)
   - Check **Display distance in miles** if preferred

3. Click **OK** to save
                """,
                "image": None
            },
            {
                "title": "Configure WSJT-X - Radio",
                "content": """
Configure WSJT-X radio control:

1. Go to **File** → **Settings** → **Radio** tab
2. Set these options:

| Setting | Value |
|---------|-------|
| Rig | Icom IC-7300 |
| Serial Port | COM# (your port) |
| Baud Rate | 115200 |
| Data Bits | 8 |
| Stop Bits | 1 |
| Handshake | None |
| PTT Method | CAT |
| Mode | Data/Pkt |
| Split Operation | Fake It |

3. Click **Test CAT** - button should turn green
4. Click **Test PTT** - radio should key up briefly
                """,
                "image": None
            },
            {
                "title": "Configure WSJT-X - Audio",
                "content": """
Configure WSJT-X audio:

1. Go to **File** → **Settings** → **Audio** tab
2. Set these options:

| Setting | Value |
|---------|-------|
| Input | USB Audio CODEC |
| Output | USB Audio CODEC |

On Windows, these may appear as:
- **Microphone (USB Audio CODEC)**
- **Speakers (USB Audio CODEC)**

3. Click **OK** to save

💡 **Tip**: In Windows Sound settings, set the CODEC to 48000 Hz, 
1 channel (mono) for best results.
                """,
                "image": None
            },
            {
                "title": "Set Audio Levels",
                "content": """
Adjust audio levels for proper operation:

**Receive Level:**
1. Tune to an FT8 frequency (e.g., 14.074 MHz)
2. Watch the green audio level bar in WSJT-X
3. Adjust until it shows about 30-40 dB
4. Adjust radio's USB output level if needed

**Transmit Level:**
1. Set radio power to about 30% with **MULTI** knob
2. Click **Tune** in WSJT-X
3. Adjust **Pwr** slider until ALC just starts to move
4. Back off slightly - ALC should barely move or stay at zero

⚠️ Overdriving (high ALC) causes splatter and interference!
                """,
                "image": None
            },
            {
                "title": "Synchronize Time",
                "content": """
FT8 requires accurate time (within ±1 second):

**Windows:**
1. Install Meinberg NTP from: https://www.meinbergglobal.com/english/sw/ntp.htm
2. Follow installation defaults
3. Time will stay synchronized automatically

**Linux:**
- Most distros use systemd-timesyncd or chrony
- Check status: `timedatectl status`
- Should show "System clock synchronized: yes"

**Verify in WSJT-X:**
- The DT (delta time) column should show values close to 0.0
- Values beyond ±1.0 indicate time sync issues
                """,
                "image": None
            },
            {
                "title": "Make Your First FT8 QSO!",
                "content": """
You're ready to operate FT8:

1. Select an FT8 frequency:
   - 20m: 14.074 MHz
   - 40m: 7.074 MHz
   - 15m: 21.074 MHz

2. Set mode to **USB-D** on the radio

3. Watch the waterfall - signals appear as yellow/red traces

4. Double-click a **CQ** call to answer

5. WSJT-X handles the QSO sequence automatically

6. After the QSO, the contact is logged

🎉 **Congratulations!** You've made your first FT8 contact!

💡 **Tip**: Start with 30-50 watts, increase only if needed.
                """,
                "image": None
            }
        ]
    },
    
    "change_band": {
        "title": "Changing Bands",
        "description": "How to change frequency bands on the IC-7300.",
        "steps": [
            {
                "title": "Touch the Frequency Display",
                "content": """
The easiest way to change bands:

1. Touch the **MHz** portion of the frequency display
2. A band selection menu appears
3. Touch the desired band (160m through 6m)

The radio will switch to the last-used frequency on that band.
                """,
                "image": None
            },
            {
                "title": "Alternative: Use Band Stack",
                "content": """
The IC-7300 has a band stack that remembers 3 frequencies per band:

1. Touch the **MHz** display
2. Touch the same band button multiple times
3. It cycles through the 3 stored frequencies

This is great for monitoring multiple frequencies on the same band.
                """,
                "image": None
            },
            {
                "title": "Direct Frequency Entry",
                "content": """
Enter a specific frequency directly:

1. Touch the **MHz** display
2. Touch the **keypad** icon (123)
3. Enter the frequency using the number pad
   - Example: For 14.250 MHz, enter 14250
4. Touch **ENT** to confirm

The radio will switch to that frequency and appropriate mode.
                """,
                "image": None
            }
        ]
    }
}


def render_wizard(wizard_id: str):
    """
    Render a step-by-step wizard.
    
    Args:
        wizard_id: ID of the wizard to render.
    """
    if wizard_id not in WIZARDS:
        st.error(f"Wizard '{wizard_id}' not found.")
        return
    
    wizard = WIZARDS[wizard_id]
    
    # Initialize session state for this wizard
    state_key = f"wizard_{wizard_id}_step"
    if state_key not in st.session_state:
        st.session_state[state_key] = 0
    
    current_step = st.session_state[state_key]
    total_steps = len(wizard['steps'])
    
    # Header
    st.markdown(f"## 📋 {wizard['title']}")
    st.markdown(wizard['description'])
    
    # Progress bar
    progress = (current_step + 1) / total_steps
    st.progress(progress, text=f"Step {current_step + 1} of {total_steps}")
    
    # Current step content
    step = wizard['steps'][current_step]
    
    st.markdown(f"### Step {current_step + 1}: {step['title']}")
    st.markdown(step['content'])
    
    if step.get('image'):
        st.image(step['image'], caption=step['title'])
    
    # Navigation buttons
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if current_step > 0:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state[state_key] = current_step - 1
                st.rerun()
    
    with col2:
        if st.button("🔄 Restart Wizard", use_container_width=True):
            st.session_state[state_key] = 0
            st.rerun()
    
    with col3:
        if current_step < total_steps - 1:
            if st.button("Next ➡️", use_container_width=True):
                st.session_state[state_key] = current_step + 1
                st.rerun()
        else:
            if st.button("✅ Complete!", use_container_width=True):
                st.success("🎉 Wizard completed! You can restart or navigate to other sections.")
                st.session_state[state_key] = 0


def get_available_wizards() -> List[Dict]:
    """
    Get list of available wizards.
    
    Returns:
        List of wizard metadata dictionaries.
    """
    return [
        {
            'id': wizard_id,
            'title': wizard['title'],
            'description': wizard['description'],
            'steps': len(wizard['steps'])
        }
        for wizard_id, wizard in WIZARDS.items()
    ]


def render_wizard_selector():
    """
    Render a wizard selection interface.
    """
    st.markdown("## 📋 Step-by-Step Guides")
    st.markdown("Select a wizard to follow guided instructions:")
    
    wizards = get_available_wizards()
    
    for wizard in wizards:
        with st.expander(f"📖 {wizard['title']} ({wizard['steps']} steps)"):
            st.markdown(wizard['description'])
            if st.button(f"Start '{wizard['title']}'", key=f"start_{wizard['id']}"):
                st.session_state.active_wizard = wizard['id']
                st.rerun()
