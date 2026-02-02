# Scan for broadcasts (How‑to)

This how‑to explains the scanning functions of the IC‑7300: Program Scan, Memory Scan, and using the Spectrum Scope for quick scanning and tuning. The document is concise and follows a neutral style with links to related references.

## Overview

Scanning lets the operator quickly locate active signals across a band or a list of stored frequencies. Scans can be performed using program lists, memory channels, or by interacting directly with the spectrum scope.

## Program Scan (quick list)

1. Prepare a program list (frequencies you wish to scan).  
   - MENU > SCAN > Program Scan → Create or Edit the list.  
2. Start the scan: press **SCAN** or use the on‑screen control and choose **Program Scan**.  
3. The radio will step through the list and stop on active signals.  
4. To stop or pause the scan: press **SCAN** again or touch the displayed frequency.  

**Notes**: Program Scan is ideal for custom lists (repeaters, beacons, nets).

## Memory Scan

1. Write frequencies to memory channels (MW or V/M options).  
2. MENU > SCAN > Memory Scan → select range or saved group.  
3. Start scan: radio steps through memory channels and stops on active signals.  
4. To add a frequency to memory while listening: store current frequency to a memory channel (Hold MW).  

## Spectrum Scope Scanning

1. Press **M.SCOPE** or touch the spectrum display.  
2. Touch or double‑touch a signal on the scope to immediately tune to it.  
3. In **Center** mode, drag across the scope to sweep the frequency and tune continuously.  
4. Use **Scroll‑C** mode for wide scanning when you want continuous motion through the band.

![Scope Touch to Tune](../images/scope_touch_tune_placeholder.svg)
*Caption: Touch the waterfall or a peak to jump and tune. Replace with an annotated GIF showing touch → tune sequence.*

## Pausing, Resuming and Locking

- Pause: Press **SCAN** or touch the screen.  
- Resume: Press **SCAN** again or the play control.  
- Lock: If a memory or program channel should be omitted, lock it in the memory editor.

## Examples

**Scanning for broadcast AM stations on 40 m**
- Set mode to AM, set step size to 1 kHz, and use Program Scan with a list of expected broadcast frequencies.

**Finding local repeaters**
- Prepare a memory group of repeater inputs → Memory Scan → radio stops on active repeater inputs.

## Troubleshooting

- If the scan never stops, check squelch settings (may be too open).  
- If the scope is unresponsive, ensure **SCOPE** is enabled in MENU > SCOPE SET.

---

*See also: [Spectrum Scope](../chapters/17_scope_operation.md) and the [Menu Tree reference](../quick_refs/menu_tree.md).*