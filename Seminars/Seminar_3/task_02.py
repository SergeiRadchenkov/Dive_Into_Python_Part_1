'''
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
* Целое положительное число
* Вещественное положительное или отрицательное число
* Строку в нижнем регистре, если в строке есть
хотябы одна заглавная буква
* Строку в верхнем регистре в остальных случаях
'''

data = input('Введите данные: ')

if data.isdigit():
    new_data = int(data)
elif data.count('.') == 1 and data.count('-') < 2 and '-' not in data[1:] and data.replace('.', '').replace('-', '').isdigit():
    new_data = float(data)
elif not data.islower():
    new_data = data.lower()
else:
    new_data = data.upper()

print(new_data)
