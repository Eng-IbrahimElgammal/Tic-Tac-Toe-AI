# Tic-Tac-Toe AI

Welcome to Tic-Tac-Toe, an implementation of the classic game with various AI algorithms. This project allows you to play Tic-Tac-Toe against an AI opponent using different search algorithms such as BFS, DFS, IDDFS, UCS, and GBFS.

## Features

- Play against an AI that uses various search algorithms to make moves.
- Choose from multiple AI algorithms: BFS, DFS, IDDFS, UCS, GBFS, and Random.
- Simple text-based interface.
- Play again option to replay the game without restarting the program.

## How to Play

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/tic-tac-toe-ai.git
    ```
2. Navigate to the project directory:
    ```bash
    cd tic-tac-toe-ai
    ```
3. Run the game:
    ```bash
    python tic_tac_toe.py
    ```

4. Enter your move as a number between 1 and 9, where 1 corresponds to the top-left position and 9 corresponds to the bottom-right position.

## AI Algorithms

- **BFS (Breadth-First Search)**: Explores all possible moves level by level.
- **DFS (Depth-First Search)**: Explores as far as possible along each branch before backtracking.
- **IDDFS (Iterative Deepening Depth-First Search)**: Combines the benefits of BFS and DFS by performing a series of depth-limited searches.
- **UCS (Uniform Cost Search)**: Explores paths with the lowest cost first.
- **GBFS (Greedy Best-First Search)**: Chooses paths based on a heuristic that estimates the cost to reach the goal.

## Code Structure


- `tic_tac_toe.py`: The main script containing the game logic and AI algorithms.
- `xo_board(game_board)`: Function to display the Tic-Tac-Toe board.
- `bfs(board)`, `dfs(board)`, `iddfs(board)`, `dls(board, depth, path)`, `ucs(board)`, `gbfs(board)`: Functions implementing the respective AI algorithms.
- `calculate(board)`: Heuristic function used by the GBFS algorithm.
- `you(board)`: Function to handle the player's move.
- `ai(board, algorithm)`: Function to handle the AI's move based on the chosen algorithm.
- `win(board, player)`: Function to check if a player has won the game.
- `reset_game()`: Function to reset the game board.
- `main()`: Main function to run the game.

## Example Gameplay

```plaintext
Welcome to Tic-Tac-Toe!
Enter your move as a number between 1 and 9, where 1 corresponds to the top-left position and 9 corresponds to the bottom-right position.
-------------
| 1 | 2 | 3 | 
-------------
| 4 | 5 | 6 | 
-------------
| 7 | 8 | 9 | 
Choose AI algorithm ( BFS, DFS, IDDFS, UCS, GBFS, Random): BFS
-------------
|   |   |   | 
-------------
|   |   |   | 
-------------
|   |   |   | 
Enter your move (1-9): 5
-------------
|   |   |   | 
-------------
|   | X |   | 
-------------
|   |   |   | 
```
## License
This project is licensed under the MIT License - see the LICENSE file for details.
