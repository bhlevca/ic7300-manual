# Receiving & Transmitting

This chapter covers the essential skills for effective reception and transmission with your IC-7300. Master these techniques to hear weak signals and produce clean, readable transmissions.

---

## 📻 Receiving Fundamentals

The IC-7300's direct-sampling SDR architecture provides exceptional receive performance. Understanding how to optimize it will help you hear signals others miss.

### Signal Path Overview

```
Antenna → Band-pass Filter → ADC → DSP → Audio
                                    │
                              ┌─────┴─────┐
                              │ Spectrum  │
                              │ Display   │
                              └───────────┘
```

The key advantage: **all signal processing happens in digital domain**, giving you:
- Sharp filter edges impossible with analog filters
- Noise reduction that preserves intelligibility
- Real-time spectrum visualization

---

## 🔇 Noise Reduction (NR)

The IC-7300 includes sophisticated DSP-based noise reduction that can dramatically improve readability in noisy conditions.

### Enabling Noise Reduction

**Quick method:**
1. Touch the **NR** indicator on the main screen
2. Adjust level with the **MULTI** knob

**Or use FUNCTION screen:**
1. Press **FUNCTION** button
2. Touch **NR** to toggle on/off
3. Touch and hold to adjust level

### NR Levels and Their Effects

| Level | Effect | Best For |
|-------|--------|----------|
| 1-3 | Mild, natural sound | Light background noise |
| 4-6 | Moderate reduction | Typical HF conditions |
| 7-10 | Aggressive | Heavy noise/QRM |
| 11-15 | Maximum | Extreme conditions |

> ⚠️ **Warning**: High NR levels can cause "warbling" artifacts on speech. Use the minimum level needed.

### Noise Reduction Types

Navigate to **MENU** → **SET** → **Function** → **NR**

| Setting | Description |
|---------|-------------|
| NR Level | 0-15, higher = more reduction |

**Pro tip:** Start at level 4-5 and adjust by ear. Too much NR sounds unnatural and can reduce intelligibility.

---

## 🔕 Noise Blanker (NB)

The noise blanker eliminates **impulse noise** - electrical sparks, ignition noise, and similar interference.

### How It Works

The NB detects sharp noise pulses and "blanks" them out before they reach your ears. Unlike NR, which processes continuously, NB targets specific noise spikes.

### Enabling Noise Blanker

1. Press **FUNCTION** button
2. Touch **NB** to toggle on/off
3. Touch and hold to access settings

### NB Settings

**MENU** → **SET** → **Function** → **NB**

| Setting | Range | Description |
|---------|-------|-------------|
| NB Level | 0-100 | Threshold for blanking |
| NB Depth | 1-10 | How aggressively to blank |
| NB Width | 1-100 | Duration of blanking window |

**Starting point:** Level 50, Depth 5, Width 50

**Adjustment strategy:**
1. Increase Level until noise disappears
2. Reduce Depth if audio sounds "choppy"
3. Adjust Width for different pulse widths

> 🔗 **See also**: [Troubleshooting](12_troubleshooting.md) for identifying noise sources.

---

## 🎚️ Notch Filter

The notch filter eliminates **single-frequency interference** like heterodynes, carriers, and birdies.

### Auto Notch Filter (ANF)

The IC-7300 can automatically detect and notch interfering carriers.

**To enable:**
1. Press **FUNCTION** button
2. Touch **NOTCH** to toggle on
3. Select **Auto** mode

**ANF behavior:**
- Automatically finds and tracks interfering carriers
- Works best on steady tones
- May briefly notch desired audio if it's near the interference

### Manual Notch Filter

For stubborn interference, manual notch gives you precise control:

1. Enable Notch from FUNCTION screen
2. Select **Manual** mode
3. Use **MULTI** knob to position the notch frequency
4. Adjust notch width if needed

### Notch Filter Settings

**MENU** → **SET** → **Function** → **NOTCH**

| Setting | Description |
|---------|-------------|
| SSB/CW Auto Notch | Enable ANF per mode |
| Notch Width | Narrow, Mid, Wide |
| Notch Position | Shows current notch frequency |

---

## 🔊 VOX (Voice-Activated Transmission)

VOX allows hands-free operation by automatically keying the transmitter when you speak.

### Enabling VOX

1. Press the **VOX/BK-IN** button on the front panel
2. The VOX indicator lights on the display

**Or via menu:**
MENU → SET → Function → VOX

### VOX Settings

| Setting | Range | Description |
|---------|-------|-------------|
| VOX Gain | 0-100 | Sensitivity (higher = triggers easier) |
| VOX Delay | 0-2.0 sec | Time to hold TX after voice stops |
| Anti VOX | 0-100 | Prevents speaker audio from triggering TX |

### Setting Up VOX

