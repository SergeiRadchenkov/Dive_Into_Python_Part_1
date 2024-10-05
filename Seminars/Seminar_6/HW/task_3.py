'''
Напишите функцию в шахматный модуль. 
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
'''
import random
from itertools import combinations

def generate_board():
    board = []

    for i in range(1, 8+1):
        queen = (i, random.randint(1, 8))
        board.append(queen)
    return board

def is_attacking(q1, q2):
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True

def generate_boards():
    count = 0
    board_list = []
    while count < 4:
        board = generate_board()
        if check_queens(board):
            count += 1
            board_list.append(board)
    return board_list

board_list = generate_boards()
if len(board_list) == 4:
    print("Найдено 4 успешных расстановки:")
    for idx, board in enumerate(board_list, 1):
        print(f"{idx}: {board}")
else:
    print("Ошибка, не удалось найти 4 успешных расстановки.")
