# IC-7300 Menu Tree Reference

Complete navigation structure of the IC-7300 menu system.

## Main Menu Structure

Press **MENU** to access:

```
MENU
├── SET
│   ├── Tone Control
│   │   ├── SSB-T (TX)
│   │   ├── SSB-R (RX)
│   │   ├── AM (RX)
│   │   └── FM (RX)
│   ├── Function
│   │   ├── AGC Time Constant
│   │   ├── MIC Gain
│   │   ├── Monitor
│   │   ├── VOX
│   │   ├── CW Settings
│   │   ├── RTTY Settings
│   │   └── Speech Settings
│   ├── Connectors
│   │   ├── ACC/USB Settings
│   │   ├── DATA MOD
│   │   └── CI-V Settings
│   ├── Display
│   │   ├── LCD Brightness
│   │   ├── Display Type
│   │   └── Screen Saver
│   ├── Time Set
│   │   └── Date/Time
│   ├── SD Card
│   │   ├── Save/Load Settings
│   │   └── Screen Capture
│   └── Others
│       ├── Beep Settings
│       ├── Reset
│       └── Information
├── VOICE
│   ├── RX Record
│   ├── TX Record
│   └── Play
├── KEYER
│   ├── CW Memory
│   └── RTTY Memory
├── SCOPE
│   ├── Scope Settings
│   ├── Audio Scope
│   └── SWR Plot
├── SCAN
│   ├── Program Scan
│   ├── Memory Scan
│   └── Select Memory Scan

See also: [How‑to: Scan for broadcasts](../howtos/scan_for_broadcasts.md)

└── OTHER
    ├── DR (Direct Recall)
    ├── Auto Notch
    ├── Manual Notch
    └── Noise Reduction
```

---

## SET > Connectors (Digital Mode Settings)

```
Connectors
├── ACC/USB AF SQL ............. OFF (Open) / AUTO
├── ACC/USB Output Level ....... 0-100%
├── ACC/USB AF Beep/Speech ..... OFF / ON
├── ACC/USB IF Output Level .... 0-100%
├── USB MOD Level .............. 0-100%
├── DATA OFF MOD ............... MIC / ACC / MIC,ACC
├── DATA MOD ................... MIC / USB / ACC / MIC,ACC
├── REF Adjust ................. Calibration
└── CI-V
    ├── CI-V Baud Rate ......... 300-19200
    ├── CI-V Address ........... 00-7F (Default: 94)
    ├── CI-V Transceive ........ ON / OFF
    ├── CI-V USB Port .......... Unlink / Link to [REMOTE]
    ├── CI-V USB Baud Rate ..... Auto / 4800-115200
    └── CI-V USB Echo Back ..... ON / OFF
```

---

## SET > Function (Operating Settings)

```
Function
├── Beep Level ................. 0-100%
├── Beep (Confirmation) ........ ON / OFF
├── Band Edge Beep ............. OFF / ON
├── RF/SQL Control ............. RF+SQL / AUTO
├── AM/FM Dial Step ............ Various
├── SSB/CW Dial Step ........... Various
├── Screen Capture ............. File type settings
├── Quick RIT/ΔTX Clear ........ OFF / ON
├── SPEECH Level ............... 0-100%
├── SPEECH Speed ............... Slow / Normal / Fast
├── [SSB] TX Tone .............. Wide / Mid / Narrow
├── [SSB] TX BW ................ Wide / Mid / Narrow
├── SSB Mic Gain ............... 0-100%
├── [AM] TX Tone ............... Wide / Mid / Narrow
├── [FM] TX Tone ............... Wide / Mid / Narrow
├── FM Mic Gain ................ 0-100%
└── Monitor Settings
```

---

## SET > CW Settings

```
CW Settings
├── CW Key Type ................ Straight / Bug / Paddle
├── CW Key Speed ............... 6-60 WPM
├── CW Sidetone ................ 300-900 Hz
├── CW Pitch ................... 300-900 Hz
├── CW Break-in ................ Semi / Full
├── CW Delay ................... 2.0-13.0 dot
├── CW Paddle Polarity ......... Normal / Reverse
├── CW Rise Time ............... 2/4/6/8 ms
└── QSK Delay Time ............. 2.0-13.0 dot
```

---

## SCOPE Settings

```
SCOPE SET
├── Scope ON/OFF ............... ON / OFF
├── During TX (CENTER Type) .... ON / OFF
├── Max Hold ................... OFF / 1-30 sec / Continuous
├── CENTER Type Display ........ Filter Center / Carrier Center
├── Averaging .................. OFF / 2-4 sweeps
├── Video BW ................... Narrow / Wide
├── Waveform Type .............. Fill / Fill + Line
├── Waveform Color ............. Current / Line colors
├── Waterfall Display .......... OFF / ON
├── Waterfall Speed ............ Slow / Mid / Fast
├── Waterfall Size ............. Small / Mid / Large
├── Waterfall Peak Color ....... RGB values
├── Waterfall Marker ........... OFF / ON / Auto Hide
└── Fixed Edges ................ Band segment definitions
```

---

## Quick Access to Common Settings

| Setting | Navigation Path |
|---------|-----------------|
| USB MOD Level | MENU > SET > Connectors |
| DATA MOD | MENU > SET > Connectors |
| CI-V Baud Rate | MENU > SET > Connectors > CI-V |
| Time/Date | MENU > SET > Time Set |
| CW Key Speed | MENU > SET > Function (CW section) |
| MIC Gain | FUNCTION button > press repeatedly |
| NR Level | FUNCTION button > NR |
| VOX Settings | QUICK button (in SSB mode) |
| Reset | MENU > SET > Others > Reset |
| Firmware Version | MENU > SET > Others > Information |

---

## Reset Options

```
MENU > SET > Others > Reset
├── Partial Reset .............. Resets some settings
├── All Reset .................. Factory defaults (all)
└── Tuner Reset ................ Clears tuner memories
```

⚠️ **Warning**: All Reset erases all customizations and memories!

---

## SD Card Operations

```
MENU > SET > SD Card
├── Save Setting ............... Save to SD card
├── Load Setting ............... Load from SD card
├── Save Config to Preset ...... Named presets
├── Load Config from Preset .... Load named preset
├── SD Card Info ............... Card capacity/usage
└── Unmount .................... Safe removal
```

---

*Refer to the ICOM Full Manual for complete details on each setting.*
