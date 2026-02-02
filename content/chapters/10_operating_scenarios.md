# Operating Scenarios and Techniques

This chapter covers practical operating scenarios with detailed guidance on receiving, transmitting, noise reduction, filtering, and VOX operation. These are the techniques that experienced operators use daily.

## Receiving Signals

### Optimal Receive Setup

**Basic Receive Configuration:**
1. Set RF GAIN to maximum (fully clockwise on outer ring)
2. Set SQUELCH to open for SSB/CW (fully counter-clockwise)
3. Set appropriate filter bandwidth for the mode
4. Enable spectrum scope for visual signal finding

**Filter Selection by Mode:**

| Mode          | Recommended Filter | Width       | Purpose                          |
| ------------- | ------------------ | ----------- | -------------------------------- |
| SSB           | FIL1               | 2.4 kHz     | Normal voice reception           |
| SSB (crowded) | FIL2               | 1.8 kHz     | Reduce adjacent interference     |
| CW            | FIL2               | 500 Hz      | Standard CW reception            |
| CW (contest)  | FIL3               | 250 Hz      | Maximum selectivity              |
| AM            | FIL1               | 6 kHz       | Full fidelity                    |
| FM            | FIL1               | 15 kHz      | Standard FM                      |
| Digital       | FIL1               | 2.4-3.0 kHz | Capture digital signal bandwidth |

### Tuning SSB Signals

**The Problem:** SSB signals sound distorted if you're not exactly on frequency.

**Proper SSB Tuning:**
1. Tune to the signal until you hear voice
2. If voice sounds too high-pitched (chipmunk): tune DOWN
3. If voice sounds too low-pitched (rumbling): tune UP
4. When voice sounds natural: you're on frequency

**Fine Tuning Technique:**
1. Listen to the sibilants (S sounds) in speech
2. These should sound crisp, not mushy or whistly
3. Use RIT if the other station is slightly off

### Tuning CW Signals

**Setting Your CW Pitch:**
1. Press **QUICK** in CW mode
2. Select **CW Pitch**
3. Choose your preferred pitch (typically 600-800 Hz)
4. The radio will center CW signals at this pitch

**Tuning to a CW Signal:**
1. Find the signal on the waterfall (thin vertical line)
2. Touch the signal or tune with main dial
3. Adjust until the tone matches your set pitch
4. Use **FILTER** to narrow bandwidth if needed

### Tuning Digital Signals

**FT8/FT4:**
- Set mode to USB-D (or USB)
- Tune to standard FT8 frequency (e.g., 14.074 MHz)
- Signals appear as short horizontal dashes on waterfall
- Let WSJT-X software handle the actual signal selection

**PSK31:**
- Use PSK software to tune within the passband
- Radio typically stays on one frequency
- Software selects signals visually

---

## Transmitting: Best Practices

### Pre-Transmission Checklist

Before every transmission, confirm:
- [ ] You're on an appropriate frequency for your license
- [ ] The frequency is clear (ask "Is this frequency in use?")
- [ ] Your antenna/SWR situation is acceptable
- [ ] Power level is appropriate for the situation
- [ ] Correct mode is selected

### Power Level Selection

**Guidelines for Power Selection:**

| Situation                | Suggested Power | Reason                        |
| ------------------------ | --------------- | ----------------------------- |
| Local contacts (<500 mi) | 25-50W          | Sufficient, saves power       |
| Regional contacts        | 50-75W          | Good balance                  |
| DX/Long distance         | 75-100W         | Maximum effectiveness         |
| Contests                 | 100W            | Need every advantage          |
| Digital modes (FT8)      | 25-50W          | Often sufficient, protects TX |
| Testing/Tuning           | 5-10W           | Minimize interference         |

**Why Not Always Use Full Power:**
- QRP contacts are rewarding
- Less interference to others
- Reduced RF exposure
- Longer equipment life
- Lower power bill!

### Making a Contact: Step-by-Step

**Calling CQ (Seeking Contacts):**

1. **Find a clear frequency**
   - Check spectrum scope for open space
   - Tune and listen for 30 seconds
   - Ask "Is this frequency in use?" (wait for response)

2. **Make your CQ call**
   ```
   "CQ CQ CQ, this is [your call sign]
   [your call sign] calling CQ and standing by"
   ```

3. **Listen for responses**
   - Watch waterfall for signals appearing
   - Listen for someone calling your call sign

4. **Respond to caller**
   ```
   "[Their call], this is [your call]
   You're 5-9 in [your location]
   Name here is [your name]
   How do you copy? [their call] this is [your call]"
   ```

