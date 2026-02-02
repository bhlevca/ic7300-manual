# Safe First Transmission & SWR Verification (How‑to)

A concise checklist and step‑by‑step procedure to verify your antenna system and perform your first safe transmission. Follow these steps every time you change antennas, cables, or after maintenance.

## Objectives
- Verify correct antenna connection and SWR at low power
- Avoid transmitter damage from high SWR
- Confirm audio and ALC are set safely before full‑power operation

## Preconditions
1. Antenna or dummy load connected to the ANT jack
2. Power supply set to 13.8V nominal and capable of required current
3. Ground connection made and secure
4. SD card inserted (optional for settings backup)

## Step‑by‑step checklist (do this before any transmit)
1. Set RF power to low (5–10 W): MENU → SET → TX → RF POWER → choose 5–10W.  
2. Set mode to **CW** or use the radio's **TUNE** function for a steady carrier.  
3. Ensure tuner is bypassed for the initial measurement: press **TUNER** until the TUNE icon disappears (tuner OFF).  
4. Touch the meter area and cycle to **SWR**.  
5. Key the transmitter briefly (PTT or TUNE carrier) for 1–2 seconds and read the SWR.  
   - If SWR < 1.5:1, proceed to step 9.  
   - If SWR 1.5–2.5:1, enable the internal tuner (press **TUNER**) and hold 1s to auto‑tune. Recheck SWR.  
   - If SWR > 3:1 or tuner fails to match: stop transmitting, reduce power to minimum, test with dummy load, and inspect coax/antenna.
6. If tuner is used successfully and SWR is acceptable, reduce tuner bypass or leave enabled as needed.  
7. With SWR acceptable, set the meter to **ALC**, speak into the microphone at normal level, and verify ALC does not pin (aim for occasional light movement).  
8. Set MIC Gain, COMP, and VOX (if used) conservatively: MIC Gain to give ALC ~50–70% on voice peaks; COMP 0–3 for casual; VOX gain 60% with 0.3s delay when used.  
9. Increase power gradually (for example: 10W → 25W → desired) — monitor SWR and ALC after each increase.  
10. Log the frequency and resulting SWR/tuner settings for future reference.

## If SWR remains high
- Recheck coax connectors, solder joints, and feedpoint.  
- Test with a known good dummy load at the radio end (should show 1:1).  
- Use SWR Plot (MENU → SCOPE SET → SWR Plot) to find resonance; re‑cut or re‑tune antenna elements as needed.  
- Consult [High SWR on Transmit](../chapters/12_troubleshooting.md#high-swr-on-transmit) for a diagnostic flow.

## Safety Notes
- Never touch the antenna or feedline while transmitting.  
- Use a dummy load for first‑time tests to avoid spurious radiation.  
- Reduce power immediately if protection indicators light or the radio reduces output.

---

*See also: [SWR Tuning (How‑to)](swr_tuning.md) and the [Quick Reference Card](../chapters/14_quick_reference_card.md).*