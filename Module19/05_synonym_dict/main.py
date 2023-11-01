# TODO здесь писать код


library_dict = dict()
count_couple = int(input("Введите количество пар слов: "))

for i_count_couple in range(1, count_couple + 1):
    line_input = input(f"{i_count_couple} пара: ").title().split(' — ')
    synonym_0, synonym_1 = line_input
    library_dict[synonym_0] = synonym_1
    library_dict[synonym_1] = synonym_0

while True:
    word_request = input("Введите слово: ").title()
    # TODO: здесь тоже будет достаточно одного обращения к словарю
    print(library_dict.get(word_request,"Такого слова в словаре нет."))

