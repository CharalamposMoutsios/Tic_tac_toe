board = [    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board(board):
    for row in board:
        print('|'.join(row))

def check_win(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def get_move(board, player):
    valid_move = False
    while not valid_move:
        row = int(input(f"{player}'s turn. Enter row number (1-3): ")) - 1
        col = int(input(f"{player}'s turn. Enter column number (1-3): ")) - 1
        if row in range(3) and col in range(3) and board[row][col] == ' ':
            board[row][col] = player
            valid_move = True
        else:
            print("Invalid move. Please try again.")

def play_game():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    players = ['X', 'O']
    current_player = players[0]
    while True:
        print_board(board)
        get_move(board, current_player)
        if check_win(board, current_player):
            print(f"{current_player} wins!")
            break
        if all([cell != ' ' for row in board for cell in row]):
            print("It's a tie!")
            break
        current_player = players[(players.index(current_player) + 1) % 2]

play_game()