'''
Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа
'''

data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 10500.2, False)
my_dict = {}

for item in data:
    key = my_dict.setdefault(type(item), [])
    key.append(item)

print(my_dict)
