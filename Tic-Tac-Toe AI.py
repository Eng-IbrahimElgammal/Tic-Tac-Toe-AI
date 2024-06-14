import random
import queue
import heapq


def xo_board(game_board):
    print("-------------")
    for i in range(0, 9, 3):
        print("|", end=" ")
        for j in range(i, i + 3):
            print(game_board[j], "|", end=" ")
        print("\n-------------")


def bfs(board):
    visited = set()
    q = queue.Queue()
    q.put((board, []))

    while not q.empty():
        curr_board, path = q.get()
        visited.add(tuple(curr_board))

        if win(curr_board, "O"):
            return path[-1]

        for i in range(9):
            if curr_board[i] == " ":
                new_board = curr_board[:]
                new_board[i] = "O"
                if tuple(new_board) not in visited:
                    q.put((new_board, path + [i]))
                    visited.add(tuple(new_board))

    return None


def dfs(board):
    visited = set()
    stack = [(board, [])]

    while stack:
        curr_board, path = stack.pop()
        visited.add(tuple(curr_board))

        if win(curr_board, "O"):
            return path[-1]

        for i in range(9):
            if curr_board[i] == " ":
                new_board = curr_board[:]
                new_board[i] = "O"
                if tuple(new_board) not in visited:
                    stack.append((new_board, path + [i]))

    return None


def iddfs(board):
    for depth in range(1, 10):
        result = dls(board, depth, [])
        if result is not None:
            return result[-1]

    return None


def dls(board, depth, path):
    if depth == 0:
        return None

    if win(board, "O"):
        return path

    for i in range(9):
        if board[i] == " ":
            new_board = board[:]
            new_board[i] = "O"
            result = dls(new_board, depth - 1, path + [i])
            if result is not None:
                return result

    return None


def ucs(board):
    visited = set()
    pq = [(0, board, [])]

    while pq:
        cost, curr_board, path = heapq.heappop(pq)

        if win(curr_board, "O"):
            return path[-1]

        visited.add(tuple(curr_board))

        for i in range(9):
            if curr_board[i] == " ":
                new_board = curr_board[:]
                new_board[i] = "O"
                new_cost = cost + 1
                if tuple(new_board) not in visited:
                    heapq.heappush(pq, (new_cost, new_board, path + [i]))
                    visited.add(tuple(new_board))

    return None


def gbfs(board):
    pq = []
    heapq.heappush(pq, (0, board, []))

    while pq:
        _, curr_board, path = heapq.heappop(pq)

        if win(curr_board, "O"):
            return path[-1]
        for i in range(9):
            if curr_board[i] == " ":
                new_board = curr_board[:]
                new_board[i] = "O"
                heuristic = calculate(new_board)
                heapq.heappush(pq, (heuristic, new_board, path + [i]))

    return None


def calculate(board):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    heuristic = 0
    for combination in win_combinations:
        count_x = 0
        count_o = 0
        for i in combination:
            if board[i] == "X":
                count_x += 1
            elif board[i] == "O":
                count_o += 1

        if count_x == 0 and count_o > 0:
            heuristic += 1
        elif count_x > 0 and count_o == 0:
            heuristic -= 1

    return heuristic


def you(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please try again.")
            elif board[move] != " ":
                print("That position is already occupied. Please try again.")
            else:
                board[move] = "X"
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

    return board


def ai(board, algorithm):
    if algorithm == "DFS":
        move = dfs(board)
    elif algorithm == "BFS":
        move = bfs(board)
    elif algorithm == "IDDFS":
        move = iddfs(board)
    elif algorithm == "UCS":
        move = ucs(board)
    elif algorithm == "GBFS":
        move = gbfs(board)
    else:
        move = random.choice([i for i in range(9) if board[i] == " "])

    board[move] = "O"
    return board


def win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combination in win_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False


def reset_game():
    board = [" "] * 9
    game_over = False
    return board, game_over


def main():
    print("Welcome to Tic-Tac-Toe!")
    print("Enter your move as a number between 1 and 9, where 1 corresponds to the top-left position and 9 corresponds "
          "to the bottom-right position.")
    xo_board([str(i + 1) for i in range(9)])

    while True:
        board, game_over = reset_game()
        algorithm = input("Choose AI algorithm ( BFS, DFS, IDDFS, UCS, GBFS, Random): ")

        while not game_over:
            xo_board(board)
            board = you(board)

            if win(board, "X"):
                print("Congratulations! You win!")

                break

            if " " not in board:
                print("It's a tie!")

                break

            board = ai(board, algorithm)

            if win(board, "O"):
                print("Sorry, you lose!")

                break

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break


if __name__ == "__main__":
    main()
