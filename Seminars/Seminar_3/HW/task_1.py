'''
Дан список повторяющихся элементов. 
Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
'''

data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42, 81, 36, 5, 18, 16, 55, 12, 7]

set_data = set(data)

for item in set(data):
    if item in data:
        data.remove(item)

set_data = set(data)

print(set_data)
