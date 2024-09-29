'''
Три друга взяли вещи в поход. 
Сформируйте словарь, где ключ - имя друга,
а значение - кортеж вещей.
Ответьте на вопросы:
* Какие вещи взяли все три друга
* Какие вещи уникальны, есть только у одного друга
* Какие вещи есть у всех друзей кроме одного и имя того,
у кого данная вещь отсутствует
* Для решения используйте операции с множествами. 
Код должен расширяться на любое большое количество друзей.
'''

hike = {
    'Aaz': ('спички', 'спальник', 'дрова', 'топор'),
    'Skeeve': ('спальник', 'спички', 'вода', 'еда'),
    'Tananda': ('вода', 'спички', 'косметика'),
}

all_things = set()
for things in hike.values():
    # for thing in set(things):
    #     all_things.add(thing)
    all_things.update(things)

print(f'Полный список вещей: {all_things}')

unique_things = {}
for master_friend, master_things in hike.items():
    for slave_friend, slave_things in hike.items():
        if master_friend != slave_friend:
            if master_friend not in unique_things:
                unique_things[master_friend] = set(master_things) - set(slave_things)
            else:
                unique_things[master_friend] = unique_things[master_friend] - set(slave_things)  

print(f'Cписок уникальных вещей: {unique_things}')

double_things = set(all_things)
for things in unique_things.values():
    double_things -= things

print(f'Cписок дублирующих вещей: {double_things}')

for friend, things in hike.items():
    print(f'У {friend} отсутствуют {double_things - set(things)}')
    print(f'Второй вариант: {friend} - {(set(things) ^ double_things) - set(unique_things[friend])}')
