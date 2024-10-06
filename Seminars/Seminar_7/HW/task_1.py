'''
Напишите функцию группового переименования файлов. Она должна:

a. принимать параметр желаемое конечное имя файлов. 
При переименовании в конце имени добавляется порядковый номер.

b. принимать параметр количество цифр в порядковом номере.

c. принимать параметр расширение исходного файла. 
Переименование должно работать только для этих файлов внутри каталога.

d. принимать параметр расширение конечного файла.

e. принимать диапазон сохраняемого оригинального имени. 
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. 
Далее счётчик файлов и расширение.
'''
__all__ = ['rename_files']

import os
import shutil

# Создать тестовую папку
folder_name = 'homework_folder'
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
os.makedirs(folder_path)
input('Папка создана. Для продолжения нажмите Enter: ')


# Заполняем папку файлами
for num in range(1, 10):
    file_name_1 = f'file_{num}.txt'
    file_name_2 = f'file_{num}.csv'
    file_path_1 = os.path.join(folder_path, file_name_1)
    file_path_2 = os.path.join(folder_path, file_name_2)

    with (
        open(file_path_1, 'w', encoding='utf-8') as file_txt,
        open(file_path_2, 'w', encoding='utf-8') as file_csv
    ):
        file_txt.write(f'Запись в файл №{num}'),
        file_csv.write(f'Запись в файл №{num}')
input('Папка заполнена файлами. Для продолжения нажмите Enter: ')


def rename_files(rename_name: str = 'new_file', digits_name: int = 2, 
                file_ext: str = 'txt', new_ext: str = 'doc', *range_name: list[int]):
    # Сохраняем в переменную все названия файлов в заданной папке
    files = os.listdir('homework_folder')
    # Находим файлы с нужным разширением
    find_files = [file for file in files if file.endswith(file_ext)]

    for num, file in enumerate(find_files, 1):
        if range_name:
            old_name = file.strip('.' + file_ext)[range_name[0]-1:range_name[1]]
        else:
            old_name = ''
        new_name = old_name + rename_name + str(num).zfill(digits_name) + '.' + new_ext

        old_name_file = os.path.join(os.getcwd(), folder_name, file)
        new_name_file = os.path.join(os.getcwd(), folder_name, new_name)
        os.rename(old_name_file, new_name_file)


rename_files('some_file', 3, 'csv', 'apk', 1, 5, 8)
input('Файлы переименованы. Для продолжения нажмите Enter: ')
