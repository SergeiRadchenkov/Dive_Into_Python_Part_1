'''
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
'''

import sys

data = [42, 73.0, 'Hello, world!', True, 42, 'Hello world!', 256, 2 ** 8, 1, 'Привет, мир!']

for i, value in enumerate(data, 1):
    check_int = 'Похоже на целое число' if isinstance(value, int) else ''
    check_str = 'Похоже на строку' if isinstance(value, str) else ''
    print(f'{i}. Объект: {value}.\nАдрес в памяти: {id(value)}.\nРазмер в памяти: {sys.getsizeof(value)}.\nХэш объекта: {hash(value)}.\n{check_int}{check_str}\n')
