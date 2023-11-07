# TODO здесь писать код
import os


def find_file(curn_path, size_file=0, subdir=0, file_count=0):
    for i_elem in os.listdir(curn_path):
        path = os.path.join(curn_path, i_elem)
        if os.path.isfile(path):
            size_file += os.path.getsize(path)
            file_count += 1
        elif os.path.isdir(path):
            subdir += 1
            size_file, subdir, file_count = (
                find_file(path, size_file, subdir, file_count))
    return size_file, subdir, file_count


folder_1 = 'Module14'

rel_path = os.path.join('../..', folder_1)
abs_path = os.path.abspath(rel_path)
print(abs_path)
size_folder, count_subdir, count_file = find_file(abs_path)
print("Размер каталога (в Кб): {size_file}".format(size_file=size_folder/1024))
print("Количество подкаталогов: {subdir}".format(subdir=count_subdir))
print("Количество файлов: {file_count}".format(file_count=count_file))