1. **Start with conservative settings:**
   - VOX Gain: 50
   - VOX Delay: 0.5 sec
   - Anti VOX: 50

2. **Speak at normal level** and watch the TX indicator
3. **Increase Gain** if TX doesn't trigger reliably
4. **Decrease Gain** if background noise triggers TX
5. **Adjust Delay** based on your speaking pattern

> 💡 **Tip**: For contests, use shorter delay (0.2-0.3 sec). For ragchewing, use longer delay (0.8-1.0 sec).

### Anti-VOX

Anti-VOX prevents the speaker output from triggering VOX. This is essential when:
- Using external speakers near the microphone
- Monitoring received audio during contests
- Operating in noisy environments

---

## 👂 Monitor Function

The Monitor function lets you hear your transmitted audio through the speaker or headphones. Essential for checking your audio quality.

### Enabling Monitor

1. Press **FUNCTION** button
2. Touch **MONI** to toggle on/off

### Monitor Settings

**MENU** → **SET** → **Function** → **MONITOR**

| Setting | Description |
|---------|-------------|
| MONI Level | Volume of monitored audio (0-100) |
| MONI TX Audio | What to monitor (MIC, ACC, USB) |

### Uses for Monitor Function

1. **Check microphone technique** - Are you too loud? Too soft?
2. **Verify compressor settings** - Hear the processed audio
3. **Troubleshoot audio issues** - Is the microphone working?
4. **Practice CW sending** - Hear your keying with sidetone

---

## 🔀 Split Operation

Split operation allows transmitting on a different frequency than you're receiving. Essential for working DX stations and pileups.

### When to Use Split

- **DX stations** often listen "up" (5-10 kHz higher)
- **Contest stations** may spread out pileups
- **Repeaters** with different input/output frequencies

### Quick Split Setup

1. **Tune to the DX station** on VFO A
2. Touch **A/B** to copy frequency to VFO B
3. Press **SPLIT** button (or touch on screen)
4. Touch **A ⟷ B** to switch to VFO B
5. **Tune VFO B** to your transmit frequency
6. Touch **A ⟷ B** to return to VFO A (receive)

Now you'll receive on VFO A and transmit on VFO B.

### Split Indicator

When Split is active:
- **SPLIT** appears on the display
- TX frequency shows briefly when you transmit

### Split Tips

- Listen for "listening up 5" or "up 5-10"
- Start calling at the EDGE of the pileup, not in the middle
- Watch the waterfall to see where the DX is listening
- Use QUICK SPLIT feature for preset offsets

---

## 🎯 RIT (Receiver Incremental Tuning)

RIT lets you adjust the receive frequency without changing the transmit frequency. Perfect for tracking a drifting station.

### Using RIT

1. Touch **RIT** on the display (or press RIT button)
2. Use the **MULTI** knob to adjust receive offset
3. The RIT offset appears on the display

### RIT Range

- Adjustment range: ±9.999 kHz
- Step size: Set in MENU → SET → Function → MAIN DIAL

### Clearing RIT

- Touch the RIT offset display to reset to 0
- Or touch RIT again to disable

### When to Use RIT

- Compensating for a station's frequency drift
- Fine-tuning receive without losing your transmit frequency
- Checking slightly off-frequency during nets

---

## 📉 Attenuator (ATT)

The attenuator reduces the input signal level, preventing receiver overload from strong signals.

### When to Use Attenuator

- Strong local stations cause distortion
- Cross-band interference from nearby transmitters
- S-meter pinned at maximum
- Audio sounds distorted despite low AF volume

### Enabling Attenuator

1. Touch **ATT** on the display
2. Or press **ATT** on the FUNCTION screen

### Attenuation Levels

The IC-7300 provides multiple attenuation levels:

| Level | Reduction | Use Case |
|-------|-----------|----------|
| OFF | 0 dB | Normal operation |
| 6 dB | -6 dB | Mild overload |
| 12 dB | -12 dB | Moderate overload |
| 18 dB | -18 dB | Strong signals nearby |

> ⚠️ **Note**: Using attenuation reduces sensitivity. Only use when needed.

---

## 📈 Preamplifiers (P.AMP)

The preamp boosts weak signals at the expense of increased noise floor.

### Preamp Levels

| Setting | Effect | Best For |
|---------|--------|----------|
| P.AMP OFF | Normal gain | Most conditions |
| P.AMP 1 | +10 dB gain | Weak signals, quiet bands |
| P.AMP 2 | +16 dB gain | Very weak signals, low noise |

### When to Use Preamp

**DO use preamp when:**
- Band is quiet and signals are weak
- Working stations at the noise floor
- Operating on higher bands (10m, 6m) where noise is lower

**DON'T use preamp when:**
- Band is noisy or crowded
- Strong signals present (causes intermodulation)
- On lower bands (160m, 80m) where noise floor is high

