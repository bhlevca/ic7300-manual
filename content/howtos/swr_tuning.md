# SWR Tuning (How‑to)

This how‑to describes practical, step‑by‑step procedures for measuring and reducing Standing Wave Ratio (SWR) on the IC‑7300. It is written in a concise, neutral style with cross‑references to related chapters such as the Antenna & SWR chapter and the troubleshooting flow.

## Overview

SWR indicates impedance matching between the transmitter and antenna system. This guide covers safe measurement, use of the internal tuner, interpretation of results, and basic remedial actions.

**Key targets**
- Ideal: < 1.5:1
- Acceptable for operation: < 2:1
- Use caution and reduce power: 2.0–3.0:1
- Do not transmit normally: > 3.0:1 (investigate)

## Preconditions

1. Ensure the transceiver is connected to the intended antenna or a dummy load.
2. Verify power supply at 13.8 V nominal.
3. Use low power for tuning (5–10 W recommended) to reduce risk.
4. If available, have an external SWR meter or antenna analyzer for verification.

## Step‑by‑step procedure

1. Set RF Power to a low value (5–10 W).  
2. Disable the internal tuner briefly to measure the antenna directly: press **TUNER** until the TUNE icon disappears (or confirm tuner is OFF).  
3. Set the operating frequency to the frequency you intend to use.  
4. Select a steady carrier mode (RTTY or use the Tune function) for the measurement.  
5. Touch the meter area on the display and cycle to **SWR**.  
6. Key the transmitter briefly (press PTT) or use the TUNER's tuning carrier to read SWR on the meter.  
7. Record the result and release PTT.

### If SWR is acceptable
- Re‑enable the tuner if desired and operate normally.  
- Optionally store tuner settings by enabling and allowing the tuner to memorize matches at the operating frequencies (press and hold **TUNER** to start auto‑tune).

### If SWR is high (> 2:1)
1. Reduce power.  
2. Check coax and connectors for damage, corrosion, or loose fittings.  
3. Test with a known good dummy load at the feed point — if SWR is 1:1 on a dummy load, the radio and cable are likely OK.  
4. Try tuning at several points across the band (low, center, high) and record the SWR curve (see SWR Plot procedure in the Antenna & SWR chapter).  
5. If necessary, enable the tuner and attempt auto‑tune (hold **TUNER** 1 second). If auto‑tune does not reach an acceptable match, consult the troubleshooting flow.

## Reading SWR on transmit safely
- Always use low power when keying to measure SWR.  
- Do not touch the antenna or feedline while transmitting.  
- If available, use a dummy load when diagnosing suspected antenna problems.

## Examples

**Example 1 — Simple tuning**
- Band: 20 m, Frequency: 14.200 MHz, Measured SWR: 3.0:1.
- Steps: Reduce power to 5 W → verify connectors → test dummy load → enable tuner and start auto‑tune → recheck SWR.

**Example 2 — Plot and inspect**
- Use the SWR Plot function (MENU > SCOPE SET > SWR Plot) to identify resonant frequency and bandwidth.

## Troubleshooting and links
- If SWR remains high after the steps above, see the troubleshooting flow: [High SWR on Transmit](../chapters/12_troubleshooting.md#high-swr-on-transmit).  
- For background information, see the Antenna & SWR chapter: [Antenna & SWR](../chapters/06_antenna_swr.md).  
- For a concise pre‑transmit checklist, see: [Safe First Transmission & SWR Verification](./safe_first_transmission.md).  

## Safety and best practice
- Never touch the antenna or coax during transmit.  
- Use a good quality dummy load for testing and an external SWR meter when available.  
- Keep records of tuner memory points for common frequencies.

---

*See also: [Scan for broadcasts (How‑to)](../howtos/scan_for_broadcasts.md) and the [Quick Reference Card](../chapters/14_quick_reference_card.md).*