
def count(number):
    count_number = 0
    while number:
        count_number += 1
        number //= 10
    return count_number


def summ(number):
    summ_number = 0
    while number:
        summ_number += number % 10
        number //= 10
    return summ_number


def input_number():
    number = int(input('Введите число: '))
    return number


def different(summnumber, countnumber):
    different_number = abs(summnumber - countnumber)
    return different_number


def main():
    number = input_number()
    summ_number = summ(number)
    print('Сумма чисел: ', summ_number)
    count_number = count(number)
    print('Количество цифр в числе: ', count_number)
    different_number = different(summ_number, count_number)
    print('Разность суммы и количества цифр: ', different_number)


main()
