# PRESENTATION STRUCTURE: Smart Switch

---

## **Slide 1: Cover / Title**
**Title:** Smart Switch
**Subtitle:** *An intelligent room lighting decision system — detects room conditions and automatically decides whether to turn the light ON or OFF.*

**Team Members:**
- 😎 **Maxmudov Vosiqxoja** — Web & Python Developer, Git Manager
- 🎮 **Arslan Gafarov** — Built homes in Minecraft, took the demo videos lol
- 💡 **Shaxizoda Shernazarova** — Senior Logic Circuits & CircuitVerse Developer
- 😌 **Muxtorov Humoyun** — Chill guy. Managed docs & made sure we checked every requirement box

**Supervisor:** Dr. Rajan Tripathi
**Course:** EEE120 — Digital Design Fundamentals

---

## **Slide 2: Problem Statement**
**Title:** What Problem Are We Solving?

- 💡 Lights left ON in empty rooms waste energy daily — a small but real global problem
- 🏠 Manual switching is inconvenient and often forgotten
- ⚡ No smart logic = no context-awareness (dark? occupied? saving mode?)
- 🔘 Existing smart systems are complex and expensive — we model the core logic simply
- ✅ **Our solution:** A rule-based digital circuit that decides light state from 4 room conditions

---

## **Slide 3: System Overview**
**Title:** How It Works — Inputs → Logic → Output

**Inputs (4):**
| Input | Type | Meaning |
|---|---|---|
| Person Detected | Binary (0/1) | Is someone in the room? |
| Room Dark | Binary (0/1) | Is it dark enough to need light? |
| Manual Switch | Binary (0/1) | User forcing light ON |
| Energy Saving Mode | Binary (0/1) | Restrict light unless person present |

**Output (1):**
| Output | Meaning |
|---|---|
| Light (LED) | ON (1) or OFF (0) |

**Core Idea:**
- Light turns ON if person is present AND room is dark
- OR if Manual switch is ON
- BUT in Energy Saving Mode → light only turns ON if person is present

---

## **Slide 4: Logic Design**
**Title:** The Logic Behind the Switch

**Boolean Expression:**
```
Light = [(Person AND Dark) OR Manual] AND NOT(EnergySave)
        OR
        [Person AND EnergySave]
```

**Gates Used:**
- AND gates → combine Person+Dark, Person+EnergySave
- OR gate → combine (Person∧Dark) with Manual
- NOT gate → invert EnergySave signal
- Final OR → merge both condition branches

**Circuit flow (describe visually with the image):**
- Person & Dark → AND → feeds first OR
- Manual → feeds same OR
- OR result → AND with NOT(EnergySave) → first branch
- Person & EnergySave → AND → second branch
- Both branches → final OR → LED output

> 📎 *Use the uploaded CircuitVerse screenshot as visual reference on this slide*

---

## **Slide 5: Truth Table**
**Title:** Truth Table — All 16 Input Combinations

> ⚠️ *Agent note: Render this as a styled HTML table — highlight rows where Light = 1 in green, Light = 0 in soft red/grey*

| Person (P) | Dark (D) | Manual (M) | EnergySave (E) | **Light Output** |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | **0** |
| 0 | 0 | 0 | 1 | **0** |
| 0 | 0 | 1 | 0 | **1** |
| 0 | 0 | 1 | 1 | **0** |
| 0 | 1 | 0 | 0 | **0** |
| 0 | 1 | 0 | 1 | **0** |
| 0 | 1 | 1 | 0 | **1** |
| 0 | 1 | 1 | 1 | **0** |
| 1 | 0 | 0 | 0 | **0** |
| 1 | 0 | 0 | 1 | **1** |
| 1 | 0 | 1 | 0 | **1** |
| 1 | 0 | 1 | 1 | **1** |
| 1 | 1 | 0 | 0 | **1** |
| 1 | 1 | 0 | 1 | **1** |
| 1 | 1 | 1 | 0 | **1** |
| 1 | 1 | 1 | 1 | **1** |

---

## **Slide 6: CircuitVerse Design**
**Title:** Circuit in Action — CircuitVerse Simulation

- Full working simulation built in CircuitVerse
- 4 inputs labeled: Person, Dark, Manual, EnergySave
- Output: LED indicator (lights up = ON)
- Uses: AND, OR, NOT gates — 5+ gates total

> 📎 *Image path:* `images/circuit_verse.jpg`
> *Display as large centered image, full-width. Add a small caption: "Smart Room Light Controller — CircuitVerse Simulation"*

---

## **Slide 7: Live Demo**
**Title:** See It Live

> 🎯 *Style suggestion: Center the link on the slide as a large clickable button/card — dark background, glowing green or yellow border, large font. Maybe add a small "▶ Try it now" arrow icon.*

**🔗 Live Demo:**
[**https://keesouwoudba.github.io/smart-switch/**](https://keesouwoudba.github.io/smart-switch/)


---

## **Slide 8: AI & LLM Usage**
**Title:** How We Used AI Tools

**Case 1 — Claude** *(img: https://cdn-public.softwarereviews.com/production/favicons/offerings/11687/original/claude-color.png)*
- Explained circuit design concepts
- Helped us understand what kind of combinational circuit fits the problem
- Guided logic structure and gate selection

**Case 2 — Google Stitch** *(img: https://miro.medium.com/v2/resize:fit:720/format:webp/1*8xXlqP3d8bzhTkLgOVYNWw.png)*
- Generated initial website design
- Produced `Design.md` and HTML/CSS boilerplate

**Case 3 — GitHub Copilot** *(img: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd4Ge-kF2agKwPQahbpEg5hshKuSFTG9ZVuQ&s)*
- Used our presentation template + prompt structure
- Generated final `presentation.html` content

> *Footer note on slide: "All AI output was reviewed, tested, and understood by the team."*

---

## **Slide 9: Conclusion**
**Title:** Wrapping Up

**✅ What Worked:**
- Team played to individual strengths — everyone delivered their role
- Circuit logic correctly maps to Python and web demo
- Full pipeline: design → simulation → code → deployment

**⚠️ What Was Challenging:**
- Time management during finals week — deadlines everywhere, almost zero breathing room

**🔭 Future Improvements:**
- Add real sensor input (PIR sensor, light sensor)
- Mobile/IoT integration
- Sequential logic: timer-based auto-off

---

## **Slide 10: Thank You**
**Title (Large, Bold, Centered):**
> # Thank You for Your Attention

**Subtitle (smaller):**
> *If you have any questions, feel free to ask!*

> 🎨 *Style suggestion: Clean minimal slide — maybe team photo or team member sticker/emoji row at the bottom. Dark background, large white text. Optional: small GitHub link or QR code in corner.*