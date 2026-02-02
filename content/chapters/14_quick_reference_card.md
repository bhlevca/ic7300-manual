# Quick Reference Card

One-page summaries for rapid lookup during operation.

---

## Essential Controls at a Glance

### Power-On Checklist

1. ☐ Antenna connected
2. ☐ Power supply on (13.8V)
3. ☐ Power cable connected
4. ☐ Hold POWER 1 second
5. ☐ Check band conditions
6. ☐ Tune antenna if needed

### Before Transmitting

1. ☐ Band is open and appropriate
2. ☐ Frequency is clear (listen first!)
3. ☐ Mode is correct (USB/LSB/CW/etc.)
4. ☐ Power level appropriate
5. ☐ SWR is acceptable (<2:1) — See: [SWR Tuning (How‑to)](../howtos/swr_tuning.md)
6. ☐ ALC not peaking (just touching)

---

## Control Quick Reference

### Main Dial & Tuning

| Control         | Function               |
| --------------- | ---------------------- |
| Main Dial       | Tune frequency         |
| Push Main Dial  | Multi options          |
| Touch frequency | Direct frequency entry |
| Touch spectrum  | Jump to signal         |

### MULTI Knob Functions (Context Sensitive)

| Mode | Available Functions                |
| ---- | ---------------------------------- |
| SSB  | RF Power, Mic Gain, VOX Gain/Delay |
| CW   | RF Power, Key Speed, Sidetone      |
| FM   | RF Power, Mic Gain                 |
| Any  | Hold MULTI to lock                 |

### Essential Buttons

| Button    | Tap            | Hold           |
| --------- | -------------- | -------------- |
| POWER     | -              | On/Off         |
| TUNER     | Enable/Disable | Start tune     |
| VOX/BK-IN | Toggle VOX     | CW Break-in    |
| MENU      | Open menu      | -              |
| QUICK     | Quick settings | -              |
| EXIT      | Go back        | Return to main |

---

## Mode Selection

| Button Press | 1st Press | 2nd Press | With DATA   |
| ------------ | --------- | --------- | ----------- |
| SSB          | USB       | LSB       | USB-D/LSB-D |
| CW           | CW        | CW-R      | -           |
| AM           | AM        | -         | AM-D        |
| FM           | FM        | -         | FM-D        |
| RTTY         | RTTY      | RTTY-R    | -           |

**Convention:** LSB below 10 MHz, USB at/above 10 MHz

---

## Common Frequencies

### SSB Calling Frequencies

| Band | LSB       | USB        |
| ---- | --------- | ---------- |
| 80m  | 3.885 MHz | -          |
| 40m  | 7.185 MHz | -          |
| 20m  | -         | 14.300 MHz |
| 15m  | -         | 21.300 MHz |
| 10m  | -         | 28.400 MHz |

### FT8 Frequencies (Most Popular)

| Band | Frequency | Band | Frequency |
| ---- | --------- | ---- | --------- |
| 80m  | 3.573     | 17m  | 18.100    |
| 40m  | 7.074     | 15m  | 21.074    |
| 30m  | 10.136    | 12m  | 24.915    |
| 20m  | 14.074    | 10m  | 28.074    |

### CW Calling

| Band | Freq   | Band | Freq   |
| ---- | ------ | ---- | ------ |
| 80m  | 3.560  | 15m  | 21.060 |
| 40m  | 7.030  | 12m  | 24.900 |
| 20m  | 14.060 | 10m  | 28.060 |

---

## Signal Reports

### RST System (CW/Digital)

| R (Readability)              | S (Strength) | T (Tone)       |
| ---------------------------- | ------------ | -------------- |
| 1 = Unreadable               | 1 = Faint    | 1 = Very rough |
| 3 = Readable with difficulty | 4-5 = Weak   | 5 = Chirpy     |
| 5 = Perfectly readable       | 7-8 = Good   | 9 = Perfect    |

### S-Meter Readings

| S-Unit  | dBm  | μV (50Ω) |
| ------- | ---- | -------- |
| S1      | -121 | 0.2      |
| S3      | -109 | 0.8      |
| S5      | -97  | 3.2      |
| S7      | -85  | 12.6     |
| S9      | -73  | 50       |
| S9+10dB | -63  | 158      |
| S9+20dB | -53  | 500      |

---

## Menu Navigation Quick Paths

### Digital Modes Setup
MENU → SET → Connectors → USB MOD Level, DATA MOD

### Display Brightness
MENU → SET → Display → LCD Brightness

### Reset to Factory
MENU → SET → Others → Reset → All Reset

