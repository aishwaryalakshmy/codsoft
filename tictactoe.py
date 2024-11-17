import math

# Initialize the game board
board = [' ' for _ in range(9)]

# Print the board in a readable format
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for a winner
def check_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    return [player, player, player] in win_conditions

# Check for a tie
def check_tie():
    return ' ' not in board

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 1  # AI wins
    elif check_winner(board, 'X'):
        return -1  # Human wins
    elif check_tie():
        return 0  # Tie

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

# AI's move
def ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

# Human move
def human_move():
    while True:
        move = input("Enter your move (1-9): ")
        try:
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("This space is taken!")
        except (ValueError, IndexError):
            print("Invalid move. Try again.")

# Main game loop
def main():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and the AI is O.")
    print_board()
    while True:
        human_move()
        print_board()
        if check_winner(board, 'X'):
            print("Congratulations, you win!")
            break
        elif check_tie():
            print("It's a tie!")
            break

        print("AI's turn...")
        ai_move()
        print_board()
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        elif check_tie():
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
