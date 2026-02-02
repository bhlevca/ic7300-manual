# Scan for broadcasts (How‑to)

This how‑to describes the IC‑7300 scanning functions: Program Scan, Memory Scan, and the Spectrum Scope. It is presented concisely with links to related references.

## Overview

Scanning enables locating active signals across a band or a set of stored frequencies. Scans may use program lists, memory channels, or direct interaction with the spectrum scope.

## Program Scan (quick list)

1. Prepare a program list of frequencies to be scanned: MENU > SCAN > Program Scan → Create or Edit the list.  
2. Start the program scan using the **SCAN** control and select **Program Scan**.  
3. The radio steps through the list and stops on active signals.  
4. Stop or pause the scan by pressing **SCAN** or touching the displayed frequency.

**Notes**: Program Scan is ideal for custom lists (repeaters, beacons, nets).

## Memory Scan

1. Store frequencies in memory channels (MW or V/M).  
2. Select MENU > SCAN > Memory Scan and choose a range or saved group.  
3. Start the memory scan; the radio steps through channels and stops on active signals.  
4. To add the current frequency while monitoring, store it to a memory channel (Hold MW).

## Spectrum Scope Scanning

1. Activate the spectrum scope: press **M.SCOPE** or touch the scope area.  
2. Touch or double‑touch a peak to tune directly to that signal.  
3. In **Center** mode, drag across the scope to sweep frequency and tune continuously.  
4. Use **Scroll‑C** mode for a continuous wideband sweep when required.

![Scope Touch to Tune](../images/scope_touch_tune_placeholder.svg)
*Caption: Touch a peak on the spectrum scope to jump and tune; replace with a short GIF demonstrating touch → tuning transition when available.*

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

 - If the scan never stops, check squelch settings (they may be too open).  
 - If the scope is unresponsive, confirm **SCOPE** is enabled in MENU > SCOPE SET.

---

*See also: [Spectrum Scope](../chapters/17_scope_operation.md) and the [Menu Tree reference](../quick_refs/menu_tree.md).*