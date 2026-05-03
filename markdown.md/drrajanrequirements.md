In this final group project, each group will design a small practical system using the concepts studied in EEE120 Digital Design Fundamentals. The project must include:

A digital logic design using combinational circuits and, where possible, simple sequential logic.
A working simulation in CircuitVerse.
A basic Python software version of the same idea.
A short pitch-style presentation explaining the problem, design, working logic, and demonstration.
Optional but encouraged: use of AI/LLMs to improve the idea, generate test cases, explain logic, or support the software interface.
 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Final Deliverables

Each group must submit the following:

CircuitVerse/LogiSim Design
A working CircuitVerse project that includes:

Logic gates
Inputs and outputs
Proper labels
A clear working circuit
Truth table or logic explanation
Sequential component if relevant, such as flip-flop, memory bit, counter, or state logic
Python Software Prototype
A simple Python program that simulates or extends the same logic.

The Python program may include:

Console-based input/output
Basic menu system
Simple GUI if students want to try
Rule-based decision logic
Score calculation
Status display
Test cases
GitHub Repository
Each group must upload their code and project files to GitHub.

The GitHub repository should include:

Python code
README file
CircuitVerse link
Screenshots
Team member names and roles
Short explanation of the project
Presentation
Each group must prepare a pitch-style presentation of maximum 10 slides.

The presentation should include:

Project title and team members
Problem statement
Why this project is useful
Inputs and outputs
Digital logic design explanation
CircuitVerse screenshot or demo link
Python software screenshot or demo
Testing and results
Role of AI/LLM, if used
Conclusion and future improvement
A short demo video may be included if feasible.

 

Important Note on AI Use

Students are allowed to use AI tools such as ChatGPT, Gemini, Claude, or other LLMs. However, they must clearly mention:

What they used AI for
What they understood themselves
What they changed or improved
Any AI-generated code or explanation must be checked and understood by the group
Marks will be reduced if students submit AI-generated work that they cannot explain.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Each project must include:

At least 4 inputs
At least 2 outputs where possible
At least 5 logic gates
A truth table or decision table
CircuitVerse simulation
Python program with user input
GitHub repository
Presentation slides
 

Suggested Presentation Flow

Slide 1: Title

Project name, group number, team members.

Slide 2: Problem

What real-world problem are you solving?

Slide 3: System Overview

Show inputs, outputs, and basic idea.

Slide 4: Logic Design

Explain the logic rules.

Slide 5: Truth Table or Decision Table

Show how inputs produce outputs.

Slide 6: CircuitVerse Design

Show screenshot and explain the circuit.

Slide 7: Python Prototype

Show code screenshot or output screenshot.

Slide 8: Demo

Show working result or short video.

Slide 9: AI/LLM Usage

Explain whether AI was used and how.

Slide 10: Conclusion

What worked, what was difficult, and what can be improved.


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Suggested GitHub Repository Structure

EEE120_Final_Project_GroupName/

│

├── README.md

├── circuitverse_link.txt

├── screenshots/

│   ├── circuit_design.png

│   ├── python_output.png

│

├── src/

│   └── main.py

│

├── presentation/

│   └── final_presentation.pdf

│

└── demo_video_link.txt

 

README File Must Include

Project Title:

Group Members:

Course:

Instructor:

Problem Statement:

Inputs:

Outputs:

Digital Logic Explanation:

CircuitVerse Link:

Python Program Explanation:

How AI/LLM was used:

How to Run the Python Code:

Screenshots:

Future Improvements:

 

Assessment Rubric

Total Marks: 100

Component

Marks

Description

Problem Understanding and Practical Relevance

10

Clear explanation of the problem, why it matters, and how it connects to real life

Digital Logic Design

20

Correct use of logic gates, input/output mapping, truth table, and circuit explanation

CircuitVerse Implementation

15

Working simulation, neat design, proper labels, and ability to demonstrate the circuit

Python Software Prototype

15

Functional Python program, correct logic, user interaction, and basic testing

Connection Between Circuit and Python

10

Python program should reflect the same decision logic as the digital circuit

Presentation and Pitch Quality

10

Clear, professional, maximum 10 slides, good structure, practical explanation

GitHub Repository and Documentation

10

Clean repository, README file, code uploaded properly, CircuitVerse link included

Teamwork and Role Distribution

5

Clear contribution from each group member

AI/LLM Usage Reflection

5

Honest explanation of how AI was used and what the students understood


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Team Role Suggestion

Each group should divide responsibilities clearly:

Role

Responsibility

Logic Designer

Defines inputs, outputs, truth table, and Boolean logic

CircuitVerse Designer

Builds and tests the circuit

Python Developer

Writes and tests the Python program

Documentation Lead

Manages GitHub README, screenshots, and submission

Presenter

Leads the final presentation and demo

For groups of 4, one student may handle two roles.

 

Submission Instructions for Canvas

Each group must submit one PDF or document containing:

Project title
Group members and IDs
GitHub repository link
CircuitVerse project link
Presentation file or PDF
Demo video link, if available
Short note on AI/LLM usage
Only one student from each group should upload the final submission to Canvas.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Academic Integrity

Students may use online resources and AI tools for support, but they must understand and explain their own work.

Copying another group’s circuit, code, or presentation will result in reduced marks or zero marks depending on severity.

During the presentation, each group member may be asked to explain part of the project. Marks may be adjusted if a student cannot explain their contribution.

 

Final Note to Students

This project is not only about making a circuit. It is about understanding how simple digital logic can become part of real practical systems such as smart homes, healthcare tools, education systems, traffic systems, security systems, and AI-inspired decision tools.

The goal is to show that even basic logic gates can be used to build useful real-world systems.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Project 1: Smart Room Light Controller

Problem

Design a smart room lighting system that decides whether the light should turn ON or OFF based on room conditions.

Inputs

Person detected: Yes/No
Room is dark: Yes/No
Manual switch: ON/OFF
Energy saving mode: ON/OFF
Output

Light ON/OFF
Digital Design Requirement

Students should design a combinational logic circuit that controls the light based on the input conditions.

Example logic:

The light turns ON if:

A person is present AND the room is dark
OR
Manual switch is ON
But if energy saving mode is ON, the light should turn ON only when a person is present.

Python Requirement

Create a Python program where the user enters room conditions and the program tells whether the light should turn ON or OFF.

Practical Relevance

Smart homes, energy saving, IoT systems.