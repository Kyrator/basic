# TODO здесь писать код
def check_lines(line_1, line_2):
    compare = False
    change = 0
    num = line_2.find(line_1[0])
    line_2 = line_2[num:] + line_2[:num]
    if line_1 == line_2:
        compare = True
        change = len(line_2) - num
    return compare, change


line_first = input("Первая строка: ")
line_second = input("Вторая строка: ")

passed, shift = check_lines(line_first, line_second)

if passed:
    print("Первая строка получается из второй со сдвигом {number}.".format(number=shift))
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
