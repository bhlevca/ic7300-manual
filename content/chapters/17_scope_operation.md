# Spectrum Scope Operation

The IC-7300's real-time spectrum scope is one of its most powerful features. This chapter teaches you how to master this tool for finding signals, analyzing band conditions, and improving your operating.

---

## 🎯 What Makes the IC-7300 Scope Special

Unlike older radios that use audio-based bandscopes, the IC-7300's scope works **directly on RF**:

- **Real-time display** of the band (no scanning delay)
- **1 MHz+ span** shows the entire band at once
- **Waterfall history** reveals signal patterns over time
- **Touch to tune** - tap any signal to hear it

This is possible because of the **direct-sampling SDR** architecture - the same ADC that creates your audio also feeds the spectrum display.

---

## 📊 Scope Display Elements

```
┌────────────────────────────────────────────────┐
│  ┌──Spectrum──────────────────────────────┐   │
│  │    ╱╲      ╱╲                          │   │
│  │   ╱  ╲    ╱  ╲    ╱╲                   │   │
│  │  ╱    ╲──╱    ╲──╱  ╲──────────────────│   │
│  └────────────────────────────────────────┘   │
│  ┌──Waterfall─────────────────────────────┐   │
│  │▓▓░░▓▓░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░│   │
│  │▓▓░░▓▓░░░░▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░│   │
│  │▓▓░░▓░░░░░▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░│   │
│  │▓░░░▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│   │
│  └────────────────────────────────────────┘   │
│  14.000 ────── 14.074 ────────── 14.350 MHz   │
└────────────────────────────────────────────────┘
```

### Spectrum (Top)

- **Vertical axis**: Signal strength (higher = stronger)
- **Horizontal axis**: Frequency
- **Center marker**: Current tuned frequency
- **Filter passband**: Shows as shaded area

### Waterfall (Bottom)

- **Horizontal axis**: Frequency
- **Vertical axis**: Time (newest at top)
- **Color intensity**: Signal strength
- **Patterns**: Reveal signal characteristics

---

## 🔧 Scope Settings

Press **M.SCOPE** button or touch the scope display to access settings.

### Display Modes

| Mode | Description | Best For |
|------|-------------|----------|
| **Center** | Tuned frequency in center | General operating |
| **Fixed** | Shows fixed frequency range | Band monitoring |
| **Scroll-C** | Center mode with scrolling | Scanning bands |
| **Scroll-F** | Fixed mode with scrolling | Band edge monitoring |

### Span Settings

| Span | Shows | Resolution | Use |
|------|-------|------------|-----|
| ±2.5 kHz | 5 kHz | High detail | CW, weak signals |
| ±5 kHz | 10 kHz | Good detail | SSB QSOs |
| ±10 kHz | 20 kHz | Medium | Typical operating |
| ±25 kHz | 50 kHz | Wide view | Scanning |
| ±50 kHz | 100 kHz | Very wide | Contest monitoring |
| ±100 kHz | 200 kHz | Band view | Band activity |
| ±250 kHz | 500 kHz | Segment view | Multi-band |
| ±500 kHz | 1 MHz | Maximum | Full band view |

### Speed/Reference Level

- **Speed**: How fast the scope updates (FAST/MID/SLOW)
- **Reference Level**: Vertical position adjustment
- **Scope Gain**: Amplifies weak signals on display

---

## 👆 Touch Interaction

The scope responds to various touch gestures:

### Single Touch

Touch anywhere on the spectrum or waterfall to **magnify** that area:
- Display zooms in to show detail
- Center marker moves to touched frequency
- Touch again to tune to that frequency

### Double Touch

**Immediately tunes** to the touched frequency:
- Your VFO jumps to that spot
- Audio changes to the new frequency
- Great for quickly checking signals

### Touch and Drag

**Pan** across the band:
- In Center mode: Tunes the VFO as you drag
- In Fixed mode: Scrolls the display range

### Pinch Gesture

**Zoom in/out** (if enabled):
- Spread fingers to decrease span (zoom in)
- Pinch fingers to increase span (zoom out)

> 💡 **Tip**: Enable Mini Scope in the settings for a compact display during normal operation.

---

## 🌊 Reading the Waterfall

The waterfall reveals information invisible in the spectrum alone.

### Signal Types

**CW Signal**
```
║║║║║║║║║║║
║ ║ ║ ║ ║ ║
 ║ ║ ║ ║ ║
  ║ ║ ║ ║
Dots and dashes as vertical marks
```

**SSB Voice**
```
▓▓▒▒░░▒▒▓▓
▒▒░░░░░░▒▒
░░░░░░░░░░
▓▓▒▒▓▓▒▒▓▓
Wide, varying pattern following speech
```

**FT8/Digital**
```
▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓
    ⋮
Consistent width, 15-second timing
```

**Carrier/Noise**
```
║║║║║║║║║║║
║║║║║║║║║║║
║║║║║║║║║║║
Steady, unchanging vertical line
```

### Recognizing Patterns

| Pattern | Likely Source |
|---------|---------------|
| Sharp vertical line | CW, carrier, birdie |
| Wide varying blocks | SSB voice |
| Regular blocks (15 sec) | FT8 |
| Continuous wide band | AM broadcast |
| Random speckles | Noise, static |
| Horizontal lines | Sweeping radar |
| Regular pulses | Digital beacon |

---

## ⚙️ Advanced Scope Settings

