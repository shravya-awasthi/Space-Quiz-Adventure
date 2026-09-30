# Project Statement — Space Quiz Adventure

## 1. Problem Statement

Beginner programmers need projects where they can put basic programming concepts together into one complete working application. A simple command-line quiz does not show graphical user interaction, event handling, timers, file storage and modular design all together. Space Quiz Adventure tries to solve this with a small educational desktop game based on space and astronomy questions.

## 2. Proposed Solution

Space Quiz Adventure is a Python Tkinter desktop application. The player enters a name and goes through three levels of multiple-choice space questions. The game gives three lives and a 15-second timer for each question. A correct answer adds points. A wrong answer or a timeout takes away a life. At the end, the score is saved to a local text file.

## 3. Scope

The project covers:

- Desktop GUI-based quiz interaction
- Three levels of astronomy questions
- Timer and life management
- Score calculation
- Local score-file storage
- Basic validation testing
- Modular Python implementation

The current version does not include online multiplayer, a database server, user accounts, cloud storage or network services.

## 4. Target Users

- Students learning Python
- Beginners learning GUI programming
- Students interested in space and astronomy
- Users who want a short educational quiz game

## 5. High-Level Features

1. Player name input
2. Graphical quiz interface
3. Three difficulty levels
4. Four multiple-choice options per question
5. Three lives
6. 15-second countdown timer
7. Level-based scoring
8. Score persistence using a text file
9. Replay and exit controls
10. Basic validation tests

## 6. Functional Requirements

- The system should accept and validate the player's name.
- The system should show one question and four answer options at a time.
- The system should have three levels of questions.
- The system should keep track of three player lives.
- The system should run a 15-second timer for each question.
- The system should calculate the score based on the current level.
- The system should move to the next question or level depending on the game state.
- The system should save the final score to `scores.txt`.
- The system should let the player restart or exit after the game ends.

## 7. Non-Functional Requirements

- **Usability:** the controls and status information should be easy to understand.
- **Performance:** the local GUI should respond quickly to user actions.
- **Reliability:** the timer, lives, level and score should be updated consistently.
- **Maintainability:** the functionality should be divided into meaningful modules.
- **Resource efficiency:** the application should run locally using standard Python libraries.
- **Error handling:** empty player names should be rejected, and a missing score file should be handled safely.

## 8. Main Modules

| Module | Responsibility |
|---|---|
| `main.py` | Starts the application |
| `game.py` | GUI, game flow, timer, lives, levels, scoring |
| `questions.py` | Stores question data for all levels |
| `score.py` | Saves and reads scores |
| `utils.py` | Reusable helper functions and ASCII artwork |
| `test_project.py` | Basic project validation tests |

## 9. Workflow

```text
Start Application
       ↓
Enter Player Name
       ↓
Validate Name
       ↓
Level 1 → Display Question → Answer / Timeout
       ↓
Update Score or Lose Life
       ↓
Level 2
       ↓
Level 3
       ↓
Game Over / Completion
       ↓
Save Score
       ↓
Play Again or Exit
```

## 10. Expected Learning Outcomes

The project shows the use of Python functions, classes, lists, dictionaries, conditions, loops, modules, file handling, Tkinter GUI programming, event-driven programming, timer events, validation and basic testing.
