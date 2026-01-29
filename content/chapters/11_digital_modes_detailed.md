# Digital Modes and Computer Connection

This chapter provides comprehensive guidance on connecting your IC-7300 to a computer and operating digital modes. The IC-7300's built-in USB audio interface makes digital operation remarkably simple compared to older radios.

## Understanding the IC-7300's Digital Interface

### The USB Connection Advantage

The IC-7300 has a **built-in USB audio codec and CAT interface**, which means:

- **One USB cable** provides both audio AND radio control
- **No external interface** (SignaLink, etc.) required
- **No ground loop issues** common with external interfaces
- **Consistent audio levels** without analog adjustments

### What the USB Port Provides

| Function | Description |
|----------|-------------|
| Audio IN | Transmit audio from computer to radio |
| Audio OUT | Receive audio from radio to computer |
| CAT Control | Computer control of frequency, mode, PTT |
| CI-V Protocol | ICOM's Computer Interface protocol |

---

## Initial Computer Connection

### Step 1: Install USB Driver

**Before connecting the USB cable**, install the ICOM USB driver.

**Windows:**
1. Download driver from ICOM website (search "IC-7300 USB driver")
2. Run the installer
3. Follow installation prompts
4. Restart computer if prompted

**Linux:**
- Usually no driver needed (kernel includes CP210x driver)
- Verify with: `lsmod | grep cp210x`
- If not loaded: `sudo modprobe cp210x`

**MacOS:**
- Download Silicon Labs CP210x driver
- Install and restart
- May need to allow in Security settings

### Step 2: Connect USB Cable

1. Use a **USB Type A to Type B cable** (like printer cable)
2. Connect Type B end to radio's rear panel USB port
3. Connect Type A end to computer
4. Radio can be ON or OFF

### Step 3: Verify Connection

