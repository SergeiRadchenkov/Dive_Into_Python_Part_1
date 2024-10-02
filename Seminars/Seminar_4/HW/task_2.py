'''
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
'''


def key_param(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        if value is None or isinstance(value, (int, float, tuple, str, bool, frozenset)):
            new_dict[value] = key
        else:
            new_dict[str(value)] = key
    return new_dict


result = key_param(first=1, second=2.0, third=[1, 2, 3], forth={4, 5, 6}, fifth=(7, 8, 9), sixth={'a': 1, 'b': 2})
print(result)
