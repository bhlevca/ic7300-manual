# Safe First Transmission & SWR Verification (How‑to)

A concise checklist and step‑by‑step procedure to verify the antenna system and perform a safe first transmission. These steps are recommended after antenna or cable changes, and after maintenance.

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
1. Set RF power to low (5–10 W): MENU → SET → TX → RF POWER → select 5–10 W.  
2. Select a steady carrier (for example, **CW** or the **TUNE** function).  
3. Bypass the internal tuner for the initial measurement: press **TUNER** until the TUNE icon disappears.  
4. Select the meter display and choose **SWR**.  
5. Key the transmitter briefly (PTT or TUNE carrier) for 1–2 seconds and read SWR.  
   - If SWR &lt; 1.5:1, continue with step 9.  
   - If SWR is 1.5–2.5:1, enable the internal tuner (press **TUNER**, hold ~1 s) and recheck SWR.  
   - If SWR &gt; 3:1 or the tuner cannot match: cease transmitting, reduce power to minimum, test with a dummy load, and inspect the coax and antenna.
6. If tuner is used successfully and SWR is acceptable, reduce tuner bypass or leave enabled as needed.  
7. With SWR acceptable, set the meter to **ALC**, speak into the microphone at normal level, and verify ALC does not pin (aim for occasional light movement).  
8. Set MIC Gain, COMP, and VOX (if used) conservatively: MIC Gain to give ALC ~50–70% on voice peaks; COMP 0–3 for casual; VOX gain 60% with 0.3s delay when used.  
9. Increase power gradually (for example: 10W → 25W → desired) — monitor SWR and ALC after each increase.  
10. Log the frequency and resulting SWR/tuner settings for future reference.

![Meter SWR Reading](../images/meter_swr_reading_placeholder.svg)
*Caption: Annotated meter showing SWR and ALC while increasing power; replace with real images or GIFs when available.*

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