**Windows:**
1. Open Device Manager
2. Look under "Ports (COM & LPT)"
3. You should see: **Silicon Labs CP210x USB to UART Bridge (COM#)**
4. Note the COM port number - you'll need it later

**Linux:**
```bash
ls /dev/ttyUSB*
# Should show /dev/ttyUSB0 or similar
```

**MacOS:**
```bash
ls /dev/tty.SLAB*
# Should show the serial device
```

### Step 4: Configure Radio Settings

These settings are critical for reliable digital operation:

**Access: MENU → SET → Connectors**

| Setting | Value | Purpose |
|---------|-------|---------|
| CI-V Baud Rate | 115200 | Fast communication speed |
| CI-V Address | 94h | Radio's CI-V address (default) |
| CI-V Transceive | ON | Radio reports changes to software |
| CI-V USB Port | Unlink from REMOTE | Separates USB from rear CI-V jack |
| CI-V USB Baud Rate | 115200 | USB-specific baud rate |
| CI-V USB Echo Back | ON | Required for most software |

**Audio Settings (same menu):**

| Setting | Value | Purpose |
|---------|-------|---------|
| DATA MOD | USB | TX audio comes from USB |
| DATA OFF MOD | MIC,ACC | Non-DATA mode audio source |
| USB MOD Level | 50% | TX audio level (adjust later) |
| USB AF Output Level | 50% | RX audio level (adjust later) |
| ACC/USB AF SQL | OFF | Audio always present |
| ACC/USB AF Beep Output | OFF | No beeps to computer |
| ACC/USB AF IF Output | OFF | Raw audio, not IF |

---

## Audio Level Configuration

### Windows Audio Settings

**Setting Up the USB Audio Device:**

1. Right-click speaker icon in system tray
2. Select "Sound settings"
3. Find "USB Audio CODEC" in input and output devices

**For Recording (RX Audio to Computer):**
1. Go to "Sound" control panel (old interface)
2. Recording tab
3. Select "USB Audio CODEC"
4. Properties → Levels → Set to 50%
5. Properties → Advanced → 48000 Hz, 16-bit, Mono

**For Playback (TX Audio from Computer):**
1. Playback tab
2. Select "USB Audio CODEC" 
3. Properties → Levels → Set to 50%
4. Properties → Advanced → 48000 Hz, 16-bit, Mono

### Linux Audio Settings

**Using PulseAudio:**
```bash
# List audio devices
pactl list sources short
pactl list sinks short

# The USB codec will appear as a source (input) and sink (output)
```

**Using ALSA directly:**
```bash
# List devices
arecord -l
aplay -l
```

### Finding the Sweet Spot

**RX Audio Level:**
1. Tune to a moderately strong signal
2. Open your digital mode software
3. Watch the audio level meter
4. Target: Peaks around -10 to -20 dB
5. Adjust USB AF Output Level on radio if needed

**TX Audio Level:**
1. Set radio to DATA mode (USB-D)
2. Set power to 50%
3. Enable transmit from software
4. Watch ALC meter on radio
5. **ALC should barely move** (or not at all)
6. If ALC pins high, reduce software output or USB MOD Level

⚠️ **Critical**: High ALC = distorted signal = interference to others!

---

## Operating Mode: DATA vs USB

### Understanding DATA Mode

The IC-7300 has a special "DATA" mode that differs from regular USB:

**USB Mode (for voice):**
- Uses microphone for audio input
- Compression, EQ can be applied
- Processing optimized for voice

**USB-D Mode (DATA):**
- Uses USB audio codec for input
- **No compression or processing**
- Clean, flat audio response
- Required for proper digital operation

### Selecting DATA Mode

1. Press **SSB** button to select USB (or LSB)
2. Touch **DATA** on the screen
3. Display should show **USB-D** (or **LSB-D**)

**Verify DATA Mode:**
- Touch the mode indicator on screen
- "USB-D" should be highlighted
- This routes USB audio to the transmitter

---

## FT8/FT4 with WSJT-X

### About FT8

FT8 (Franke-Taylor design, 8-FSK modulation) is currently the most popular digital mode:
- 15-second transmission periods
- Works with very weak signals (-24 dB S/N)
- Semi-automated contact procedure
- Requires accurate computer time

### Installing WSJT-X

1. Download from: https://wsjt.sourceforge.io/
2. Install for your operating system
3. Run WSJT-X

### WSJT-X Configuration

**File → Settings → General:**
| Setting | Value |
|---------|-------|
| My Call | Your call sign |
| My Grid | Your grid square (e.g., FN31) |
| Display | Your preference |

**File → Settings → Radio:**
| Setting | Value |
|---------|-------|
| Rig | Icom IC-7300 |
| Serial Port | Your COM port (e.g., COM3) |
| Baud Rate | 115200 |
| Data Bits | 8 |
| Stop Bits | 1 |
| Handshake | None |
| PTT Method | CAT |
| Transmit Audio Source | Rear/Data |
| Mode | Data/Pkt |
| Split Operation | Fake It |

**Click "Test CAT"** - Button should turn green
**Click "Test PTT"** - Radio should key momentarily

**File → Settings → Audio:**
| Setting | Value |
|---------|-------|
| Input | USB Audio CODEC (or Microphone - USB Audio CODEC) |
| Output | USB Audio CODEC (or Speakers - USB Audio CODEC) |

### FT8 Operating Procedure

**Standard FT8 Frequencies:**

| Band | Frequency | Notes |
|------|-----------|-------|
| 160m | 1.840 MHz | Night only |
| 80m | 3.573 MHz | Popular |
| 60m | 5.357 MHz | Channel-specific |
| 40m | 7.074 MHz | Very popular |
| 30m | 10.136 MHz | Popular |
| 20m | 14.074 MHz | Most popular |
| 17m | 18.100 MHz | |
| 15m | 21.074 MHz | |
| 12m | 24.915 MHz | |
| 10m | 28.074 MHz | |
| 6m | 50.313 MHz | |

**Making FT8 Contacts:**

1. **Set frequency**: Tune to FT8 frequency (e.g., 14.074 MHz)
2. **Set mode**: USB-D on radio
3. **Enable monitoring**: Click "Monitor" in WSJT-X
4. **Wait for decode**: Signals appear in left panel
5. **Call CQ or answer CQ**:
   - To call CQ: Select your frequency, click "Enable TX", then "CQ"
   - To answer: Double-click on a CQ in the decode window
6. **Complete exchange**: Software handles the sequence
7. **Log contact**: WSJT-X logs automatically

### FT8 Tips from Experience

**Time Synchronization:**
- FT8 requires time accuracy within ±1 second
- Windows: Install Meinberg NTP or Dimension 4
- Linux: Enable systemd-timesyncd or chrony
- Check "DT" column - values should be near 0.0

**Power Level:**
- Start with 25-50W
- FT8 is efficient - more power rarely helps
- High power causes unnecessary interference
- Watch ALC - should NOT move

**Frequency Selection:**
- WSJT-X shows your TX frequency in waterfall
- Pick a clear spot (no other signals)
- Stay within the standard FT8 window (0-3000 Hz audio)

**Patience:**
- Propagation matters more than power
- If no response, try different bands
- Activity varies by time of day

---

## PSK31 with Fldigi

### About PSK31

PSK31 (Phase Shift Keying, 31 baud) is a keyboard-to-keyboard mode:
- Very narrow bandwidth (~31 Hz)
- Good for ragchewing
- Readable at low signal levels
- Real-time text exchange

### Installing Fldigi

1. Download from: http://www.w1hkj.com/
2. Install for your operating system
3. Run Fldigi and complete setup wizard

### Fldigi Configuration

**Configure → Rig Control → Hamlib:**
- Rig: Icom IC-7300
- Device: Your serial port
- Baud Rate: 115200
- Enable: PTT via Hamlib

**Configure → Sound Card → Devices:**
- Capture: USB Audio CODEC
- Playback: USB Audio CODEC

**Configure → Sound Card → Audio:**
- Sample rate: 48000 (Native)

### PSK31 Operating

**Standard PSK31 Frequencies:**
| Band | Frequency |
|------|-----------|
| 80m | 3.580 MHz |
| 40m | 7.070 MHz |
| 20m | 14.070 MHz |
| 15m | 21.070 MHz |
| 10m | 28.120 MHz |

**Making a PSK31 Contact:**

1. Set radio to USB-D
2. Tune to PSK frequency
3. Watch waterfall for PSK signals (narrow, rhythmic)
4. Click on a signal to decode it
5. To call CQ: Type your message and transmit
6. To answer: Transmit their call and yours

---

## RTTY (Radioteletype)

### About RTTY

RTTY is one of the oldest digital modes:
- Uses FSK (Frequency Shift Keying)
- 45.45 baud standard
- Two tones: Mark and Space
- Still popular in contests

### RTTY Configuration

**Radio Settings for RTTY:**
1. Can use RTTY mode (built-in decoder) or
2. Use USB-D with software decoder (more flexible)

**For Software RTTY (USB-D):**
- Same audio settings as other digital modes
- Software (Fldigi, MMTTY, etc.) does encoding/decoding

**For Built-in RTTY:**
- Press RTTY mode button
- Touch screen shows built-in RTTY decoder
- Can operate without computer for basic contacts

---

## JS8Call

### About JS8Call

JS8Call is derived from FT8 but designed for messaging:
- Longer transmissions possible
- Keyboard-to-keyboard style
- Store-and-forward capability
- Good for emergency communications

### JS8Call Setup

1. Download from: http://js8call.com/
2. Configuration similar to WSJT-X
3. Uses same CAT and audio settings

**Key Differences from FT8:**
- Variable-length messages
- Can relay through other stations
- "Heartbeat" feature for monitoring
- Built-in messaging system

---

## Troubleshooting Digital Modes

### No Audio to Computer

**Symptoms:** Software shows no signal, flat waterfall

**Check:**
1. Correct audio device selected in software
2. USB AF Output Level not zero on radio
3. Windows sound settings correct
4. Cable connected properly

**Fix:**
- Verify audio device in software settings
- Increase USB AF Output Level
- Check Windows Recording devices

### No Audio to Radio (TX)

**Symptoms:** PTT works but no power output, or low power

**Check:**
1. Correct audio device for output
2. Software audio output not muted
3. USB MOD Level not zero
4. DATA mode enabled (USB-D, not just USB)

**Fix:**
- Verify output device in software
- Check software TX audio slider
- Verify USB MOD Level is ~50%
- Ensure USB-D mode (touch DATA on screen)

### CAT Control Not Working

**Symptoms:** Test CAT fails, can't control radio

**Check:**
1. Correct COM port selected
2. Baud rate matches radio setting
3. CI-V address correct
4. CI-V Echo Back is ON
5. Driver installed properly

**Fix:**
- Verify COM port in Device Manager
- Match baud rate (115200 recommended)
- Try different CI-V USB Port settings
- Reinstall USB driver

### PTT Not Working

**Symptoms:** Radio won't transmit, or stays in TX

**Check:**
1. PTT method set to CAT
2. CAT control working (test first)
3. VOX not interfering
4. Correct mode (DATA mode for digital)

**Fix:**
- Use CAT PTT method in software
- Disable VOX when using digital modes
- Verify CAT is working before testing PTT

### Distorted TX Audio (High ALC)

**Symptoms:** Other stations report bad audio, ALC pegged

**Check:**
1. Software output level too high
2. USB MOD Level too high
3. Not in DATA mode (compression applied)

**Fix:**
- Reduce software output (Pwr slider in WSJT-X)
- Reduce USB MOD Level to 30-40%
- Ensure USB-D mode selected

### Decoding Problems

**Symptoms:** Can see signals but no decode, or wrong decode

**Check:**
1. Time synchronization (for FT8)
2. Audio level appropriate
3. Correct mode selected in software
4. Frequency calibration

**Fix:**
- Sync computer time to internet
- Adjust audio level to proper range
- Verify software mode matches signals
- Calibrate against known signals (WWV)

---

## Digital Mode Quick Reference

### Audio Level Guidelines

| Meter | Target |
|-------|--------|
| Software RX level | -10 to -20 dB peaks |
| ALC meter | No movement or barely touching |
| Power meter | Should match software power setting |

### Recommended Power Levels

| Mode | Power | Notes |
|------|-------|-------|
| FT8 | 25-50W | Very efficient, more is rarely better |
| FT4 | 25-50W | Same as FT8 |
| PSK31 | 25-50W | QRP works well |
| RTTY | 50-75W | Full power OK for contests |
| JS8Call | 25-50W | Similar to FT8 |

### CI-V Settings Summary

| Setting | Value |
|---------|-------|
| CI-V Baud Rate | 115200 |
| CI-V Address | 94h |
| CI-V USB Echo Back | ON |
| CI-V USB Port | Unlink from REMOTE |

### Software PTT Settings

| Software | PTT Method |
|----------|------------|
| WSJT-X | CAT |
| Fldigi | Hamlib |
| JS8Call | CAT |
| MMTTY | CAT |

---

## Advanced: Multiple Instances

### Running Multiple Digital Mode Programs

You can run multiple programs that share the radio, but:

**What Works:**
- One program for CAT control
- Multiple programs for audio (if OS allows)
- Logging programs alongside operating software

**What Doesn't Work:**
- Two programs trying CAT control simultaneously
- Programs fighting over PTT

**Solution: Omni-Rig or FLRig**
- Virtual rig server that multiple programs connect to
- Single connection to radio
- Shares control among programs

---

## Summary: Digital Mode Checklist

```
DIGITAL MODE SETUP CHECKLIST
============================

Hardware:
□ USB cable connected (Type A to Type B)
□ USB driver installed
□ COM port identified

Radio Settings:
□ CI-V Baud Rate: 115200
□ CI-V USB Echo Back: ON
□ DATA MOD: USB
□ USB MOD Level: 50%
□ USB AF Output Level: 50%

Software Settings:
□ Correct rig selected (IC-7300)
□ Correct COM port
□ Baud rate: 115200
□ PTT Method: CAT
□ Audio input: USB Audio CODEC
□ Audio output: USB Audio CODEC

Testing:
□ CAT test passes (green)
□ PTT test works
□ Audio levels appropriate
□ ALC stays low during TX
□ RX audio decodes correctly

Ready to Operate:
□ Radio in USB-D mode
□ Time synchronized
□ Frequency correct for mode
□ Power level appropriate
```
