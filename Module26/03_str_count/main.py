# TODO здесь писать код
import os
from typing import List


def count_lines(path: str) -> List[int, str]:
    """
    Реализуйте функцию-генератор, которая берёт все питоновские файлы
    в директории и вычисляет количество строк в каждом файле, игнорируя
    пустые строки и строки комментариев. По итогу функция-генератор должна
    с помощью yield каждый раз возвращать количество строк в очередном файле.
    """

    for address, dir_name, files in os.walk(path):
        count = 0
        for file in files:
            file_path = os.path.join(address, file)
            if file.endswith('.py'):
                with open(file_path, 'r') as open_file:
                    for i_line in open_file:
                        if not i_line.lstrip().startswith('#') and len(i_line.split()) != 0:
                            if not i_line.rstrip().endswith('\n') and len(i_line.split()) != 0:
                                count += 1
                yield count, file


user_folder = 'Module26'
user_path = os.path.abspath(os.path.join('..'))
print(user_path)
try:
    if os.path.exists(user_path):
        for line, count_file_path in count_lines(user_path):
            print(f'Количество строк в {count_file_path} {line} написан код')
    else:
        raise FileNotFoundError('Нет такой директории')
except FileNotFoundError as exc:
    print(exc)

# TODO: код упал
TypeError: Too many arguments for typing.List; actual 2, expected 1
