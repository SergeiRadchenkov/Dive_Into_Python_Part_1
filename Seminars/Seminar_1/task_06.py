'''
Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print
'''

REFORM = 1582
BIG_LEAP_YEAR = 400
SMALL_LEAP_YEAR = 4
LARGE_MON_LEAP_YEAR = 100
MULTIPLE = 0

year = int(input('Введите год: '))
if year < REFORM:
    res = 'Григорианский календарь ещё не введён'
elif year % BIG_LEAP_YEAR == MULTIPLE:
    res = f'{year} - високосный год'
elif year % 100 == MULTIPLE:
    res = f'{year} - не високосный год'
elif year % SMALL_LEAP_YEAR == MULTIPLE:
    res = f'{year} - високосный год'
else:
    res = f'{year} - не високосный год'
print(res)
