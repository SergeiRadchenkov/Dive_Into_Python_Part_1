'''
Напишите функцию для транспонирования матрицы
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def trans_matrix(any_matrix):
    new_matrix = [[0] * len(any_matrix) for _ in range(len(any_matrix[0]))]
    for row in range(len(matrix[0])):
        for col in range(len(matrix)):
            new_matrix[col][row] = any_matrix[row][col]
    return new_matrix



for row in trans_matrix(matrix):
    print(row)
