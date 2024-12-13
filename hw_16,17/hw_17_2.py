def print_board(board):
    print("-------------")
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
        print("-------------")

def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_board_full(board):
    return " " not in board

def play_game():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    current_player = "X"
    print("********** Игра Крестики-нолики для двух игроков **********")
    
    while True:
        print_board(board)
        try:
            move = int(input(f"Куда поставим {current_player}? ")) - 1
            if board[move] not in ["X", "O"]:
                board[move] = current_player
            else:
                print("Эта клетка уже занята, попробуйте другую.")
                continue
        except (ValueError, IndexError):
            print("Неверный ввод. Введите номер от 1 до 9.")
            continue
        
        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} выиграл!")
            break
        if is_board_full(board):
            print_board(board)
            print("Ничья!")
            break
        
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
