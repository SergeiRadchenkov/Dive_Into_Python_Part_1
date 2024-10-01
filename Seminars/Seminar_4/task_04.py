'''
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
'''

def sorting_list(my_list: list[int]):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                not_sorted = True


data_list = [8, 15, 42, 4, 23, 16]
sorting_list(data_list)
print(data_list)
