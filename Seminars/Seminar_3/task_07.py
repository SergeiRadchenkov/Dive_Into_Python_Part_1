'''
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.
'''

data = input('Ведите строку текста: ')

my_dict1 = {}
for char in set(data):
    my_dict1[char] = data.count(char)
print(my_dict1)


my_dict2 = {}
for char in data:
    if char not in my_dict2:
        my_dict2[char] = 1
    else:
        my_dict2[char] += 1
print(my_dict2)


my_dict3 = {}
for char in data:
    my_dict3[char] = my_dict3.get(char, 0) + 1
print(my_dict3)