**Answering Someone's CQ:**

1. **Wait for them to finish calling**

2. **Respond with your call sign**
   ```
   "[Their call], this is [your call sign] [phonetically]"
   ```

3. **Wait for acknowledgment**

4. **Exchange information**
   - Signal report (e.g., "5-9" = loud and clear)
   - Location
   - Name
   - Other information as appropriate

### Signal Reports

**RST System:**

| Readability | Meaning                         |
| ----------- | ------------------------------- |
| 1           | Unreadable                      |
| 2           | Barely readable                 |
| 3           | Readable with difficulty        |
| 4           | Readable with little difficulty |
| 5           | Perfectly readable              |

| Strength | S-Meter Reading           |
| -------- | ------------------------- |
| 1        | Faint, barely perceptible |
| 3        | Weak                      |
| 5        | Fair                      |
| 7        | Moderately strong         |
| 9        | Strong signal             |

**Common Reports:**
- **5-9**: Loud and clear (often given even when not quite true)
- **5-7**: Good readable signal
- **5-5**: Adequate but not strong
- **5-3**: Weak but workable

---

## Noise Reduction Techniques

### Types of Noise

**Understanding Noise Sources:**

| Noise Type    | Characteristics | Best Solution                 |
| ------------- | --------------- | ----------------------------- |
| White noise   | Constant hiss   | NR (Noise Reduction)          |
| Impulse noise | Clicks, pops    | NB (Noise Blanker)            |
| Heterodyne    | Steady whistle  | Notch filter                  |
| AC hum        | 60/120 Hz buzz  | Notch or DSP filtering        |
| QRM           | Other stations  | Narrow filter, shift passband |
| Atmospheric   | Crashes, static | Wait, or use NR               |

### Noise Blanker (NB) Operation

**What NB Does:**
- Samples the signal for pulse-type noise
- Blanks (mutes) the audio during noise pulses
- Works best on repetitive impulse noise

**Setting Up NB:**
1. Press **FUNCTION** until NB is visible
2. Touch **NB** to enable
3. Touch and hold **NB** to adjust level
4. Start with level 3-5
5. Increase if noise persists
6. Decrease if audio becomes distorted

**NB Effectiveness:**
- ✓ Car ignition noise
- ✓ Electric fence interference
- ✓ Some computer noise
- ✗ Continuous noise (use NR instead)
- ✗ Atmospheric static (limited help)

### Noise Reduction (NR) Operation

**What NR Does:**
- DSP analyzes audio for noise patterns
- Subtracts estimated noise from signal
- Reveals signals buried in noise

**Setting Up NR:**
1. Press **FUNCTION** until NR is visible
2. Touch **NR** to enable
3. Touch and hold **NR** to adjust level
4. Start with level 4-6
5. Increase until noise is reduced
6. Stop before audio becomes "watery" or "robotic"

**NR Tips:**
- Level 8-10 is very aggressive (may distort)
- Level 4-6 usually optimal for SSB
- Higher levels can work for CW
- Some loss of naturalness is normal

### Notch Filter Operation

**Auto Notch:**
- Automatically finds and removes carriers
- Enable in FUNCTION menu
- Good for single heterodyne
- May struggle with multiple interfering carriers

**Manual Notch:**
- You control the notch frequency
- Use MULTI knob to move notch
- Better for complex interference
- Takes practice to use effectively

**When to Use Notch:**
- Steady whistle on frequency
- Carrier interference
- Unintentional mixing products
- NOT for voice interference (use filter instead)

### Passband Tuning

The IC-7300 allows shifting the receive passband to avoid interference.

**Using Twin PBT:**
1. Press **FILTER**
2. Touch **SHIFT** or **WIDTH**
3. Use touch screen to adjust

**SHIFT:** Moves entire passband up or down in frequency
- Use when interference is on one side of the signal

**WIDTH:** Narrows the passband symmetrically
- Use to reduce all interference equally

**Practical Example:**
- Signal at 14.225 MHz
- Interference just above the signal
- Use SHIFT to move passband DOWN
- Interference moves out of passband

---

## Filter Configuration and Use

### Understanding IF Filters

The IC-7300 has three configurable filter positions (FIL1, FIL2, FIL3).

**Default Settings:**

| Position | SSB     | CW     | AM    | FM     |
| -------- | ------- | ------ | ----- | ------ |
| FIL1     | 2.4 kHz | 500 Hz | 6 kHz | 15 kHz |
| FIL2     | 1.8 kHz | 250 Hz | 3 kHz | 10 kHz |
| FIL3     | 500 Hz  | 50 Hz  | 2 kHz | 7 kHz  |

