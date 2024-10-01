'''
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
'''


def sum_between_indexes(my_list: list[int | float], i_1: int, i_2: int) -> int | float:
    i_max = max(i_1, i_2)
    i_max_plus_1 = i_max if i_max < len(my_list) else len(my_list)
    i_min = min(i_1, i_2)
    i_min = i_min if i_min >= 0 else 0
    return sum(my_list[i_min:i_max_plus_1])


numbers = [4, 8, 15, 16, 23, 42]
print(sum_between_indexes(numbers, -2,  10))
