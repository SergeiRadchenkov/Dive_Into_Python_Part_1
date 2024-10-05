'''
Создайте функцию генератор чисел Фибоначчи
'''


def fibonacci():
    prev_fib = 0
    fib = 1
    while True:
        yield fib
        fib, prev_fib = fib + prev_fib, fib

f = fibonacci()
for num in range(10):
    print(next(f))