### Enabling Preamp

1. Touch **P.AMP** on the display
2. Cycle through OFF → P.AMP 1 → P.AMP 2

---

## 📡 Transmitting Fundamentals

Clean transmission is courtesy to other operators. The IC-7300 provides tools to ensure your signal is readable and doesn't splatter.

### Power Output

**MENU** → **SET** → **Function** → **TX**

| Band | Maximum Power |
|------|---------------|
| HF (1.8-29.7 MHz) | 100W |
| 6m (50-54 MHz) | 100W |

### Setting Power Level

1. Press **FUNCTION** button
2. Touch **RF PWR** 
3. Adjust with **MULTI** knob (0-100%)

Or adjust the RF PWR slider on the touch screen.

### Power vs. S-Units

| Power | Approximate S-Unit Change |
|-------|---------------------------|
| 100W → 50W | -0.5 S-unit |
| 100W → 25W | -1 S-unit |
| 100W → 10W | -1.7 S-units |

> 💡 **Tip**: Use the minimum power needed. QRP (5W) contacts are more satisfying!

---

## 🎙️ Microphone Gain and Compression

Proper audio settings ensure your signal is clear and readable.

### Microphone Gain

**MENU** → **SET** → **Function** → **TX** → **MIC GAIN**

**Setting microphone gain:**
1. Connect a dummy load
2. Speak at normal level while watching ALC meter
3. Adjust MIC GAIN so ALC **just barely** moves
4. Peaks should TOUCH the ALC zone, not pin it

### Speech Compressor

The compressor increases average power without increasing peak power, improving readability.

**Enable via:**
1. Press **FUNCTION**
2. Touch **COMP** to toggle on
3. Touch and hold to adjust level

### Compressor Settings

| Setting | Range | Effect |
|---------|-------|--------|
| COMP Level | 0-10 | Higher = more compression |

**Conservative setting:** 3-4 for natural sound
**Aggressive setting:** 6-8 for DX/contests

> ⚠️ **Warning**: Over-compression sounds harsh and can cause splatter. Less is more!

### Checking Your Audio

1. Enable **MONI** (Monitor) function
2. Speak into microphone
3. Listen for distortion or clipping
4. Adjust MIC GAIN and COMP as needed

---

## 📏 ALC and Power Metering

### Understanding ALC

ALC (Automatic Level Control) prevents over-driving the transmitter.

**ALC meter interpretation:**

| ALC Reading | Meaning | Action |
|-------------|---------|--------|
| Not moving | Under-driven | May increase gain |
| Just touching | Perfect | No action needed |
| Mid-scale | OK, watching | Reduce if hits max |
| Pinned/max | Over-driven | **Reduce input immediately** |

### Power Meter

Shows actual RF output power.

**Meter options:** (Touch the meter to cycle)
- PO (Power Output)
- SWR
- ALC
- COMP (Compression level)
- ID (Drain current)
- VD (Drain voltage)
- TEMP (PA temperature)

---

## 🔧 Transmit Bandwidth and Audio

### Filter Width (SSB)

**MENU** → **SET** → **Function** → **TX** → **SSB TX BPF**

| Setting | Bandwidth | Use |
|---------|-----------|-----|
| 100-2900 Hz | Wide | Local/ragchew |
| 300-2700 Hz | Medium | General use |
| 500-2500 Hz | Narrow | DX/contests |

### Monitor TX Audio

Always check your transmitted audio using the MONI function before important contacts.

---

## 💡 Real-Life Operating Tips

### Reception Strategies

**In contests:**
> "I run NR at 2-3 and use the narrow filter. The DSP filters are so good that I rarely need more NR."

**Working weak DX:**
> "Turn OFF the preamp on 40m and below - the band noise is already high. Use preamp on 15m and 10m when the band is quiet."

**Eliminating QRM:**
> "I combine manual notch for steady carriers with the DSP filter for adjacent channel rejection. The waterfall shows me exactly what's happening."

### Transmission Best Practices

**Audio reports:**
> "I always ask for audio reports from stations I work regularly. 'How's my audio?' has helped me fine-tune my settings."

**Power management:**
> "I run 50-75W most of the time. Only go to 100W when really needed. The finals will last longer and your signal isn't that much weaker."

**Split operation:**
> "Watch the waterfall to see WHERE the DX is listening. If everyone is calling on one frequency, try the edges of the pileup."

### Common Mistakes to Avoid

1. **Too much compression** - Sounds distorted, causes splatter
2. **ALC pinned** - Over-driving causes distortion
3. **Preamp on noisy bands** - Just amplifies the noise
4. **Full power always** - Unnecessary and heats the PA
5. **Ignoring SWR** - High SWR reduces power and can damage finals

> 🔗 **See also**: [Scope Operation](17_scope_operation.md) for visual signal analysis
