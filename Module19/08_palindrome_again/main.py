# TODO здесь писать код
# def func_1(line):
#     for i_line in range(len(line)):
#         temp = (line[i_line::-1] + line[:i_line:-1])
#         if temp == line:
#             print("Можно сделать палиндромом")
#             break
#     else:
#         print("Нельзя сделать палиндромом")
#
#
# def main():
#     line = input("Введите строку: ")
#     func_1(line)
#
#
# main()

def func_1(line):
    sym_dict = {}
    for sym in line:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    count = 0
    for sym_value in sym_dict.values():
        if sym_value % 2 != 0:
            count += 1
    return count <= 1


def main():
    line = input("Введите строку: ")
    if func_1(line):
        print("Можно сделать палиндромом")
    else:
        print("Нельзя сделать палиндромом")


main()
