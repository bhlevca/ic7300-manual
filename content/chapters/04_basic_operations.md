# Basic Operations

This chapter covers the fundamental operations of your IC-7300, from power-on to making your first contact.

## First Power On

### Initial Setup Sequence

1. **Verify connections**:
   - Power supply connected and off
   - Antenna connected
   - Ground connected (recommended)

2. **Power on the supply**:
   - Turn on your 13.8V power supply first
   - Verify voltage with meter if unsure

3. **Power on the IC-7300**:
   - Press and hold **POWER** for 1 second
   - Display illuminates, startup screen appears
   - Radio comes up on last used frequency

### Setting Date and Time

Accurate time is important, especially for digital modes:

1. Press **MENU**
2. Touch **SET**
3. Touch **Time Set**
4. Touch **Date/Time**
5. Set the date: Year, Month, Day
6. Set the time: Hour, Minute
7. Touch **SET** to confirm

💡 **Tip**: For FT8 and digital modes, time must be accurate within ±1 second!

---

## Tuning and Frequency Selection

### Using the Main Dial

The large **MAIN DIAL** is your primary tuning control:

- **Slow rotation**: Fine tuning (1 Hz, 10 Hz steps)
- **Fast rotation**: Rapid tuning (100 Hz, 1 kHz steps)
- **Push dial**: Access MULTI control options

### Direct Frequency Entry

For quick frequency changes:

1. Touch the **frequency display** (MHz portion)
2. Touch **keypad icon** (123)
3. Enter frequency in kHz (e.g., 14250 for 14.250 MHz)
4. Touch **ENT** to confirm

### Changing Bands

**Method 1 - Touch Screen**:
1. Touch the **MHz** portion of frequency display
2. Touch the desired band (160m, 80m, 40m, etc.)

**Method 2 - Band Stack**:
- Touch the same band multiple times
- Cycles through 3 stored frequencies per band

### Band Stack Memory

The IC-7300 remembers 3 frequencies for each band:

1. Tune to desired frequency
2. Hold **MW** (Memory Write) for 1 second
3. Repeat for other frequencies
4. Now touching the band cycles through them

---

## Mode Selection

### Voice Modes

**SSB (Single Side Band)**:
- Press **SSB** button to toggle USB/LSB
- USB: Standard for frequencies above 10 MHz
- LSB: Standard for frequencies below 10 MHz
- Best for voice communication on HF

**AM (Amplitude Modulation)**:
- Press **AM** button
- Used for broadcast listening
- Power reduced to 25W carrier

**FM (Frequency Modulation)**:
- Press **FM** button  
- Used on 10m and 6m repeaters
- Full 100W output available

### Digital Modes

**SSB-D (Data Mode)**:
- Press **SSB**, then touch **DATA** on screen
- Display shows USB-D or LSB-D
- Used for FT8, PSK31, SSTV

**RTTY**:
- Press **RTTY** button
- Built-in decoder shows text on screen
- 45.45 baud standard

**CW**:
- Press **CW** button
- Built-in keyer available
- BK-IN for break-in operation

---

## Adjusting Volume and Squelch

### Audio Volume (AF)

Use the **inner ring** of the AF/RF-SQL knob:

- Rotate clockwise to increase
- Affects speaker and headphones
- Independent of USB audio levels

### RF Gain

Use the **outer ring**, rotated counter-clockwise from center:

- Reduces receiver sensitivity
- Use when strong signals overload receiver
- Maximum sensitivity at 12 o'clock

### Squelch

Use the **outer ring**, rotated clockwise from center:

- Sets threshold for audio output
- Signals below threshold are muted
- Keep open (counter-clockwise) for SSB/CW

---

## Using the S-Meter

The S-meter shows signal strength:

| Reading | Meaning |
|---------|---------|
| S1-S3 | Weak signal |
| S5-S7 | Moderate signal |
| S9 | Strong signal |
| S9+10dB | Very strong |
| S9+40dB | Extremely strong |

💡 **Tip**: Each S-unit represents approximately 6 dB.

---

## Transmitting

### Before You Transmit

1. **Check your license** - Ensure you're authorized for the frequency and mode
2. **Listen first** - Make sure the frequency is clear
3. **Check SWR** - Verify antenna is matched
4. **Reduce power** - Start with lower power, increase if needed

