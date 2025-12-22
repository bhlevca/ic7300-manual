# WSJT-X / FT8 Setup Guide

FT8 has revolutionized amateur radio, enabling contacts with extremely weak signals. This chapter provides complete setup instructions for WSJT-X with your IC-7300.

## What is FT8?

FT8 (Franke-Taylor design, 8-FSK modulation) is a digital mode designed for weak signal communication:

- **15-second transmit/receive cycles**
- **Works 10-20 dB below the noise floor**
- **Standardized message exchange**
- **Automatic decoding**

### FT8 Frequencies

| Band | Dial Frequency | USB Mode |
|------|----------------|----------|
| 160m | 1.840 MHz | USB-D |
| 80m | 3.573 MHz | USB-D |
| 40m | 7.074 MHz | USB-D |
| 30m | 10.136 MHz | USB-D |
| 20m | 14.074 MHz | USB-D |
| 17m | 18.100 MHz | USB-D |
| 15m | 21.074 MHz | USB-D |
| 12m | 24.915 MHz | USB-D |
| 10m | 28.074 MHz | USB-D |
| 6m | 50.313 MHz | USB-D |

---

## Step 1: Install USB Driver

Before anything else, install the ICOM USB driver.

### Windows Installation

1. Download from: https://www.icomamerica.com/support
2. Search for "IC-7300" and find "USB Driver"
3. **Do NOT connect USB cable yet!**
4. Run installer as Administrator
5. Follow installation prompts
6. Restart computer if prompted
7. NOW connect USB cable to radio and computer
8. Wait for Windows to recognize device

### Verify Installation

1. Open Device Manager (right-click Start > Device Manager)
2. Expand "Ports (COM & LPT)"
3. Look for "Silicon Labs CP210x USB to UART Bridge (COM#)"
4. **Note the COM port number!**

Also check for audio device:
1. Open Sound Settings
2. Look for "USB Audio CODEC" in both Playback and Recording

---

## Step 2: Configure IC-7300

### Radio Settings

Press **MENU** > **SET** > **Connectors**:

```
Connectors Settings:
├── ACC/USB AF SQL ........... OFF (Open)
├── ACC/USB Output Level ..... 50%
├── ACC/USB AF Beep/Speech ... OFF
├── USB MOD Level ............ 50%
├── DATA OFF MOD ............. MIC,ACC
├── DATA MOD ................. USB
└── CI-V
    ├── CI-V USB Baud Rate ... 115200
    ├── CI-V USB Echo Back ... ON
    └── CI-V USB Port ........ Unlink from [REMOTE]
```

### Operating Mode

1. Press **SSB** to select USB mode
2. Touch **DATA** on screen
3. Display should show **USB-D**

### Filter Settings

1. Press **FILTER**
2. Select **FIL1** (3.6 kHz recommended)
3. Exit filter screen

### Function Settings

1. Press **FUNCTION**
2. Set **NB** (Noise Blanker): OFF
3. Set **NR** (Noise Reduction): OFF
4. Set **NOTCH**: OFF
5. Set **AGC**: FAST

---

## Step 3: Install WSJT-X

### Download

1. Go to: https://wsjt.sourceforge.io/
2. Click on "WSJT-X" in the left menu
3. Download the version for your operating system

### Windows Installation

1. Run the downloaded .exe installer
2. Accept license agreement
3. Choose installation folder (default is fine)
4. Create desktop shortcut (recommended)
5. Complete installation

### Linux Installation

```bash
# Debian/Ubuntu
sudo dpkg -i wsjtx_X.X.X_amd64.deb
sudo apt-get install -f  # Fix any dependencies

# Fedora/RHEL
sudo rpm -i wsjtx-X.X.X-linux64.rpm
```

### Mac Installation

1. Open the downloaded .dmg file
2. Drag WSJT-X to Applications folder
3. First launch: Right-click > Open (to bypass Gatekeeper)

---

## Step 4: Configure WSJT-X

### Initial Setup Wizard

On first launch, WSJT-X runs a setup wizard:

1. Enter your **Call Sign**
2. Enter your **Grid Square** (4 or 6 characters)
3. Click OK to continue

### Settings - General Tab

Go to **File** > **Settings** (or press F2):

**Station Details**:
- My Call: Your callsign
- My Grid: Your Maidenhead grid (e.g., FN03)
- CQ/73 in message: Leave unchecked for standard operation

**Display**:
- Check "Display distance in miles" if preferred
- Check "Show DXCC entity and worked before status"

### Settings - Radio Tab

This is the critical section:

| Setting | Value |
|---------|-------|
| Rig | Icom IC-7300 |
| Serial Port | COM# (your port from Step 1) |
| Baud Rate | 115200 |
| Data Bits | 8 |
| Stop Bits | 1 |
| Handshake | None |
| PTT Method | CAT |
| Transmit Audio Source | Rear/Data |
| Mode | Data/Pkt |
| Split Operation | Fake It or Rig (either works) |

**Test the Connection**:
1. Click **Test CAT** - button should turn GREEN
2. Click **Test PTT** - radio should briefly transmit
3. If either fails, check settings and COM port

### Settings - Audio Tab

| Setting | Value |
|---------|-------|
| Input | USB Audio CODEC (or Microphone IC-7300) |
| Output | USB Audio CODEC (or Speakers IC-7300) |

On Windows, you may need to scroll through the device list to find the correct entries.

💡 **Tip**: Rename audio devices in Windows Sound settings to "IC-7300" for easy identification.

