# Rear Panel Connections

The rear panel of the IC-7300 contains all the connections for antenna, power, computer interface, and accessories. Proper connection is essential for safe and effective operation.

## Panel Overview

From left to right, the rear panel includes:

- Ground terminal
- Antenna connector
- Tuner control port
- ACC socket
- USB port
- CI-V Remote jack
- External speaker jack
- Key jack
- ALC input
- DC power input

---

## Antenna Connection

### ANT Connector
**Type**: SO-239 (accepts PL-259)
**Impedance**: 50 Ω

This is your primary antenna connection.

**Installation**:
1. Use quality coaxial cable (RG-213, RG-8, LMR-400)
2. Ensure PL-259 connector is properly installed
3. Hand-tighten, then 1/4 turn more with wrench
4. Do not over-tighten!

**Recommended Cables by Distance**:

| Distance | Recommended Cable |
|----------|-------------------|
| < 50 ft (15m) | RG-8X, RG-213 |
| 50-100 ft | RG-213, LMR-400 |
| > 100 ft | LMR-400, Hardline |

💡 **Tip**: Quality coax minimizes signal loss. On 6m/2m, use low-loss cable!

### Ground Terminal (GND)
**Type**: Binding post / Screw terminal

Connect your station ground here:

- Use heavy gauge wire (#10 AWG or larger)
- Keep ground lead as short as possible
- Connect to station ground system
- Helps reduce RFI and is a safety measure

⚠️ **Warning**: This is an RF ground, not a substitute for electrical safety ground!

---

## Power Connection

### DC Power Input
**Type**: 2-pin power connector
**Voltage**: 13.8V DC ±15%
**Current**: 23A maximum (at 100W output)

**Power Requirements**:

| Mode | Current Draw |
|------|-------------|
| Receive (no signal) | ~2.0A |
| Receive (signal) | ~2.5A |
| Transmit (100W) | ~23A |
| Transmit (50W) | ~12A |

**Power Supply Selection**:
- Minimum 25A regulated supply recommended
- Switching supplies work well but may need filtering
- Linear supplies are quieter but heavier

**Connection Tips**:
1. Check polarity before connecting (center is positive)
2. Ensure connections are tight
3. Use supplied power cable (has inline fuses)
4. Replace fuses with correct rating (30A)

⚠️ **Warning**: Reverse polarity WILL damage the transceiver!

---

## Computer Interface

### USB Port
**Type**: USB Type-B (like a printer)
**Functions**: 
- CAT (Computer Aided Transceiver) control
- Audio interface (sound card)
- CI-V serial communication

The USB port is the primary computer interface for the IC-7300.

**Driver Installation** (IMPORTANT!):
1. Download driver from ICOM website FIRST
2. Install driver BEFORE connecting USB cable
3. Then connect USB cable
4. Windows will recognize the device

**What It Provides**:
- Virtual COM port for CAT control
- USB Audio CODEC for sound
- Single cable for all digital mode operation

**USB Audio Specifications**:
- Sample rate: 48 kHz
- Channels: 1 (mono)
- Bit depth: 16-bit

### CI-V REMOTE Jack
**Type**: 3.5mm stereo jack
**Function**: Alternative CI-V control connection

Use this for:
- Separate CAT control (when USB audio is used differently)
- Connection to CI-V accessories
- Multi-radio setups

**When to Use**:
- If USB is being used for audio only
- When connecting to older control software
- For RS-BA1 remote control setups

💡 **Tip**: Most users only need the USB connection. The CI-V jack is optional.

---

## Accessory Connections

### ACC Socket
**Type**: 13-pin DIN connector
**Function**: External device interface

**Pinout Reference**:

| Pin | Function |
|-----|----------|
| 1 | GND |
| 2 | RTTY keying |
| 3 | SEND (PTT out) |
| 4 | MOD (Audio in) |
| 5 | AF out |
| 6 | SQUELCH |
| 7 | +13.8V out |
| 8 | ALC |
| 9 | Reserved |
| 10 | Reserved |
| 11 | GND |
| 12 | GND |
| 13 | AF out (SQL) |

**Common Uses**:
- Linear amplifier connection (SEND signal)
- External TNC for packet
- External audio processing
- Interface to SDR panadapters

### TUNER Control Port
**Type**: 4-pin connector
**Function**: Control for AH-4/AH-2b external antenna tuners

If using an ICOM external automatic tuner:
1. Connect control cable to this port
2. Connect RF cable from tuner to ANT connector
3. The tuner will be controlled automatically

### ALC Input
**Type**: RCA jack
**Function**: ALC feedback from non-ICOM amplifiers

If using a non-ICOM linear amplifier:
1. Connect ALC output from amp to this jack
2. The IC-7300 will reduce power to prevent overdrive
3. Adjust amp settings for proper ALC action

💡 **Tip**: Not needed for ICOM amplifiers which use the ACC connection.

---

## Audio Connections

### External Speaker (EXT SP)
**Type**: 3.5mm mono jack
**Impedance**: 4-8 Ω

Connect an external speaker for:
- Better audio quality
- Increased volume
- Separate speaker for operating position

When connected:
- Internal speaker is disabled
- Volume controlled by AF knob
- Use quality speaker for best audio

**Recommended External Speakers**:
- ICOM SP-38
- Any quality 8Ω communications speaker
- Small powered speakers (with volume low)

### KEY Jack
**Type**: 3.5mm stereo jack
**Function**: CW key/paddle connection

**Compatible Keys**:
- Straight key (on tip)
- Iambic paddle (tip = dit, ring = dah)
- Bug/semi-automatic key

**Key Type Selection** (in menu):
- MENU > SET > CW > Key Type
- Options: Straight, Bug, Paddle

**Keying Settings**:
- Key speed: 6-60 WPM
- Sidetone: Adjustable pitch and volume
- Paddle polarity: Normal or reverse

---

## Connection Diagram

```
         ┌─────────────────────────────────────────────┐
         │              REAR PANEL                      │
         │                                              │
         │  GND  ANT  TUNER  ACC   USB  REMOTE  SP  KEY│
         │   │    │     │     │     │     │     │    │ │
         │   ○    ◉     ●     ●     ▬     ○     ○    ○ │
         │                                              │
         │                              ALC   DC POWER  │
         │                               ○      ══════  │
         └─────────────────────────────────────────────┘
```

---

## Connection Order

When setting up your station, connect in this order:

1. **Ground** - Station ground first
2. **DC Power** - Power supply (radio OFF)
3. **Antenna** - RF connection
4. **Accessories** - USB, key, speaker
5. **Power on** - Turn on radio last

When shutting down:

1. Power off radio
2. Disconnect accessories
3. Power supply off
4. Antenna may remain connected

---

## Troubleshooting Connections

### No Power
- Check fuse in power cable
- Verify power supply is 13.8V
- Check polarity
- Ensure connectors are tight

### No Transmit
- Check antenna connection
- Verify SWR is acceptable
- Check if protection circuit activated

### No Computer Connection
- Install USB driver before connecting
- Try different USB port
- Check COM port in Device Manager
- Verify cable is data-capable (not charge-only)

### No Audio from USB
- Select correct audio device in software
- Check USB MOD Level setting in radio
- Verify USB Audio CODEC appears in system

---

*Continue to [Basic Operations](04_basic_operations.md) to learn how to use your IC-7300 for everyday operating.*
