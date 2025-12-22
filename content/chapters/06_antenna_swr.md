# Antenna & SWR

Understanding SWR (Standing Wave Ratio) and proper use of the antenna tuner are essential skills for any IC-7300 operator. This chapter explains how to measure SWR, use the built-in tuner, and ensure your antenna system is working properly.

## Understanding SWR

### What is SWR?

SWR (Standing Wave Ratio) measures how well your antenna system is matched to the transceiver's 50Ω output. 

**Perfect match**: SWR = 1:1 (all power goes to antenna)
**Good match**: SWR = 1.5:1 (about 4% reflected)
**Acceptable**: SWR = 2:1 (about 11% reflected)
**Marginal**: SWR = 3:1 (about 25% reflected)
**Poor**: SWR > 3:1 (significant power loss)

### Why SWR Matters

1. **Power transfer**: High SWR means less power reaches the antenna
2. **Final amplifier protection**: Very high SWR can damage the transmitter
3. **Transmission line losses**: High SWR increases cable losses
4. **Signal quality**: Poor match can cause distortion

### SWR Reference Table

| SWR | Power Reflected | Power to Antenna |
|-----|-----------------|------------------|
| 1.0:1 | 0% | 100% |
| 1.5:1 | 4% | 96% |
| 2.0:1 | 11% | 89% |
| 3.0:1 | 25% | 75% |
| 4.0:1 | 36% | 64% |
| 5.0:1 | 44% | 56% |

---

## Measuring SWR on the IC-7300

The IC-7300 has a built-in SWR meter that provides accurate readings.

### Displaying the SWR Meter

1. Touch the **meter area** on screen while transmitting
2. Touch **SWR** to select SWR display
3. The meter now shows SWR when transmitting

You can also toggle through:
- **Po**: Power output
- **SWR**: Standing Wave Ratio
- **ALC**: Automatic Level Control
- **COMP**: Compression level
- **Vd**: Drain voltage
- **Id**: Drain current

### Spot SWR Measurement

To measure SWR at a single frequency:

1. Press **TUNER** to turn OFF the tuner (important!)
   - This measures the antenna directly, not through the tuner
2. Set the frequency you want to measure
3. Select **RTTY** mode (provides steady carrier)
4. Touch meter to show **SWR**
5. Press **TRANSMIT** or hold PTT briefly
6. Read the SWR from the meter
7. Release PTT

💡 **Tip**: RTTY mode provides a constant carrier, ideal for SWR measurement.

### SWR Plot Measurement

The IC-7300 can plot SWR across a frequency range:

1. Press **MENU** > **SCOPE SET**
2. Touch **SWR Plot**
3. Set START and END frequencies
4. Touch **MEASURE**
5. The radio scans and plots SWR

This shows the SWR curve for your antenna, helping identify:
- Resonant frequency (lowest SWR)
- Usable bandwidth
- Need for adjustment

---

## The Internal Antenna Tuner

The IC-7300 includes an automatic antenna tuner that can match impedances from approximately 16.7Ω to 150Ω (SWR up to 3:1).

### How the Tuner Works

The internal ATU uses an L-network of inductors and capacitors:

1. It samples the forward and reflected power
2. Automatically adjusts L and C values
3. Memorizes settings for each frequency segment
4. Recalls settings when you return to a frequency

### Tuner Specifications

| Parameter | Value |
|-----------|-------|
| Matching Range | 16.7 - 150Ω (SWR ≤ 3:1) |
| Memory Points | Per frequency segment |
| Tuning Time | 2-3 seconds typical |
| Emergency Mode | Matches higher SWR at reduced power |

### Enabling the Tuner

**Quick enable** (uses memorized settings):
- Press **TUNER** once
- **TUNE** icon appears on screen
- Previously stored match is applied

**Start tuning** (find new match):
- Press and hold **TUNER** for 1 second
- **TUNE** icon blinks during tuning
- Radio transmits briefly
- Icon stops blinking when complete

### Manual Tuning Procedure

For best results, tune at each frequency you'll use:

1. Set your operating frequency
2. Press **TUNER** to enable (if not already)
3. Hold **TUNER** for 1 second to start tuning
4. Wait for tuning to complete (icon stops blinking)
5. Check SWR - should now be low

### Tuning Different Band Segments

If your antenna SWR varies across a band:

1. Tune at the low end of the band segment
2. Tune at the high end
3. The tuner memorizes both settings
4. It interpolates for frequencies between

**Example for 40m**:
- Tune at 7.000 MHz
- Tune at 7.150 MHz
- Tune at 7.300 MHz
- Now the entire band is covered

---

## Emergency Tuning Mode

When your antenna SWR exceeds 3:1, the standard tuner won't engage. Emergency mode allows tuning with high SWR but at reduced power.

