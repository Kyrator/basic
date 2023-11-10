# TODO здесь писать код
count_letter = 0
line_count = 0
error_list = list()

try:
    with open('people.txt', 'r') as file_open:
        print("Содержимое файла people.txt")
        for i_line in file_open:
            try:
                length = len(i_line)
                line_count += 1
                if i_line.endswith('\n'):
                    length -= 1
                print(i_line, end='')
                count_letter += length
                if length <= 3:
                    error_list.append(line_count - 1)
                    raise NameError
            except NameError:
                error = ("Oшибка: менее трёх символов в строке {line}.\n".format(line=line_count - 1))
                with open('errors.log', 'a') as error_file:
                    error_file.write(error)
        print()

except FileNotFoundError as exc:
    print(exc, 'Такого файла не существует')

finally:
    print("Ответ в консоли:")
    with open('errors.log', 'r') as error_file:
        for i_line in error_file:
            print(i_line, end='')
    print("Общее количество символов: {count_letter}.".format(count_letter=count_letter))
