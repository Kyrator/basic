# TODO здесь писать код
def func_1(line):
    for i_line in range(len(line)):
        temp = (line[i_line::-1] + line[:i_line:-1])
        if temp == line:
            print("Можно сделать палиндромом")
            break
    else:
        print("Нельзя сделать палиндромом")


def main():
    line = input("Введите строку: ")
    func_1(line)


main()
