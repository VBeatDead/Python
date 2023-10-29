import random

def create_board(width):
    return [['-' for _ in range(width)] for _ in range(width)]

def print_board(board):
    for row in board:
        print(' '.join(row))

def generate_random_position(board):
    empty_cells = [(row, col) for row in range(len(board)) for col in range(len(board)) if board[row][col] == '-']
    if empty_cells:
        return random.choice(empty_cells)
    
is_winner = lambda board, player, goal: board[goal[0]][goal[1]] == player

def move_player(board, player, move):
    player_row, player_col = player
    new_row, new_col = player_row, player_col

    if move == 'w':
        new_row -= 1
    elif move == 'a':
        new_col -= 1
    elif move == 's':
        new_row += 1
    elif move == 'd':
        new_col += 1

    if 0 <= new_row < len(board) and 0 <= new_col < len(board):
        board[player_row][player_col] = '-'
        board[new_row][new_col] = 'A'
        return (new_row, new_col)
    else:
        return player

def main():
    while True:
        width = int(input("Masukkan lebar papan: "))
        board = create_board(width)
        player = generate_random_position(board)
        goal = generate_random_position(board)
        board[player[0]][player[1]] = 'A'
        board[goal[0]][goal[1]] = 'O'

        print("Selamat datang di permainan!")
        print_board(board)

        changes = 0
        while changes < 3:
            change_position = input("Ingin mengubah posisi? (y/n): ").lower()
            if change_position == 'y':
                new_player_position = generate_random_position(board)
                board[player[0]][player[1]] = '-'
                board[new_player_position[0]][new_player_position[1]] = 'A'
                player = new_player_position
                changes += 1
                print_board(board)
            else:
                break
            
        moves = input("Masukkan gerakan: ").lower()
        for move in moves:
            player = move_player(board, player, move)
        print_board(board) 
        if is_winner(board, 'A', goal):
            print("Selamat, Anda menang!")
        else:
            print("Maaf, Anda kalah!")
        play_again = input("Mau bermain lagi? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == '__main__':
    main()