### Save Settings to SD Card
MENU → SET → SD Card → Save Setting

### CW Settings
MENU → SET → Function → CW Settings

### AGC Settings
MENU → SET → Function → AGC Time Constant

---

## DSP Functions

### Noise Reduction

| Control  | Range       | Best For              |
| -------- | ----------- | --------------------- |
| NR Level | 1-15        | 4-8 typical           |
| NB Level | 1-10        | 5-7 for ignition      |
| Notch    | Auto/Manual | Carriers, heterodynes |

### Filter Bandwidth Suggestions

| Mode | Bandwidth | Use Case          |
| ---- | --------- | ----------------- |
| SSB  | 2.4 kHz   | Normal            |
| SSB  | 1.8 kHz   | Crowded band      |
| CW   | 500 Hz    | Normal            |
| CW   | 250 Hz    | Contest/QRM       |
| FT8  | 3.0 kHz   | See full range    |
| AM   | 9.0 kHz   | Broadcast quality |

---

## Tuner Quick Reference

### Auto-Tune Procedure

1. Set power to 10-50W
2. Touch frequency within band
3. Hold TUNER 1 second
4. Wait for "TUNE" to stop blinking
5. SWR should show <2:1

### Tuner Indicators

| Display          | Meaning                |
| ---------------- | ---------------------- |
| TUNE steady      | Tuner engaged, matched |
| TUNE blinking    | Tuning in progress     |
| No TUNE          | Tuner bypassed         |
| High SWR warning | Check antenna          |

---

## VFO Operations

| Action                | Method                      |
| --------------------- | --------------------------- |
| Switch A↔B            | Press A/B button            |
| Copy A→B              | Hold A/B 1 second           |
| Split operation       | Press SPLIT                 |
| RIT (receive offset)  | Press RIT, use RIT/XIT knob |
| XIT (transmit offset) | Press XIT, use RIT/XIT knob |

---

## Memory Operations

| Task            | Steps                                          |
| --------------- | ---------------------------------------------- |
| Store frequency | Set freq → Hold MW → Select channel → Touch MW |
| Recall memory   | Press VFO/MEMO → Turn dial or touch            |
| Edit memory     | Recall → Edit → Hold MW                        |

---

## Touch Screen Areas

| Touch Location    | Result               |
| ----------------- | -------------------- |
| Frequency display | Direct entry keypad  |
| Mode indicator    | Mode popup menu      |
| S-meter           | Change meter display |
| Waterfall signal  | Jump to frequency    |
| VFO indicator     | Switch VFO A/B       |
| Filter display    | Adjust bandwidth     |

---

## Troubleshooting Quick Checks

| Problem         | First Check           | Second Check      |
| --------------- | --------------------- | ----------------- |
| No power        | 13.8V present?        | Fuse OK?          |
| No receive      | Volume up?            | Squelch open?     |
| No transmit     | PTT connected?        | ALC normal?       |
| High SWR        | Antenna connected?    | Correct band?     |
| No audio to PC  | USB MOD Level?        | Cable secure?     |
| OVF indicator   | Strong signals nearby | Enable ATT        |
| Noisy reception | NR enabled?           | NB if pulse noise |

---

## Emergency Reference

### RF Burn Safety
- Never touch antenna while transmitting
- Maintain safe distance from radiating elements
- High voltage present at antenna feedpoint

### Power Supply
- Operating: 13.8V DC ±15%
- Maximum: 23A during transmit
- Never exceed 15.8V

### Antenna Limits
- SWR > 3:1: Reduce power
- No antenna connected: Do not transmit
- Use dummy load for testing

---

## Phonetic Alphabet Quick Reference

| A-I     | J-R      | S-Z     |
| ------- | -------- | ------- |
| Alpha   | Juliet   | Sierra  |
| Bravo   | Kilo     | Tango   |
| Charlie | Lima     | Uniform |
| Delta   | Mike     | Victor  |
| Echo    | November | Whiskey |
| Foxtrot | Oscar    | X-ray   |
| Golf    | Papa     | Yankee  |
| Hotel   | Quebec   | Zulu    |
| India   | Romeo    |         |

---

## Essential Q-Codes

| Code | Meaning               |
| ---- | --------------------- |
| QRL? | Is frequency in use?  |
| QRM  | Man-made interference |
| QRN  | Natural static        |
| QRZ? | Who is calling?       |
| QSB  | Signal fading         |
| QSL  | I acknowledge         |
| QSO  | Contact               |
| QSY  | Change frequency      |
| QTH  | Location              |
| 73   | Best regards          |
