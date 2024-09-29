'''
Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.

Два варианта решения: короткое и длинное
'''

data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]
new_data = list(set(data))
print(new_data)


new_list = []
for item in data:
    if item not in new_list:
        new_list.append(item)
print(new_list)
