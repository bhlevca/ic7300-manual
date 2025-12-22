# Digital Modes Overview

The IC-7300 excels at digital mode operation thanks to its built-in USB audio interface and CAT control. This chapter provides an overview of digital modes and general setup procedures.

## Why Digital Modes?

Digital modes offer several advantages:

- **Weak signal performance**: Modes like FT8 work with signals below the noise floor
- **Low power effectiveness**: 25-50W is often more than enough
- **Keyboard operation**: No microphone needed
- **Automatic logging**: Computer tracks all contacts
- **DX opportunities**: Work stations you'd never hear on voice

## Popular Digital Modes

| Mode | Speed | Bandwidth | Best For |
|------|-------|-----------|----------|
| FT8 | 15 sec | ~50 Hz | Weak signal DX |
| FT4 | 7.5 sec | ~80 Hz | Contests |
| PSK31 | Slow | ~31 Hz | Keyboard chat |
| RTTY | 45 baud | ~250 Hz | Contests, traffic |
| JS8 | Continuous | ~50 Hz | Keyboard QSOs |
| WSPR | 2 min | ~6 Hz | Propagation study |

---

## Basic Setup Requirements

### Hardware Needed

**Essential**:
- IC-7300 transceiver
- Computer (Windows, Mac, or Linux)
- USB A-to-B cable (like printer cable)

**Optional**:
- External monitor for waterfall display
- Foot switch for PTT
- Ferrite chokes for RFI suppression

### Software Needed

**Driver** (REQUIRED FIRST):
- ICOM USB driver from icomamerica.com/support

**Digital Mode Programs**:
- WSJT-X (FT8, FT4, WSPR, JT65, JT9)
- Fldigi (PSK31, RTTY, many others)
- JS8Call (JS8 mode)
- Winlink (Email over radio)

**Support Software**:
- Meinberg NTP (Windows time sync)
- Virtual Audio Cable (advanced setups)
- Logging software (HRD, Log4OM, N1MM+)

---

## IC-7300 Configuration for Digital Modes

### USB Driver Installation

⚠️ **Critical**: Install the driver BEFORE connecting the USB cable!

