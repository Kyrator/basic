# TODO здесь писать код
# Функция для корректного создания вопроса при запросе слов
def requst_words(number):
    single_number = {
        1: 'первый', 2: 'второй', 3: 'третий',
        4: 'четвертый', 5: 'пятый', 6: 'шестой',
        7: 'седьмой', 8: 'восьмой', 9: 'девятый',
        10: 'десятый', 11: 'одиннадцатый', 12: 'двенадцатый',
        13: 'тринадцатый', 14: 'четырнадцатый', 15: 'пятнадцатый',
        16: 'шестнадцатый', 17: 'семнадцатый', 18: 'восемнадцатый',
        19: 'девятнадцатый', 20: 'двадцатый', 30: 'тридцатый',
        40: 'сороковой', 50: 'пятьдесятый', 60: 'шестьдесятый',
        70: 'семьдесятый', 80: 'восемьдесятый', 90: 'девяностый',
        100: 'сотый'}

    couple_number = {
        20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят',
        70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто', 100: 'сто'}

    number += 1
    if 1 <= number <= 20 or number % 10 == 0:
        number_needs = single_number[number]
    elif 21 <= number <= 109:
        number_second = number % 10
        number_first = number - number_second
        number_needs = couple_number[number_first] + " " + single_number[number_second]
    else:
        number_needs = str(number)
    return number_needs


quantity_order = int(input("Введите количество заказов: "))

order_dict = dict()
i_quantity_order = 0

while i_quantity_order < quantity_order:
    line = input(f"{requst_words(i_quantity_order).title()} заказ: ").split()  # Разделение строки через символ
    # указанный в примере
    client = line[0]
    pizza = line[1]
    quantity = int(line[2])

    if len(line) != 3:
        print("Некорректный ввод ")
        print("Попробуйте заново")
    else:
        if client not in order_dict:  # if a client doesn't exist in dictionary of order
            order_dict[client] = {pizza: quantity}
        else:
            if pizza in order_dict[client]:  # if a pizza exist in dictionary
                order_dict[client][pizza] += quantity
            else:  # if a pizza doesn't exist in dictionary of client
                order_dict[client][pizza] = quantity
        i_quantity_order += 1
print()

for key, value in sorted(order_dict.items()):
    print(key)
    for val_key, val_val in sorted(value.items()):
        print(f"\t{val_key}: {val_val}")
