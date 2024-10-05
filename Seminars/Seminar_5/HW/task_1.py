'''
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''

file_path = 'C:/Users/Nitro V15/Desktop/Dive_into_Python/Seminars/Seminar_5/HW/task_1.py'

def path_tuple(any_path: str) -> tuple:
    file_name = file_path.split('/')[-1]
    file_to_path = file_path[:-len(file_name)]
    file_name, resolution = file_name.split('.')
    return(file_to_path, file_name, '.' + resolution)


result = path_tuple(file_path)
print(result)
