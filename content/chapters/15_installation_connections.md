# Installation & Connections

Proper installation is critical for safe and optimal operation of your IC-7300. This chapter covers everything from unpacking to making your first transmission-ready connection.

---

## 📦 What's in the Box

Your IC-7300 package should include:

| Item                   | Quantity | Notes                                |
| ---------------------- | -------- | ------------------------------------ |
| IC-7300 Transceiver    | 1        | The radio itself                     |
| HM-219 Hand Microphone | 1        | With UP/DOWN buttons                 |
| DC Power Cable         | 1        | Fused (20A), with Anderson connector |
| Spare Fuses            | 2        | 20A blade type                       |
| USB Cable              | 1        | Type A to Type B                     |
| Plugs/Covers           | Various  | For unused connectors                |
| Manual & Warranty      | 1 set    | Keep for reference                   |

> **Missing something?** Contact ICOM support or your dealer immediately.

---

## 🔧 Pre-Installation Planning

### Location Considerations

Choose a location that provides:

- **Adequate ventilation**: The IC-7300 generates heat during transmit. Leave at least 10cm (4") on all sides.
- **Stable surface**: The radio weighs 4.2kg (9.3 lbs). Ensure your desk can support it.
- **Easy access**: You'll frequently use the touch screen and controls.
- **Low RF noise**: Away from switching power supplies, computers, LED lights.

### Required Accessories (Not Included)

| Item              | Specification                | Why You Need It            |
| ----------------- | ---------------------------- | -------------------------- |
| **Power Supply**  | 13.8V DC, 30A continuous     | Powers the radio           |
| **Antenna**       | 50Ω, rated for 100W+         | For transmitting/receiving |
| **Coax Cable**    | RG-8, LMR-400, or equivalent | Connects antenna to radio  |
| **Ground Wire**   | #10 AWG or heavier           | RFI reduction, safety      |
| **Antenna Tuner** | Optional, 50Ω                | If antenna SWR > 1.5:1     |

---

## ⚡ DC Power Connection

The IC-7300 requires **13.8V DC** (acceptable range: 11.7V - 15.6V).

### Power Supply Selection

**Minimum specifications:**
- Output: 13.8V DC regulated
- Current: 23A minimum (30A recommended)
- Regulation: ±5% under load
- Ripple: < 100mV peak-to-peak

**Recommended supplies:**
- Samlex SEC-1235M (30A switching, very clean)
- Astron RS-35M (35A linear, bulletproof reliability)
- MFJ-4230MVP (30A switching, popular choice)

### Connection Procedure

1. **Power OFF the supply** before connecting
2. Verify polarity: **RED = Positive (+)**, **BLACK = Negative (-)**
3. Connect the radio's DC cable to the supply:
   - Red wire → Positive (+) terminal
   - Black wire → Negative (-) terminal
4. **DO NOT** remove the inline fuses from the cable
5. Verify connections are tight (loose connections cause voltage drop)

```
┌─────────────────┐     ┌──────────────┐
│  Power Supply   │     │   IC-7300    │
│                 │     │              │
│  [+] ════════════════► DC INPUT     │
│                 │     │              │
│  [-] ════════════════► (GND)        │
│                 │     │              │
│  [GND]          │     │  [GND]       │
└───────┬─────────┘     └──────┬───────┘
        │                      │
        └───────► EARTH ◄──────┘
                GROUND
```

> ⚠️ **WARNING**: Reverse polarity WILL damage the radio. Double-check before powering on!

### Wire Gauge Requirements

| Cable Length   | Minimum Wire Gauge |
| -------------- | ------------------ |
| Up to 1m (3ft) | 14 AWG             |
| 1-2m (3-6ft)   | 12 AWG             |
| 2-3m (6-10ft)  | 10 AWG             |
| Over 3m        | Not recommended    |

---

## 📡 Antenna Connection

### Main Antenna Port

The IC-7300 has a single antenna connector on the rear panel:
- **Type**: SO-239 (accepts PL-259 connector)
- **Impedance**: 50Ω unbalanced
- **Power handling**: 100W continuous

**Connection steps:**
1. Inspect the PL-259 connector for damage
2. Hand-tighten the connector (don't over-torque)
3. Ensure the center pin makes contact
4. Route coax away from power cables (reduces RFI)

### Coax Cable Selection

| Cable Type | Loss at 30MHz (per 100ft) | Best Use            |
| ---------- | ------------------------- | ------------------- |
| RG-8X      | 2.0 dB                    | Short runs (<50ft)  |
| RG-8       | 1.3 dB                    | Medium runs         |
| LMR-400    | 0.7 dB                    | Long runs, low loss |
| Hardline   | 0.3 dB                    | Tower installations |

### Antenna Recommendations by Band

| Band | Good Options                   |
| ---- | ------------------------------ |
| 160m | Inverted L, full-size vertical |
| 80m  | Dipole, inverted V, vertical   |
| 40m  | Dipole, vertical, EFHW         |
| 20m  | Dipole, beam, vertical         |
| 15m  | Beam, vertical, dipole         |
| 10m  | Beam, vertical                 |
| 6m   | Beam, vertical, dipole         |

> 🔗 **See also**: [Antenna & SWR](06_antenna_swr.md) for tuning and matching.

---

## 🌍 Grounding

Proper grounding reduces RFI, prevents shocks, and improves receive performance.

### Station Ground

Connect the radio's **GND** terminal to:
1. A dedicated ground rod (8ft copper, driven into earth)
2. Use #10 AWG (or heavier) wire
3. Keep the ground wire as SHORT as possible
4. Bond multiple grounds together to prevent ground loops

```
┌─────────────┐   #10 AWG    ┌──────────┐
│  IC-7300    ├──────────────►│ Ground   │
│  GND        │  < 6ft ideal │ Rod      │
└─────────────┘              └──────────┘
                                  │
┌─────────────┐                   │
│  Power      ├───────────────────┘
│  Supply GND │   Bond all grounds
└─────────────┘   together!
```

### Safety Ground (AC)

The power supply should be plugged into a grounded (3-prong) outlet. This provides:
- Chassis safety ground
- Surge protection path
- Equipment protection

> ⚠️ **Never defeat the safety ground** by using a 3-to-2 adapter.

---

## 🔌 USB Connection

The USB port provides **three functions** in one cable:
1. **CAT Control** (CI-V protocol for computer control)
2. **Audio Output** (for digital modes, recording)
3. **Audio Input** (for digital modes, voice keyer)

### Driver Installation

**Windows 10/11**: Drivers install automatically via Windows Update.

**If manual installation needed:**
1. Download "Silicon Labs CP210x" driver from ICOM support
2. Install before connecting the radio
3. Reboot if prompted

### USB Audio Setup

The IC-7300 appears as two audio devices:
- **USB Audio CODEC** (Speaker) - Output from radio
- **USB Audio CODEC** (Microphone) - Input to radio

**Windows settings:**
1. Right-click speaker icon → Sound Settings
2. Set USB Audio CODEC as **default for output** (if using digital modes)
3. Or configure per-application in your logging/digital software

### CI-V Settings

Configure in: **MENU** → **SET** → **Connectors** → **CI-V**

| Setting            | Recommended Value                 |
| ------------------ | --------------------------------- |
| CI-V Baud Rate     | 19200 (reliable) or 115200 (fast) |
| CI-V Address       | 94h (default for IC-7300)         |
| CI-V Transceive    | ON (for real-time freq updates)   |
| CI-V USB Port      | Unlink from [REMOTE]              |
| CI-V USB Baud Rate | Auto                              |
| CI-V USB Echo Back | OFF                               |

> 🔗 **See also**: [Digital Modes Overview](07_digital_modes.md) for software configuration.

---

## 🎤 Microphone Connection

The IC-7300 uses an **8-pin round connector** for the microphone.

### HM-219 Hand Microphone

The included HM-219 provides:
- PTT switch
- UP/DOWN buttons (for tuning or memory channels)
- Electret condenser element

**Connection:**
1. Align the notch on the plug with the connector
2. Push in firmly until it clicks
3. Do not force - it should slide in smoothly

### Other Compatible Microphones

| Microphone  | Type     | Notes                |
| ----------- | -------- | -------------------- |
| HM-219      | Hand mic | Included with radio  |
| SM-30       | Desktop  | Great for ragchewing |
| SM-50       | Desktop  | Premium option       |
| Heil PR-781 | Studio   | Needs adapter cable  |
| Any dynamic | Various  | Check wiring diagram |

### Microphone Wiring (8-pin connector)

| Pin | Function       | Wire Color (HM-219) |
| --- | -------------- | ------------------- |
| 1   | MIC audio      | Shielded wire       |
| 2   | 8V output      | -                   |
| 3   | PTT            | White               |
| 4   | MIC ground     | Shield              |
| 5   | UP             | Yellow              |
| 6   | DOWN           | Green               |
| 7   | +8V output     | -                   |
| 8   | SQL (not used) | -                   |

---

## 🔗 ACC Socket Connection

The **13-pin DIN ACC socket** provides:

| Pin | Function | Common Use            |
| --- | -------- | --------------------- |
| 1   | GND      | Ground reference      |
| 2   | SEND     | PTT output to amp     |
| 3   | MOD      | AF input (1-2V RMS)   |
| 4   | AF OUT   | Fixed audio output    |
| 5   | RTTY/PSK | Keying line           |
| 6   | BAND     | Band voltage output   |
| 7   | +8V      | Accessory power       |
| 8   | ALC      | ALC input from amp    |
| 11  | SEND     | PTT output            |
| 12  | AF OUT   | Adjustable audio out  |
| 13  | +13.8V   | Power output (1A max) |

### Common ACC Connections

**Linear Amplifier:**
- Connect SEND (pin 2 or 11) to amplifier PTT
- Connect ALC (pin 8) if amplifier provides ALC
- Connect BAND (pin 6) for automatic band switching

**External TNC/Sound Card:**
- Connect MOD (pin 3) for TX audio input
- Connect AF OUT (pin 4 or 12) for RX audio output
- Connect SEND for PTT control

---

## ⌨️ External Keyer/Paddle (CW)

Connect paddles or a straight key to the **KEY jack** (3.5mm stereo).

### Wiring

| Connector | Function                 |
| --------- | ------------------------ |
| Tip       | Dot (paddle) or Key line |
| Ring      | Dash (paddle)            |
| Sleeve    | Ground                   |

### Configuration

**MENU** → **SET** → **Function** → **CW-KEY SET**

| Setting   | Options                         |
| --------- | ------------------------------- |
| Key Type  | PADDLE, BUG, ELEC-KEY, STRAIGHT |
| Dot/Dash  | Normal or Reverse               |
| Key Speed | 6-60 WPM                        |

---

## 🏁 Final Checklist

Before powering on for the first time:

- [ ] DC power connected with correct polarity
- [ ] Antenna connected (or dummy load for testing)
- [ ] Ground wire connected
- [ ] Microphone plugged in
- [ ] All connections tight
- [ ] Ventilation adequate
- [ ] Power supply OFF

**First power-on:**
1. Turn ON the power supply
2. Hold the IC-7300 POWER button for 1 second
3. Verify voltage display shows ~13.8V
4. Listen for fan (runs only when needed)
5. Check that touch screen responds

🎉 **Congratulations!** Your IC-7300 is ready for initial configuration.

> 🔗 **Next step**: [Basic Operations](04_basic_operations.md) to make your first QSO!

---

## 💡 Real-Life Installation Tips

### From Experienced Operators

**Power supply placement:**
> "I keep my power supply on the floor, away from the radio. This keeps switching noise away from the receiver and provides better airflow."

**Cable management:**
> "Use ferrite chokes on USB and power cables where they enter the radio. Even good cables can pick up stray RF."

**Testing without antenna:**
> "Always use a dummy load for initial testing. I've seen operators damage finals by testing into an open connector."

**Ground loop prevention:**
> "My power supply ground, radio ground, and computer ground all connect to ONE point - my station ground bus. No loops, no hum."

### Common Installation Mistakes

1. **Inadequate power supply**: A 20A supply will work... until you transmit at full power for a few minutes
2. **Long DC cables**: Voltage drop causes problems - keep cables SHORT
3. **No RF ground**: Results in RF in the shack, hot microphones, erratic behavior
4. **USB ground loops**: Use USB isolators if you get digital mode hum
