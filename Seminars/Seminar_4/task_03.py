'''
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
'''

def range_unicode(text: str) -> dict[str, int]:
    first, second = map(int, text.split())
    result = {}
    for number in range(min(first, second), max(first, second) + 1):
        result[chr(number)] = number
    return result


print(range_unicode('1 10'))