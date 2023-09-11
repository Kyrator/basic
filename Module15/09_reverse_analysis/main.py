# TODO здесь писать код

# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):
numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
number_len = len(numbers_list)

for index in range(number_len // 2 + 1):
    numbers_list[index], numbers_list[number_len - index - 1] = numbers_list[number_len - index - 1], numbers_list[
        index]

for number in numbers_list:
    if number % 2 != 0:
        numbers_list.remove(number)

print(numbers_list)
