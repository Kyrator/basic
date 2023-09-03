# TODO здесь писать код


def check(number):
    while number < 2:
        print("Введите число больше 1")
        number = int(input("Введите число: "))
    return number


def calculate(number):
    for i in range(2, number//2):
        if number % i == 0:
            number = i
            break
    return number

def main():
    number = int(input("Введите число: "))
    number = check(number)
    answer = calculate(number)
    print(f"Наименьший делитель, отличный от единицы: {answer}")


main()