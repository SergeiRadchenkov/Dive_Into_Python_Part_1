'''
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
'''

SPACE = ' '
STAR = '*'
ONE = 1

rows = int(input('Введите количество рядов ёлки: '))
spaces = rows - ONE
stars = ONE
for i in range(rows):
    print(spaces * SPACE + stars * STAR)
    spaces -= ONE
    stars += ONE + ONE
