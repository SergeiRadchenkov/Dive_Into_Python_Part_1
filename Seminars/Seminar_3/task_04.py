'''
Создайте вручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды.
'''
COUNT = 2

data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]

for item in set(data):
    if data.count(item) == COUNT:
        for _ in range(COUNT):
            data.remove(item)

print(data)
