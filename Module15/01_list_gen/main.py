# TODO здесь писать код
def check(check_number):
    while check_number < 2:
        print("Введите положительное число.")
        check_number = int(input("Введите число: "))
    return check_number


number_range = check(int(input("Введите число: ")))
list_odd_number = []

for number in range(number_range + 1):
    if number % 2 != 0:
        list_odd_number.append(number)

print("Список из нечётных чисел от одного до N:", list_odd_number)
