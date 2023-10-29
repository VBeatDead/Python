import random

# Fungsi untuk membuat board matrix
def create_board(width):
    return [['-' for _ in range(width)] for _ in range(width)]

# Fungsi untuk mencetak board
def print_board(board):
    for row in board:
        print(' '.join(row))

# Fungsi untuk memeriksa apakah pemain menang
def is_winner(board, player, goal):
    return board[goal[0]][goal[1]] == player

# Fungsi untuk menggerakkan pemain
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

# Fungsi untuk menghasilkan posisi acak
def generate_random_position(board):
    empty_cells = [(row, col) for row in range(len(board)) for col in range(len(board)) if board[row][col] == '-']
    if empty_cells:
        return random.choice(empty_cells)
    else:
        raise ValueError("Tidak ada sel kosong di papan!")

# Main function
def main():
    original_board = None

    while True:
        try:
            width = int(input("Masukkan lebar papan: "))
            board = create_board(width)
            player = generate_random_position(board)
            goal = generate_random_position(board)
            board[player[0]][player[1]] = 'A'
            board[goal[0]][goal[1]] = 'O'
            original_board = [row[:] for row in board]  # Simpan board awal

            print("Selamat datang di permainan!")
            print_board(board)

            changes = 0
            while changes < 3:  # Maksimal 3 kali mengacak board
                change_position = input("Ingin mengacak board? (y/n): ").lower()
                if change_position == 'y':
                    board = create_board(width)  # Mengacak ulang board
                    player = generate_random_position(board)
                    goal = generate_random_position(board)
                    board[player[0]][player[1]] = 'A'
                    board[goal[0]][goal[1]] = 'O'
                    original_board = [row[:] for row in board]  # Simpan board awal kembali
                    changes += 1
                    print_board(board)
                else:
                    break

            chances = 2  # Set jumlah kesempatan pemain
            while chances > 0:
                moves = input("Masukkan gerakan: ").lower()
                for move in moves:
                    player = move_player(board, player, move)

                print_board(board)

                if is_winner(board, 'A', goal):
                    print("Selamat, Anda menang!")
                    chances = 0
                    break
                else:
                    chances -= 1
                    if chances > 0:
                        print(f"Anda memiliki {chances} kesempatan lagi!")

            if chances == 0 and not is_winner(board, 'A', goal):
                print("Maaf, Anda kalah!")

            play_again = input("Mau bermain lagi? (y/n): ").lower()
            if play_again != 'y':
                break
            else:
                board = [row[:] for row in original_board]  # Kembalikan board ke kondisi awal
                print_board(board)

        except ValueError as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == '__main__':
    main()
