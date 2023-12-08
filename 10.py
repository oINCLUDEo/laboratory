import tkinter as tk
import random


def check_winner(board, player):
    # Проверка строк, столбцов и диагоналей на победу
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    return all(board[i][j] != '' for i in range(3) for j in range(3))


def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ''
                    best_score = min(score, best_score)
        return best_score


def find_best_move(board):
    best_move = None
    best_score = -float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


def on_click(row, col):
    global player, board, winner

    if board[row][col] == '' and not winner:
        board[row][col] = player
        buttons[row][col].config(text=player)

        if check_winner(board, player):
            winner_label.config(text=f"Игрок {player} победил!")
            winner = True
        elif is_board_full(board):
            winner_label.config(text="Ничья!")
            winner = True
        else:
            player = 'O' if player == 'X' else 'X'

            if player == 'O' and not winner:
                row, col = find_best_move(board)
                board[row][col] = player
                buttons[row][col].config(text=player)

                if check_winner(board, player):
                    winner_label.config(text=f"Компьютер победил!")
                    winner = True
                elif is_board_full(board):
                    winner_label.config(text="Ничья!")
                    winner = True
                else:
                    player = 'X'


root = tk.Tk()
root.title("Крестики-нолики")

player = 'X'
winner = False
board = [['' for _ in range(3)] for _ in range(3)]

buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', font=('Arial', 20), width=4, height=2,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j)

winner_label = tk.Label(root, text='', font=('Arial', 16))
winner_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