### Customizing Filter Widths

**To Change Filter Settings:**
1. Press **FILTER**
2. Touch the bandwidth display
3. Use touch slider to adjust width
4. New setting saves to current filter position

**Or in Menu:**
1. **MENU** → **SET** → **Function** → **Filter**
2. Select mode (SSB, CW, etc.)
3. Adjust FIL1, FIL2, FIL3 widths

### Filter Selection Strategies

**For SSB Voice:**
- **Comfortable listening:** 2.4-2.7 kHz (FIL1)
- **Crowded band:** 1.8-2.1 kHz (FIL2)
- **Extreme interference:** Custom narrow setting

**For CW:**
- **Casual operation:** 400-500 Hz
- **Contest/pileup:** 250-300 Hz
- **Ultimate selectivity:** 50-100 Hz (requires very stable signal)

**For Digital Modes:**
- **FT8/FT4:** 2.4-3.0 kHz (need to capture signal spread)
- **PSK31:** 500 Hz (very narrow signal)
- **RTTY:** 500-1000 Hz (twin tones)

### Shape Factor

Beyond width, filter shape matters:

**SOFT Shape:**
- Gradual rolloff
- More natural audio
- Less ringing on CW
- Good for relaxed operation

**SHARP Shape:**
- Steep rolloff  
- Maximum rejection
- May cause ringing on CW
- Best for severe interference

**To Change Shape:**
1. Press **FILTER**
2. Look for shape indicator
3. Touch to toggle SOFT/SHARP

---

## VOX (Voice Operated Transmit)

### What VOX Does

VOX automatically keys the transmitter when you speak, and returns to receive during pauses. This enables hands-free operation.

### Configuring VOX

**Basic VOX Settings:**
1. Press **QUICK** in SSB mode
2. Touch **VOX**
3. Enable VOX

**Or in Menu:**
- **MENU** → **SET** → **Function** → **VOX**

**Key Parameters:**

| Setting   | Range    | Purpose                             |
| --------- | -------- | ----------------------------------- |
| VOX Gain  | 0-100%   | Sensitivity to voice                |
| Anti-VOX  | 0-100%   | Prevents speaker from triggering TX |
| VOX Delay | 0-3000ms | Hold time after you stop speaking   |

### Setting Up VOX

**Step 1: Set VOX Gain**
1. Start with gain at 50%
2. Speak at normal voice level
3. Radio should key (TX) when you speak
4. Reduce gain if it keys on background noise
5. Increase if it doesn't key reliably

**Step 2: Set Anti-VOX**
1. Turn up speaker volume
2. Set Anti-VOX high enough that speaker audio doesn't trigger TX
3. Usually 50-70% works well
4. Use headphones to eliminate this issue entirely

**Step 3: Set VOX Delay**
1. Start with 500ms delay
2. Too short: clips words and returns to RX between sentences
3. Too long: stays in TX during natural pauses
4. 300-800ms typical for conversation
5. Shorter for contest operation

### VOX Operating Tips

**When to Use VOX:**
- Contests (speed is critical)
- Nets where you transmit frequently
- Operating while doing other tasks
- When you need hands free

**When NOT to Use VOX:**
- High noise environment
- Background noise (TV, people talking)
- When sharing space with others
- Digital modes (use CAT control instead)

**Common VOX Problems:**

| Problem                  | Cause                    | Solution                            |
| ------------------------ | ------------------------ | ----------------------------------- |
| Keys on noise            | Gain too high            | Reduce VOX gain                     |
| Keys on speaker          | Anti-VOX too low         | Increase Anti-VOX or use headphones |
| Cuts off words           | Delay too short          | Increase VOX delay                  |
| Stays keyed during pause | Delay too long           | Reduce VOX delay                    |
| Erratic operation        | Inconsistent voice level | Speak more consistently             |

---

## Operating Scenarios

### Scenario 1: Casual SSB Ragchew

**Setup:**
- Mode: USB (above 10 MHz) or LSB (below 10 MHz)
- Filter: FIL1 (2.4 kHz)
- Power: 50-75W
- NR: Level 4-5 if needed
- AGC: FAST

**Procedure:**
1. Find a calling frequency or call CQ
2. Exchange signal reports and names
3. Discuss topics of mutual interest
4. Exchange 73s (best regards) at end

**Pro Tips:**
- Let the other station finish before transmitting
- Keep transmissions reasonably short
- Use phonetics for call signs when needed
- Keep a log (paper or electronic)