### Enabling Emergency Mode

1. Press **MENU** > **SET** > **Function**
2. Find **Tuner (Emergency)**
3. Set to **ON**
4. Press **EXIT**

### Using Emergency Mode

When enabled:
- Tuner will attempt to match SWR up to approximately 10:1
- Maximum power is reduced to 50W
- Use only when necessary (temporary antennas, emergency situations)

⚠️ **Warning**: Don't rely on Emergency mode for normal operation. Fix your antenna!

---

## External Antenna Tuners

While the internal tuner is convenient, you may need an external tuner for:

- Antennas with SWR > 3:1
- Wide-range matching capability
- Use with amplifiers

### ICOM External Tuners

The IC-7300 supports automatic control of:

- **AH-4**: Remote automatic tuner
- **AH-2b**: Mobile antenna tuner

These connect to the **TUNER** port on the rear panel and are controlled automatically.

### Non-ICOM External Tuners

When using other external tuners:

1. **Disable internal tuner**: Press **TUNER** until icon disappears
2. **Connect tuner** between radio and antenna
3. **Use tuner's controls** to find match
4. Some tuners can use the radio's tune signal

**Popular Compatible Tuners**:
- LDG AT-100/AT-200 (with ICOM cable)
- LDG IT-100 (designed for ICOM)
- MFJ-939I (ICOM interface)
- Elecraft KAT series

### LDG IT-100 Setup

The IT-100 is specifically designed for ICOM radios:

1. Connect control cable to radio's **TUNER** port
2. Connect coax from radio to tuner input
3. Connect antenna to tuner output
4. Press **TUNER** on radio - IT-100 will tune

---

## Interpreting SWR Readings

### Good SWR Range

| SWR | Interpretation | Action |
|-----|----------------|--------|
| 1.0 - 1.5 | Excellent | None needed |
| 1.5 - 2.0 | Good | Tuner optional |
| 2.0 - 2.5 | Acceptable | Use tuner |
| 2.5 - 3.0 | Marginal | Tuner required |
| > 3.0 | Poor | Check antenna! |

### Common SWR Problems

**SWR too high everywhere**:
- Check all connections
- Look for damaged coax
- Verify antenna is installed correctly
- Check antenna dimensions

**SWR good on one band, high on others**:
- Single-band antenna (normal)
- Multi-band antenna needs adjustment
- Balun or matching issue

**SWR changes with weather**:
- Normal for some antennas
- Wet conditions affect resonance
- May need re-tuning after rain

**SWR changes when touching coax**:
- Common mode current issue
- Need choke balun at feedpoint
- RF in the shack

---

## Protection Circuits

The IC-7300 has built-in protection for high SWR conditions.

### Automatic Power Reduction

When SWR exceeds safe limits:

1. **First level** (SWR 2.5-3:1): Slight power reduction
2. **Second level** (SWR > 3:1): Significant power reduction
3. **Extreme** (SWR > 10:1): Transmission blocked

### SWR Protection Settings

In **MENU** > **SET** > **Function**:

- **SWR Cal**: Calibrate SWR meter
- **Tuner (Emergency)**: Enable emergency tuning

---

## Antenna Tips for IC-7300

### Recommended Antenna Types

**Dipoles**: Simple and effective
- Cut to frequency: Length = 468 / frequency (MHz) feet
- Feed with 50Ω coax
- SWR typically 1.5:1 or better at resonance

**Vertical Antennas**: Good for DX
- Require good ground/radial system
- Often multi-band with traps or loading
- SWR may vary more than dipoles

**End-Fed Half-Wave**: Convenient installation
- Requires matching transformer (49:1 or 64:1)
- Can be multi-band with tuner
- Watch for RF in the shack

**Beam Antennas**: Best performance
- Requires rotator
- Excellent SWR when properly tuned
- Good for DX chasing

### Multi-Band Solutions

For operating multiple bands:

1. **Fan dipole**: Multiple dipoles sharing one feedpoint
2. **Trap dipole**: Single wire with band-switching traps
3. **Off-center fed dipole**: Multi-band with tuner
4. **Vertical with radials**: Usually multi-band

---

## Quick Reference: SWR Checklist

Before transmitting, verify:

- [ ] Antenna connected securely
- [ ] Coax in good condition
- [ ] SWR below 2:1 (or tuner engaged)
- [ ] Operating frequency within antenna's design range
- [ ] No objects touching antenna

If SWR is high:

- [ ] Check all connections
- [ ] Verify correct antenna port
- [ ] Try different frequency
- [ ] Inspect feedline
- [ ] Use antenna analyzer if available

---

*Continue to [Digital Modes Overview](07_digital_modes.md) to learn about setting up the IC-7300 for FT8, PSK31, and other digital modes.*
