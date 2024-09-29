'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
'''

BAG = 11.5

hike = {
    'спички': 0.05, 
    'спальник': 5.0, 
    'дрова': 8.0, 
    'топор': 2.0,
    'вода': 1.5,
    'еда': 2.0
}

# Вариант 1: с одним вариантом
weight = 0
list_things = []
for key, value in hike.items():
    if weight + value < BAG:
        weight += value
        list_things.append(key)
print(f'{weight} {list_things}')


# Вариант 2: все возможные варианты
items = list(hike.items())
num_items = len(items)

valid_combinations = []

for i in range(1 << num_items):
    current_weight = 0
    current_items = []

    for j in range(num_items):
        if i & (1 << j):
            current_weight += items[j][1]
            current_items.append(items[j][0])

    if current_weight <= BAG:
        valid_combinations.append((current_items, current_weight))

print(f'Все возможные варианты комплектации рюкзака:')
for index, (combination, total_weight) in enumerate(valid_combinations, start=1):
    print(f'Вариант {index}: {combination}, Общий вес: {total_weight:.2f} кг')