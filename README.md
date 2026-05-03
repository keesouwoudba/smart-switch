# Smart Switch

Smart Room Light Controller for EEE120 Digital Design Fundamentals.

This project turns a simple room-light decision into a practical digital system. The assignment asked for a Python implementation, and we completed that requirement in [python/main.py](python/main.py). We also went beyond the baseline by building an interactive website demo and a Minecraft/redstone-inspired visual simulation so the same logic could be shown in a more engaging way.

## Project Title

Smart Switch: Smart Room Light Controller

## Group Members

- Maxmudov Vosiqxoja — Web & Python Developer, Git Manager
- Arslan Gafarov — Minecraft / demo video support
- Shaxizoda Shernazarova — Logic Circuits & CircuitVerse Developer
- Muxtorov Humoyun — Documentation and requirements review

## Course

EEE120 — Digital Design Fundamentals

## Instructor

Dr. Rajan Tripathi

## Problem Statement

Design a smart room lighting system that decides whether the light should turn ON or OFF based on room conditions. The goal is to reduce wasted electricity, avoid forgotten manual switches, and show how basic digital logic can solve a real-life automation problem.

## Inputs

The system uses 4 binary inputs:

- Person Detected (P): Is someone in the room?
- Room Dark (D): Is the room dark enough to need light?
- Manual Switch (M): Is the user forcing the light ON?
- Energy Saving Mode (E): Should the system restrict the light unless a person is present?

## Outputs

- Light (L): ON or OFF

The presentation and circuit also describe the LED output visually.

## Digital Logic Explanation

The project follows the assignment rule set:

- Light turns ON if a person is present AND the room is dark.
- Light turns ON if the manual switch is ON.
- If energy saving mode is ON, the light should turn ON only when a person is present.

The boolean expression used in the presentation is:

$$
L = \bigl(((P \land D) \lor M) \land \lnot E\bigr) \lor (P \land E)
$$

This is a combinational circuit. It uses AND, OR, and NOT gates, and it does not depend on memory or a clock signal.

## Python Program Explanation

The Python prototype in [python/main.py](python/main.py) is a console program that:

- asks the user for the 4 binary inputs,
- evaluates the logic using gate-style functions,
- prints the result and explanation,
- prints the full 16-row decision table,
- runs built-in self-tests.

The Python version mirrors the circuit logic instead of using a separate app-style shortcut.

## Website Demo

We also built a website version of the project in the main web app files. This was a creative extension of the assignment so the logic could be demonstrated interactively in a browser, not only as a console program.

The website uses the same smart-light idea and includes a live interface, room-state behavior, and a presentation-friendly demo flow.

## Minecraft / Redstone-Inspired Demo

To make the project more visual and fun, we also created a Minecraft/redstone-inspired simulator concept. This was used to show the logic in a game-like block layout and to connect the circuit idea to a familiar visual environment.

## Truth Table / Decision Table

The system has 4 inputs, so there are 16 possible input combinations.

The logic table is included in the presentation, and the Python program can print the full table automatically.

## CircuitVerse Link

Replace with the final shared link:

- CircuitVerse project: [add your link here](circuitverse/Smart%20Room%20Light%20Controller.cv)

## GitHub Repository

Replace with your final repository link:

- GitHub: [add your link here](.)

## Screenshots

- CircuitVerse screenshot: [images/circuit_verse.jpg](images/circuit_verse.jpg)
- Python output image: [python/image.png](python/image.png)
- Minecraft/redstone simulator screenshot: [stitch_redstone_circuit_simulator/screen.png](stitch_redstone_circuit_simulator/screen.png)

## How to Run the Python Code

Run the console prototype with:

```bash
/usr/bin/python python/main.py
```

Inside the menu, you can:

- evaluate one room scenario,
- show the decision table,
- run self-tests,
- exit.

## AI / LLM Usage

We used AI tools to support the project, but we reviewed and understood the output ourselves.

- Claude helped explain the logic design and circuit structure.
- Google Stitch helped generate the initial website layout and design notes.
- GitHub Copilot helped draft and refine the presentation content.

What we understood ourselves:

- the meaning of each input,
- why the circuit is combinational,
- how the truth table maps to the output,
- how the Python logic matches the circuit.

What we changed or improved:

- we adapted the logic to match the assignment exactly,
- we created a clearer presentation flow,
- we added a Python decision table and self-tests,
- we extended the idea into a website demo and Minecraft/redstone-inspired visual version.

## Team Roles

- Logic Designer: Shaxizoda Shernazarova
- CircuitVerse Designer: Shaxizoda Shernazarova
- Python / Web Developer: Maxmudov Vosiqxoja
- Documentation Lead: Muxtorov Humoyun
- Demo / Visual Support: Arslan Gafarov

## Future Improvements

- Add a real sensor-based input version using a PIR and light sensor.
- Add a timer-based auto-off feature.
- Add a mobile-friendly IoT control layer.
- Expand the Minecraft/redstone version into a fuller interactive demo.


