# TODO здесь писать код
import os.path

# При помощи модуля os (и функции join) сформируйте пути до файлов work_logs.txt и output.txt в папке data
# (output.txt может не быть в папке data, но его нужно будет там создать, при помощи кода)
input_file_path = os.path.abspath(os.path.join('data', 'work_logs.txt'))
output_file_path = os.path.abspath(os.path.join('data', 'output.txt'))


# Документация по join https://docs-python.ru/standart-library/modul-os-path-python/funktsija-join-modulja-os-path/

# Не забудьте проверить наличие файлов перед тем как начать работу с ними
# https://docs-python.ru/standart-library/modul-os-path-python/funktsija-exists-modulja-os-path/


def error_log_generator(input_file) -> str:
    with open(input_file, 'r') as log_file:
        for line_log in log_file:
            if 'ERROR' in line_log:
                yield line_log


def check_file_input(file_path):
    if os.path.exists(file_path):
        return True
    else:
        raise FileExistsError("Файла не существует")


print(input_file_path)
print(os.path.exists(input_file_path))
if check_file_input(input_file_path):
    with open(output_file_path, 'w') as output_file:
        for error_log in error_log_generator(input_file_path):
            output_file.write(error_log)
