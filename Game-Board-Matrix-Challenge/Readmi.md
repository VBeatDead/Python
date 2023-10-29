**GitHub Repository Title**: "PythonBoardGame"

This repository contains a simple Python board game that you can play. The game is based on the following rules:

1. Create a board matrix with a width specified by the user. List comprehension is used to create the board matrix.
2. There is a player piece (symbol 'A') that can move horizontally and vertically, and there are goal positions (symbol 'O') to reach in the game.
3. If the player piece reaches a goal position, the game ends with a "win," and if it doesn't reach the goal, it's a "loss."
4. The initial player piece and goal positions are generated randomly at the start of the game using a random generator (up to 3 times). Exception handling is implemented for this.
5. Pure functions and lambda expressions are also applied where possible.

### Instructions

To play the game, follow these steps:

1. Clone this repository to your local machine.

2. Run the `game.py` file to start the game.

3. You will be prompted to enter the width of the game board.

4. The game board will be displayed with the player piece ('A') and goal position ('O').

5. You can change the player's position randomly up to 3 times. Enter 'y' to change the position or 'n' to proceed to the game.

6. Enter your moves using 'w' (up), 'a' (left), 's' (down), and 'd' (right) to move the player piece.

7. The game will inform you if you win or lose.

8. You can choose to play again by entering 'y' or exit the game by entering 'n'.

Have fun playing the Python board game!