**Windows**:
1. Download from [ICOM website](https://www.icomamerica.com/support)
2. Run installer as Administrator
3. Follow prompts, accept defaults
4. Restart if prompted
5. NOW connect USB cable
6. Check Device Manager for COM port

**Linux**:
- Driver usually built into kernel (cp210x)
- May need to add user to dialout group:
  ```bash
  sudo usermod -a -G dialout $USER
  ```
- Log out and back in

**Mac**:
- Download Silicon Labs driver from ICOM website
- Install and restart
- Connect USB cable

### Radio Menu Settings

Navigate to **MENU** > **SET** > **Connectors**:

| Setting | Value | Purpose |
|---------|-------|---------|
| ACC/USB AF SQL | OFF (Open) | Continuous audio output |
| ACC/USB Output Level | 50% | Audio to computer (adjust as needed) |
| ACC/USB AF Beep/Speech | OFF | Prevent tones in recordings |
| ACC/USB IF Output Level | 50% | IF output level |
| USB MOD Level | 40-50% | Audio from computer |
| DATA OFF MOD | MIC,ACC | Mic source when not in data mode |
| DATA MOD | USB | Use USB audio for data modes |

Navigate to **CI-V** section:

| Setting | Value | Purpose |
|---------|-------|---------|
| CI-V USB Baud Rate | 115200 | Fast communication |
| CI-V USB Echo Back | ON | Required for most software |
| CI-V USB Port | Unlink from [REMOTE] | Separate USB control |

### Operating Mode Settings

For digital modes, use USB-D:

1. Press **SSB** button until **USB** is displayed
2. Touch **DATA** on screen
3. Display shows **USB-D**

**Filter Settings**:
1. Press **FILTER**
2. Select **FIL1** (typically 3.0-3.6 kHz)
3. This allows seeing more signals on waterfall

**Function Settings**:
1. Press **FUNCTION**
2. Turn OFF: **NB**, **NR**, **NOTCH**
3. Set **AGC** to FAST (or OFF for FT8)

---

## Audio Configuration

### Windows Audio Settings

1. Open **Sound Settings** (right-click speaker icon)
2. Find **USB Audio CODEC** in Playback devices
3. Set as default for digital mode software
4. Properties > Advanced: **48000 Hz, 1 channel, 16-bit**
5. Properties > Enhancements: **Disable all**

For recording device:
1. Find **USB Audio CODEC** in Recording devices
2. Properties > Advanced: **48000 Hz, 1 channel, 16-bit**

💡 **Tip**: Rename the devices to "IC-7300" for easy identification.

### Linux Audio Settings

Using PulseAudio/PipeWire:
1. Open sound settings (pavucontrol)
2. Find "USB Audio CODEC"
3. Set sample rate to 48000 Hz

Using ALSA directly:
```bash
# Find the device
aplay -l
# Note the card and device numbers
# Configure in .asoundrc if needed
```

---

## CAT Control Setup

CAT (Computer Aided Transceiver) control allows software to:
- Read/set frequency
- Change modes
- Key the transmitter
- Monitor status

### Finding Your COM Port

**Windows**:
1. Open Device Manager
2. Expand "Ports (COM & LPT)"
3. Find "Silicon Labs CP210x USB to UART Bridge"
4. Note the COM number (e.g., COM3)

**Linux**:
```bash
ls /dev/ttyUSB*
# Usually /dev/ttyUSB0 for IC-7300
```

**Mac**:
```bash
ls /dev/tty.SLAB*
# Usually /dev/tty.SLAB_USBtoUART
```

### Standard CAT Settings

Most software uses these settings:

| Parameter | Value |
|-----------|-------|
| Baud Rate | 115200 |
| Data Bits | 8 |
| Stop Bits | 1 |
| Parity | None |
| Handshake | None |
| CI-V Address | 94h (default) |

---

## Time Synchronization

Digital modes (especially FT8) require accurate computer time.

### Windows: Meinberg NTP

1. Download from [meinbergglobal.com](https://www.meinbergglobal.com/english/sw/ntp.htm)
2. Install with default options
3. Service starts automatically
4. Syncs to pool.ntp.org servers

### Linux: systemd-timesyncd

Most modern distros sync automatically:
```bash
# Check status
timedatectl status
# Should show "System clock synchronized: yes"
```

### Mac: Built-in

1. System Preferences > Date & Time
2. Check "Set date and time automatically"
3. Select appropriate server

### Verifying Time Accuracy

In WSJT-X, the **DT** column shows time offset:
- Values should be close to 0.0
- ±0.5 is acceptable
- ±1.0 or more indicates sync problems

---

## Power Settings for Digital Modes

Digital modes use constant carrier during transmission, which causes more heat than voice modes.

### Recommended Power Levels

| Mode | Recommended Power | Maximum Safe |
|------|-------------------|--------------|
| FT8/FT4 | 25-50W | 75W |
| PSK31 | 25-40W | 50W |
| RTTY | 30-50W | 75W |
| WSPR | 5W | 10W |

### ALC Settings

**Critical**: Keep ALC meter showing minimal or no movement!

High ALC causes:
- Splatter (interference to adjacent signals)
- Distortion
- Reduced communication effectiveness

**Proper ALC adjustment**:
1. Set radio power to 100%
2. In software, find power/audio slider
3. Start transmitting (use TUNE function)
4. Adjust software audio until ALC barely moves
5. Reduce slightly more for safety margin

---

## Troubleshooting Common Issues

### No Audio to Computer

1. Check USB cable is connected
2. Verify USB Audio CODEC appears in sound settings
3. Check ACC/USB Output Level (increase if needed)
4. Ensure DATA mode is active (USB-D)

### No Audio from Computer (No TX)

1. Verify DATA MOD is set to USB
2. Check USB MOD Level setting
3. Confirm software is outputting to USB Audio CODEC
4. Check PTT is keying the radio

### CAT Control Not Working

1. Verify correct COM port
2. Check baud rate matches (115200)
3. Ensure CI-V USB Echo Back is ON
4. Try "Test CAT" button in software
5. Close other programs that might use the port

### High ALC / Distorted Signal

1. Reduce audio drive in software
2. Lower USB MOD Level in radio
3. Check for audio processing enabled in Windows
4. Ensure AGC is set to FAST or OFF

### RF Interference (RFI)

Symptoms: Computer freezes, USB disconnects, strange audio

Solutions:
1. Add ferrite chokes to USB cable (near radio end)
2. Reduce power
3. Improve station grounding
4. Use shorter USB cable
5. Add ferrites to other cables

---

## Quick Start Checklist

Before first digital mode operation:

- [ ] USB driver installed
- [ ] USB cable connected
- [ ] COM port identified
- [ ] Radio settings configured (Connectors menu)
- [ ] Mode set to USB-D
- [ ] Time synchronized
- [ ] Software installed and configured
- [ ] CAT control tested
- [ ] Audio levels set properly
- [ ] ALC not showing on transmit

---

*Continue to [WSJT-X / FT8](08_wsjt_ft8.md) for detailed FT8 setup instructions, or [Fldigi Setup](09_fldigi_setup.md) for PSK31 and RTTY.*