### Scenario 2: Working a DX Pileup

**Setup:**
- Mode: SSB or CW
- Filter: FIL2 (narrower)
- Power: 100W (maximum)
- Compression: ON (level 3-5)
- Split operation may be required

**What's a Pileup:**
- Rare/DX station is calling CQ
- Many stations respond simultaneously
- DX station picks out individual calls

**Technique:**
1. **Listen first!** Learn the DX station's pattern
2. Determine if they're working split (listening on different frequency)
3. Wait for them to finish a contact
4. Give your call sign clearly, once or twice
5. STOP and listen - do NOT keep calling
6. If they respond to you, give quick signal report
7. Let them control the QSO pace

**Common Mistakes:**
- Calling while DX is transmitting
- Continuous calling without listening
- Long-winded transmissions
- Calling on DX transmit frequency when they're working split

### Scenario 3: Emergency/Priority Traffic

**Setup:**
- Mode: USB on 14.300 MHz (Maritime Mobile/emergency)
- Filter: FIL1
- Power: 100W
- Everything else: default

**If You Hear Emergency Traffic:**
- Do NOT transmit unless you can help
- Stand by and listen
- Note details in case you need to relay

**If You Have an Emergency:**
1. Transmit "MAYDAY MAYDAY MAYDAY" (life-threatening) or
   "PAN PAN PAN" (urgent but not immediately life-threatening)
2. Give your call sign
3. State your location
4. State nature of emergency
5. State what assistance you need
6. Listen for response

### Scenario 4: Contest Operation

**Setup:**
- Mode: SSB or CW
- Filter: FIL2 or FIL3 (narrow)
- Power: 100W
- AGC: FAST
- VOX: ON with short delay
- Compression: ON

**Contest Exchange:**
- Keep it SHORT
- Standard exchange varies by contest
- Example: call sign, signal report, serial number or zone

**Efficient Technique:**
1. Find clear frequency or answer CQs
2. Use standard phonetics
3. Confirm exchange was received correctly
4. Log the contact immediately
5. Move on quickly

### Scenario 5: Net Operation

**What's a Net:**
- Organized on-air meeting
- Net Control Station (NCS) runs the net
- Participants check in and may pass traffic

**Setup:**
- Mode: Usually USB or LSB
- Filter: FIL1
- Power: As needed to be heard
- Listen for NCS instructions

**Net Procedure:**
1. Listen for NCS to call for check-ins
2. When called, give your call sign clearly
3. Wait for acknowledgment
4. Follow NCS instructions
5. Don't transmit unless called upon

---

## Advanced Receive Techniques

### Using RF Gain

**Default Position:** Fully clockwise (maximum)

**When to Reduce RF Gain:**
- Very strong signals cause distortion (AGC can't keep up)
- S-meter pinned at maximum
- Audio sounds harsh or distorted

**Technique:**
1. Start with RF gain at maximum
2. If strong signal causes problems, reduce RF gain
3. Watch S-meter - should come off the peg
4. Audio should clean up
5. Readjust as signal strength changes

### Using Attenuator

The IC-7300 has built-in attenuators for extreme signal conditions.

**Accessing Attenuator:**
1. Press **FUNCTION**
2. Look for **ATT** option
3. Select attenuation level (6dB, 12dB, 18dB)

**When to Use:**
- Very strong local signals causing overload
- When RF gain reduction isn't enough
- Contest weekends on lower bands
- Near broadcast transmitters

### Pre-Amp Settings

**The IC-7300's preamp settings:**
- P.AMP 1: Moderate gain boost
- P.AMP 2: Maximum gain boost
- AMP OFF: No amplification

**General Guidelines:**
- HF (below 30 MHz): Usually P.AMP OFF
- 6 meters: P.AMP 1 or 2 helpful
- Strong signal conditions: AMP OFF
- Weak signal conditions: Try P.AMP 1

---

## Summary: Operating Quick Reference

| Situation  | Mode    | Filter | Power     | Special               |
| ---------- | ------- | ------ | --------- | --------------------- |
| Casual SSB | USB/LSB | FIL1   | 50W       | NR if needed          |
| CW Ragchew | CW      | FIL2   | 50W       | AGC SLOW              |
| DX Pileup  | Any     | FIL2   | 100W      | Compression ON        |
| Contest    | Any     | FIL2/3 | 100W      | VOX ON                |
| Digital    | USB-D   | FIL1   | 30-50W    | Software controls PTT |
| Net        | USB/LSB | FIL1   | As needed | Follow NCS            |
| Testing    | Any     | Any    | 10W       | Dummy load            |
