'''
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
'''

def uni_list(text: str) -> list[int]:
    result = []
    for symbol in set(text):
        result.append(ord(symbol))
    return sorted(result, reverse=True)


print(uni_list('Каждый охотник желает знать, где сидит фазан'))