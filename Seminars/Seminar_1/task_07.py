'''
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print
'''

LOWER_LIMIT = 1
UPPER_LIMIT = 9999
ONE = 1
TEN = 10
HUNDRED = 100
SQUARE = 2

num = LOWER_LIMIT - ONE
while num < LOWER_LIMIT or num > UPPER_LIMIT:
    num = int(input(f'Введите чило от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
if num < TEN:
    res = f'Число {num} - цифра. Её квадрат = {num**SQUARE}'
elif num < HUNDRED:
    first_num = num // TEN
    second_num = num % TEN
    res = f'Число {num} - двузначное число. Произведение цифр = {first_num*second_num}'
else:
    first_num = num // HUNDRED
    second_num = num // TEN % TEN
    third_num = num % TEN
    mirror = third_num * 100 + second_num * 10 + first_num
    res = f'Число {num} - трёхначное число. Его зеркальное число = {mirror}'
print(res)
