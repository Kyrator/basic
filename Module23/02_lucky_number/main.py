# TODO здесь писать код
import random

total = 0
try:
    while total < 777:
        number = int(input("Введите число: "))
        if random.randint(1, 13) == 5:
            raise TypeError
        with open('out_file.txt', 'a') as out_file:
            out_file.write(str(number) + "\n")
        total += number
except TypeError:
    print("Вас постигла неудача!")
else:
    print("Вы успешно выполнили условие для выхода из порочного цикла!")

print()
with open('out_file.txt', 'r') as out_file:
    print("Содержимое файла out_file.txt")
    for i_line in out_file:
        print(i_line, end='')