Access via **MENU** → **SET** → **Function** → **SCOPE**

### Display Configuration

| Setting | Options | Description |
|---------|---------|-------------|
| Scope During TX | ON/OFF | Show scope while transmitting |
| Waterfall Display | ON/OFF | Enable/disable waterfall |
| Waterfall Speed | SLOW/MID/FAST | Scrolling rate |
| Waterfall Size | Large/Small | Relative size |
| Spectrum Color | Multiple | Spectrum trace color |
| Waterfall Color | Multiple | Color scheme |

### Marker Settings

| Setting | Description |
|---------|-------------|
| Center Marker | Shows tuned frequency |
| Edge Frequency | Display band edges |
| Grid | Shows frequency/level grid |
| Passband Edge | Shows filter bandwidth |

### Performance Settings

| Setting | Options | Effect |
|---------|---------|--------|
| FFT Window | Hanning/Rectangular | Spectral accuracy |
| AVG | OFF/2/3/4 | Noise averaging |

---

## 🎨 Waterfall Color Schemes

Choose a scheme that works for your eyes:

| Scheme | Best For |
|--------|----------|
| **Default** | General use |
| **Blue** | Dark environments |
| **Green** | Low light |
| **Heat** | Maximum contrast |
| **Spectrum** | Rainbow style |

Experiment to find what shows weak signals best for you.

---

## 📻 Practical Scope Techniques

### Finding Activity on a Band

1. Set span to **±100 kHz** or wider
2. Watch for peaks in the spectrum
3. See activity "trails" in the waterfall
4. Touch to investigate interesting signals

### Monitoring a Specific Segment

1. Switch to **Fixed** mode
2. Set the fixed edges to your segment
3. Watch the entire segment while tuned elsewhere
4. Touch to jump to activity

### Contest Operating

1. Use **±25 to ±50 kHz** span
2. Enable **FAST** waterfall speed
3. Look for open frequencies between peaks
4. Watch calling patterns in the waterfall

### Working DX Pileups

1. Use **±10 to ±25 kHz** span
2. Watch where the DX station transmits (peak)
3. See where they're listening (their TX triggers responses)
4. Find a clear spot at the pileup edge

### CW Operating

1. Use narrow span (**±2.5 to ±5 kHz**)
2. CW signals appear as thin vertical lines
3. Waterfall shows sending rhythm (helps copy callsigns!)
4. Distinguish CW from carriers by pattern

### Digital Mode Monitoring

1. Use **±10 kHz** span centered on digital frequency
2. FT8 signals appear as regular 15-second blocks
3. Count signals to estimate band activity
4. Find clear frequency for your transmission

---

## 🔍 Interpreting What You See

### Band Conditions from the Scope

**Dead band:**
- Flat spectrum, no peaks
- Waterfall shows only noise speckles
- Occasional atmospheric burst

**Band opening:**
- Sudden appearance of peaks
- Waterfall shows new activity starting
- Signal strength increasing over time

**Crowded band:**
- Peaks everywhere
- Waterfall filled with activity
- Hard to find clear frequencies

### Identifying Interference

**Local noise:**
- Multiple equally-spaced peaks (switching noise)
- Horizontal waterfall lines (sweeping)
- Broad raised noise floor

**Propagation artifacts:**
- Multiple peaks from same station (multipath)
- Signals fading in waterfall (QSB)
- Doppler spread on HF signals

---

## 💡 Pro Tips from Experienced Operators

### Scope Optimization

> "I keep the waterfall in SLOW mode most of the time. FAST eats up screen too quickly and makes patterns harder to see."

### Finding Weak Signals

> "Turn down the reference level to see weak signals better. The scope gain can make them visible even when you can barely hear them."

### Contest Strategy

> "During contests, I use Fixed mode to watch the pileup while I'm calling. I can see exactly when a frequency opens up."

### Digital Mode Integration

> "For FT8, zoom in tight (±2.5 kHz) to see individual signals clearly. The waterfall helps you spot stations before they decode."

### Avoiding the Crowd

> "Before calling CQ, I watch the waterfall for 30 seconds. If there are faint traces where I want to operate, someone is probably using that frequency from far away."

---

## 🛠️ Troubleshooting Scope Issues

### Scope Shows Nothing

- Check that scope is enabled (MENU → SET → Display)
- Verify antenna is connected
- Try different band with known activity
- Check span isn't too narrow

### Waterfall Too Fast/Slow

- Adjust Waterfall Speed in scope settings
- SLOW for pattern recognition
- FAST for fast-changing conditions

### Signals Don't Match Audio

- Verify Center mode is selected
- Check that no RIT is enabled
- Confirm filter width matches passband display

### Scope Looks "Grainy"

- Enable AVG (averaging) to smooth display
- Reduce scope gain if over-amplifying noise
- Check FFT window setting

---

## ⌨️ Scope Quick Reference

| Action | How |
|--------|-----|
| Open scope settings | Press M.SCOPE or touch scope |
| Toggle waterfall | Long-press M.SCOPE |
| Tune to signal | Double-touch on scope |
| Zoom in | Touch to magnify, or pinch |
| Change span | MULTI knob in scope mode |
| Pan display | Touch and drag |
| Reset view | Exit and re-enter scope |

> 🔗 **Related**: [Basic Operations](04_basic_operations.md) | [Receiving & Transmitting](16_receiving_transmitting.md) | [Digital Modes](07_digital_modes.md)
