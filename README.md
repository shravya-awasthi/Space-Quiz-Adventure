# 🚀 Space Quiz Adventure

## 1. Project Overview

Space Quiz Adventure is a colourful desktop quiz game made in Python using Tkinter.

The player goes through three space-themed levels and answers multiple-choice questions. The player has three lives and must answer each question before a 15-second timer runs out.

The project was made to show programming concepts like functions, lists and dictionaries, modules, conditional logic, file handling, GUI programming, event-driven programming and timers.

## 2. Problem Statement

Many beginner programming projects only work through the command line. This project is a small but complete graphical application. In it, a learner can use Python concepts to solve a meaningful interactive problem, which is creating an educational quiz game.

## 3. Objectives

- Build a working desktop application using Python.
- Use modular programming by separating the game, question, score and utility logic.
- Provide an easy-to-use graphical interface.
- Show input validation and error handling.
- Use a timer, lives, levels, scoring and file storage to make a complete workflow.
- Check important project data with basic tests.

## 4. Game Features

- 🚀 Space-themed Tkinter GUI
- ❤️ Three lives
- ⭐ Three levels: Easy, Medium, Hard
- ⏱️ 15-second timer for every question
- 🏆 Level-based scoring
- 🎨 Four clearly different answer-button colours
- 💾 Score saving in `scores.txt`
- 🔄 Play-again option
- ❌ Exit option
- 🧪 Basic validation tests

## 5. Levels

### Level 1 - Easy
Basic space questions.

### Level 2 - Medium
More detailed astronomy questions.

### Level 3 - Hard
More challenging space questions.

## 6. Scoring

Correct answers give:

- Level 1: 10 points
- Level 2: 20 points
- Level 3: 30 points

A wrong answer or a timeout costs one life.

## 7. Technologies

- Python 3
- Tkinter
- Functions
- Dictionaries
- Lists
- Modules
- File handling
- Event-driven programming

## 8. How to Run

1. Install Python 3.
2. Open this folder in VS Code, IDLE, or another Python editor.
3. Run `main.py`.

Tkinter normally comes with Python on Windows and macOS. On some Linux installations, Tkinter may need to be installed separately.

## 9. Project Files

- `main.py` - starts the game
- `game.py` - game logic and GUI
- `questions.py` - question database
- `score.py` - score storage
- `utils.py` - helper functions
- `scores.txt` - saved scores
- `test_project.py` - tests the game
- `README.md` - project introduction
- `statement.md` - project summary
- `requirements.txt` - requirements for the full experience

## 10. Installation

1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal inside the project folder.
4. Tkinter is part of the standard Python installation on most desktop setups. On some Linux systems, it may need to be installed separately.

No external Python packages are required.

## 11. Running the Program

```bash
python main.py
```

Enter a player name and click **START GAME**.

## 12. Testing

Run the basic validation tests with:

```bash
python test_project.py
```

Expected result:

```text
Ran 18 tests in (seconds)s

OK
```

The tests check the three-level question structure, the number of questions and options, and the valid answer indexes.

Manual GUI testing should also check:

1. An empty player name shows a warning.
2. Questions and four options are displayed.
3. Correct answers increase the score.
4. Wrong answers reduce a life.
5. A timeout reduces a life.
6. The timer resets for each question.
7. Level changes work correctly.
8. Game Over saves the score.
9. Play Again goes back to the start screen.
10. Exit closes the application.

## 13. VITyarthi Modules

### Functional modules

1. Player/game initialization
2. Question and answer processing
3. Level and life management
4. Timer management
5. Score management and file storage
6. GUI presentation and navigation

### Non-functional requirements

- **Usability:** simple buttons and clear status labels.
- **Performance:** lightweight local application, and the GUI responds immediately.
- **Reliability:** input validation and controlled game-state changes.
- **Maintainability:** the logic is divided into meaningful Python modules.
- **Resource efficiency:** uses only the Python standard library, with no external services.
- **Error handling:** empty-name validation and safe reading of the score file.

## 14. Design Artefacts

The design diagrams used in the report are also in the repository under `diagrams/`: architecture, workflow, use case, sequence, class/component, and storage design.

## 15. Future Improvements

- Sound effects
- More questions
- Difficulty selection
- High-score ranking
- Power-ups
- Animated spaceship
- Images and background music
