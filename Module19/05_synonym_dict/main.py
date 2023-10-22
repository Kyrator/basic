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


words = {
    1: 'первая', 2: 'вторая', 3: 'третья',
    4: 'четвертая', 5: 'пятая', 6: 'шесть',
    7: 'седьмая', 8: 'восьмая', 9: 'девятая',
    10: 'десятая', 11: 'одиннадцатая', 12: 'двенадцатая',
    13: 'тринадцатая', 14: 'четырнадцатая', 15: 'пятнадцатая',
    16: 'шестнадцатая', 17: 'семнадцатая', 18: 'восемнадцатая',
    19: 'девятнадцатая', 20: 'двадцатая'}

library_dict = dict()

count_couple = int(input("Введите количество пар слов: "))
for i_count_couple in range(count_couple):
    line = input(f'{words[i_count_couple + 1].title()} пара: ').split()
    library_dict[line[0]] = line[2]

request_word()
