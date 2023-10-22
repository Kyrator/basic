# TODO здесь писать код
def request_word():
    word_request = input("Введите слово: ").lower().title()
    synonym_request = ''
    for key, value in library_dict.items():
        if word_request == key:
            synonym_request = value
            print(f"Синоним: {synonym_request}")
            break
        elif word_request == value:
            synonym_request = key
            print(f"Синоним: {synonym_request}")
            break
    else:
        not_exist_word()
    return synonym_request


def not_exist_word():
    print("Такого слова в словаре нет.")
    request_word()


def requst_words(number):
    single_number = {
        1: 'первая', 2: 'вторая', 3: 'третья',
        4: 'четвертая', 5: 'пятая', 6: 'шестая',
        7: 'седьмая', 8: 'восьмая', 9: 'девятая',
        10: 'десятая', 11: 'одиннадцатая', 12: 'двенадцатая',
        13: 'тринадцатая', 14: 'четырнадцатая', 15: 'пятнадцатая',
        16: 'шестнадцатая', 17: 'семнадцатая', 18: 'восемнадцатая',
        19: 'девятнадцатая', 20: 'двадцатая', 30: 'тридцатая',
        40: 'сороковая', 50: 'пятьдесятая', 60: 'шестьдесятая',
        70: 'семьдесятая', 80: 'восемьдесятая', 90: 'девяностая',
        100: 'сотая'}

    couple_number = {
        20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят',
        70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто', 100: 'сто'}

    number += 1
    if 1 <= number <= 20 or number % 10 == 0:
        number_needs = single_number[number]
    else:
        number_second = number % 10
        number_first = number - number_second
        number_needs = couple_number[number_first] + " " + single_number[number_second]
    return number_needs


library_dict = dict()
i_count_couple = 0
count_couple = int(input("Введите количество пар слов: "))
while i_count_couple < count_couple:
    line = input(f"{requst_words(i_count_couple).title()} пара: ").split(" — ")
    if len(line) == 2:
        library_dict[line[0]] = line[1]
        i_count_couple += 1
    else:
        print("Некорректный ввод ")
        print("Попробуйте заново")

request_word()
