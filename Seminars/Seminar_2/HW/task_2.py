'''
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions
'''

import fractions
from math import gcd

frac1 = "1/2"
frac2 = "1/3"

# Разделяем на числитель и знаменатель
num_1, den_1 = map(int, frac1.split('/'))
num_2, den_2 = map(int, frac2.split('/'))

# Сумма дробей: приводим к общему знаменателю
common_den = den_1 * den_2
num_sum = num_1 * den_2 + num_2 * den_1

# Сокращаем дробь
gcd_sum = gcd(num_sum, common_den)
num_sum //= gcd_sum
common_den //= gcd_sum

# Произведение дробей
num_mul = num_1 * num_2
den_mul = den_1 * den_2

# Сокращаем дробь
gcd_mul = gcd(num_mul, den_mul)
num_mul //= gcd_mul
den_mul //= gcd_mul

# Выводим результат
print(f'Сумма дробей: {num_sum}/{common_den}')
print(f'Произведение дробей: {num_mul}/{den_mul}')

# Используем модуль fractions для проверки
a = fractions.Fraction(frac1)
b = fractions.Fraction(frac2)
print(f'Проверка суммы: {a + b}')
print(f'Проверка произведения: {a * b}')