### Voice Transmission (SSB/AM/FM)

1. Select appropriate mode
2. Hold **PTT** on microphone (or use VOX)
3. Speak in normal voice, close to mic
4. Release PTT when finished
5. Wait for response

### Adjusting Microphone Gain

1. Press **MULTI** knob
2. Touch **MIC GAIN** on screen
3. Rotate MULTI to adjust
4. ALC meter should barely move on voice peaks

**Ideal Settings**:
- ALC just moving on peaks
- Power meter shows ~75-100W peaks on SSB
- Clear audio reports from others

### Power Output Control

1. Press **MULTI** knob
2. Touch **RF POWER** on screen
3. Rotate MULTI to adjust (0-100%)

**Recommended Power Levels**:

| Situation | Power |
|-----------|-------|
| Local contacts | 10-25W |
| DX on good bands | 50-75W |
| DX on poor bands | 100W |
| Digital modes | 25-50W |
| QRP operation | 5W |

---

## Using the Spectrum Scope

The spectrum scope is one of the IC-7300's best features.

### Opening the Scope

1. Press **SCOPE** button
2. Full-screen spectrum appears
3. Press again for mini scope
4. Press again to disable

### Understanding the Display

**Spectrum** (top portion):
- Shows signal strength vs. frequency
- Peaks indicate signals
- Touch peaks to tune to them

**Waterfall** (bottom portion):
- Shows signals over time
- Signals appear as colored traces
- Helps identify weak signals

### Scope Modes

**Center Mode**:
- Your frequency is always centered
- Good for general tuning
- Shows span around your frequency

**Fixed Mode**:
- Shows fixed frequency range
- Good for monitoring a band segment
- Touch edges to scroll

### Adjusting the Scope

Touch **EXPD** on screen for:
- Span: ±2.5, ±5, ±10, ±25, ±50, ±100, ±250 kHz
- Reference level: Adjust noise floor display
- Speed: FAST, MID, SLOW

---

## Making Your First Contact

### Calling CQ

1. Find a clear frequency
2. Listen for 10-15 seconds
3. Ask "Is this frequency in use?"
4. Wait 5 seconds
5. Call: "CQ CQ CQ, this is [your call] calling CQ..."
6. Repeat 2-3 times
7. End with "...standing by"

### Answering a CQ

1. Wait for station to finish CQ
2. Say their callsign once, your call twice
3. Example: "W1ABC, this is VA3XYZ, VA3XYZ"
4. Wait for response

### Basic QSO Format

A typical voice contact includes:
1. Signal report (RS: Readability, Strength)
2. Name and QTH (location)
3. Brief description of equipment
4. Weather and other pleasantries
5. Sign off with 73 (best regards)

**Example Exchange**:
> "W1ABC from VA3XYZ, you're 5 by 9 in Toronto, Ontario. 
> Name here is Bogdan, using an IC-7300 and a dipole. 
> How copy? Over."

---

## Using Memories

### Saving a Memory

1. Tune to desired frequency and mode
2. Press **MW** (Memory Write)
3. Touch desired memory channel
4. Touch **MW** to save

### Recalling a Memory

1. Press **M-CH** to enter memory mode
2. Rotate **MAIN DIAL** to select channel
3. Or touch **MEMO** and select from list

### Memory Contents

Each memory stores:
- Frequency
- Mode
- Filter settings
- Name (optional)
- Tone settings (for FM)

---

## Quick Menu Shortcuts

The **QUICK** button provides fast access to common settings.

**In SSB Mode**:
- Compression level
- VOX settings
- Microphone gain

**In CW Mode**:
- Key speed (WPM)
- Sidetone pitch
- Break-in mode

**In FM Mode**:
- Tone frequency
- Offset direction
- Repeater settings

---

## Daily Operating Tips

### Before Operating

- [ ] Check antenna connections
- [ ] Verify power supply
- [ ] Set correct time
- [ ] Check operating frequency/band conditions

### During Operating

- [ ] Monitor SWR periodically
- [ ] Use minimum power needed
- [ ] Keep transmissions brief
- [ ] Log contacts

### After Operating

- [ ] Power down properly
- [ ] Log any outstanding contacts
- [ ] Note any issues for later

---

*Continue to [Spectrum Scope](05_spectrum_scope.md) for detailed information on using the scope and waterfall display.*