### Settings - Reporting Tab (Optional but Recommended)

Enable PSK Reporter uploads:
1. Check "Enable PSK Reporter spotting"
2. Your signals will appear on pskreporter.info

Enable LoTW integration:
1. Enter LoTW credentials if you have an account

---

## Step 5: Set Audio Levels

Proper audio levels are critical for good operation.

### Receive Level

1. Tune to an FT8 frequency (e.g., 14.074 MHz)
2. Observe the green bar at bottom of WSJT-X
3. Target: **30-40 dB** shown on the meter
4. Adjust if needed:
   - In radio: MENU > SET > Connectors > ACC/USB Output Level
   - In Windows: Recording device properties > Levels

### Transmit Level (ALC Adjustment)

⚠️ **Critical: Never overdrive the transmitter!**

1. Set radio RF Power to about 30-50%
2. In WSJT-X, click **Tune**
3. Watch the ALC meter on the radio
4. Adjust the **Pwr** slider in WSJT-X:
   - ALC should barely move or stay at zero
   - If ALC moves significantly, reduce power
5. Click **Tune** again to stop

**Correct Power Setting**:
- Pwr slider typically at 25-50%
- ALC showing minimal movement
- Power output around 25-50W

---

## Step 6: Time Synchronization

FT8 requires accurate time (within ±1 second).

### Windows: Install Meinberg NTP

1. Download from: https://www.meinbergglobal.com/english/sw/ntp.htm
2. Choose "ntp-xxx-setup.exe"
3. Install with default options
4. Service starts automatically
5. Computer time will stay synchronized

### Verify Synchronization

In WSJT-X, watch the **DT** column in decoded messages:
- Values should be close to **0.0**
- If most DT values are > ±1.0, your clock needs adjustment

---

## Step 7: Making Your First FT8 QSO

### Getting Started

1. Open WSJT-X
2. Select **FT8** mode (Mode menu)
3. Tune to an FT8 frequency (e.g., 14.074 MHz on 20m)
4. Watch the waterfall - signals appear as colored traces

### Understanding the Display

**Waterfall**: Shows signals over time
- Yellow/red traces are signals
- Each signal occupies about 50 Hz
- Click a signal to set your TX frequency

**Band Activity**: Lists decoded stations
- CQ calls shown in bold
- Callsigns you've worked are marked

**Rx Frequency**: Where you're receiving
**Tx Frequency**: Where you'll transmit

### Answering a CQ

1. Wait for a CQ message to appear (e.g., "CQ W1ABC FN31")
2. **Double-click** on the CQ message
3. WSJT-X sets up the QSO automatically
4. Click **Enable Tx** to begin transmitting
5. The sequence proceeds automatically:
   - Your call + grid is sent
   - Await signal report
   - Send your report
   - Receive RR73 (acknowledgment)
   - Send 73

### Calling CQ

1. Click **CQ** in the Generate Std Msgs section
2. Click **Enable Tx**
3. Your CQ is sent during the next TX period
4. Wait for replies
5. Double-click a reply to begin the QSO

---

## Troubleshooting

### No Decodes Appearing

- Check mode is USB-D on radio
- Verify audio input level (30-40 dB)
- Confirm time is synchronized
- Ensure frequency is correct

### CAT Test Fails

- Verify COM port number
- Check baud rate is 115200
- Confirm CI-V USB Echo Back is ON
- Try a different USB port
- Close other programs using the COM port

### PTT Test Fails

- Ensure PTT Method is set to CAT
- Try different Split Operation setting
- Check radio is not in a menu screen

### Radio Not Transmitting

- Verify DATA mode is active (USB-D)
- Check audio output device setting
- Increase USB MOD Level in radio
- Verify software audio output level

### High SWR / Power Foldback

- Check antenna connection
- Use antenna tuner
- Reduce power

---

## Tips for Success

### General Operation

1. **Start with low power** (25-30W) - FT8 is effective at low power
2. **Let the sequence complete** - don't click Enable Tx multiple times
3. **Be patient** - especially on busy bands
4. **Use the waterfall** - find a clear spot before calling CQ

### Best Practices

- Don't transmit on top of other stations
- Keep your signal in the conventional passband (200-2500 Hz)
- Enable PSK Reporter to see where you're being heard
- Log all contacts for later QSL confirmation

### Band Selection

| Condition | Recommended Bands |
|-----------|-------------------|
| Daytime | 20m, 17m, 15m, 12m, 10m |
| Evening | 40m, 30m, 20m |
| Night | 80m, 40m, 30m |
| Poor conditions | 30m, 40m |
| DX openings | 15m, 12m, 10m |

---

## Quick Reference: WSJT-X Settings for IC-7300

### Radio Tab
```
Rig: Icom IC-7300
Serial Port: [Your COM port]
Baud Rate: 115200
PTT Method: CAT
Mode: Data/Pkt
Split: Fake It
```

### IC-7300 Settings
```
Mode: USB-D
Filter: FIL1 (3.6 kHz)
DATA MOD: USB
USB MOD Level: 40-50%
CI-V USB Baud Rate: 115200
CI-V USB Echo Back: ON
NB: OFF, NR: OFF, NOTCH: OFF
AGC: FAST
```

---

*For PSK31, RTTY, and other modes, continue to [Fldigi Setup](09_fldigi_setup.md). For JS8 keyboard chat mode, see [JS8Call](10_js8call.md).*
