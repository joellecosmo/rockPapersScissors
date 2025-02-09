# Rock-Paper-Scissors Game

This is a simple **Rock-Paper-Scissors** game written in Python. The user plays against the computer, choosing one of the three weapons: **Rock (🪨), Paper (📄), or Scissors (✂️)**.

## How the Game Works
- The user selects the number of sets they want to play.
- Each round, the user is prompted to input their weapon:
  - `R` for Rock 🪨
  - `P` for Paper 📄
  - `S` for Scissors ✂️
- The computer randomly selects its weapon.
- The winner of each round is determined using standard Rock-Paper-Scissors rules:
  - **Rock beats Scissors**
  - **Scissors beats Paper**
  - **Paper beats Rock**
  - A tie occurs if both players select the same weapon.
- The game keeps track of wins, losses, and ties.
- At the end of all sets, the results are displayed.

## Installation & Usage
### Requirements
Ensure you have **Python 3.x** installed on your system.

### Running the Game
1. Download the `rock_paper_scissors.py` file.
2. Open a terminal or command prompt in the file’s directory.
3. Run the script using:
   ```sh
   python rock_paper_scissors.py

## Improvements and Customizations
 - Add a scoreboard that tracks wins/losses across multiple sessions.
 - Implement a graphical version using a GUI library like Tkinter or PyGame.
 - Enhance user experience by adding sound effects or animations.
