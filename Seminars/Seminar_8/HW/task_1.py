'''
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
'''
__all__ = ['traverse_directory', 'get_folder_size']

import os
import json
import csv
import pickle

PATH_DIR = 'C:\\Users\\Nitro V15\\Desktop\\Dive_into_Python\\Seminars\\Seminar_8'


def traverse_directory(directory):
    results = []
    for dir_path, dir_names, file_names in os.walk(directory):
        for file in file_names:
            file_path = os.path.join(dir_path, file)
            entry_file = {
                'Path': file_path,
                'Type': 'File',
                'Size': os.path.getsize(file_path)
            }
            results.append(entry_file)
        for dir in dir_names:
            dir_path_full = os.path.join(dir_path, dir)
            entry_dir = {
                'Path': dir_path_full,
                'Type': 'Directory',
                'Size': get_folder_size(dir_path_full)
            }
            results.append(entry_dir)
        return results
    

def get_folder_size(folder_path):
    total_size = 0
    for dir_path, dir_names, file_names in os.walk(folder_path):
        for file in file_names:
            file_path = os.path.join(dir_path, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size


def save_result_to_json(results, name_file):
    with open(name_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)


def save_result_to_csv(results, name_file):
    with open(name_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        writer.writerows(results)


def save_result_to_pickle(results, name_file):
    with open(name_file, 'wb') as f:
        pickle.dump(results, f)


if __name__ == '__main__':
    result = traverse_directory(PATH_DIR)
    save_result_to_json(result, 'results.json')
    save_result_to_csv(result, 'results.csv')
    save_result_to_pickle(result, 'results.pickle')
