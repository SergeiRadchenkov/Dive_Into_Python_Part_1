'''
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.

Каждая группа включает файлы с несколькими расширениями.

В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''
from os import chdir
from pathlib import Path


def sort_files(path: str | Path, groups: dict[Path, list[str]] = None) -> None:
    chdir(path)
    if groups is None:
        groups = {
            Path('video'): ['mp4', 'avi', 'mkv', 'mov'],
            Path('image'): ['jpeg', 'jpg', 'png', 'gif'],
            Path('music'): ['mp3', 'wav', 'flac', 'm4a'],
        }
    reverse_groups = {}
    for directory, extension_list in groups.items():
        if not directory.is_dir():
            directory.mkdir()
        for extention in extension_list:
            reverse_groups[f'.{extention}'] = directory
    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups:
            file.replace(reverse_groups[file.suffix] / file.name)


if __name__ == '__main__':
    sort_files(Path('C:\\Users\\Nitro V15\\Desktop\\Dive_into_Python\\Seminars\\Seminar_7'))