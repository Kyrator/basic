# TODO здесь писать код

import os


def gen_files_path(path):
    """
    Функция рекурсивно проходит по
    всем каталогам указанной директории
    (по умолчанию — корневой диск), находит указанный
    пользователем каталог и генерирует пути всех встреченных файлов
    """

    for address, dir_name, files in os.walk(path):
        for file in files:
            print(os.path.join(address, file))


folder = os.path.abspath(os.path.join('..'))
gen_files_path(folder)
