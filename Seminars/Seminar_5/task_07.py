'''
Создайте функцию генератор.
Функция генерирует N простых чисел начиная с 2.
Для проверки числа на простоту используйте правило:
"Число является простым, если делится нацело только на еденицу и на себя". 
'''


def is_prime(num: int):
    if num % 2 == 0 and num != 2:
        return False
    for div in range(3, int(num**0.5) + 1):
        if num % div == 0:
            return False
    return True


def prime_generator(n: int):
    for number in range(2, n + 1):
        if is_prime(number):
            yield number


print(*prime_generator(80))
