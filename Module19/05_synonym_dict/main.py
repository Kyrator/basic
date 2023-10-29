# TODO здесь писать код


# Проверка слова в словаре
def request_word():
    word_request = input("Введите слово: ").lower()
    if library_dict.get(word_request, False):
        print(library_dict.get(word_request))
    else:
        not_exist_word()


# Если слова нет в словаре
def not_exist_word():
    print("Такого слова в словаре нет.")
    request_word()


library_dict = dict()
i_count_couple = 1
count_couple = int(input("Введите количество пар слов: "))
while i_count_couple <= count_couple:
    line_input = input(f"{i_count_couple} пара: ").lower().split('-')
    line_strip = [word.strip() for word in line_input]
    if len(line_strip) == 2:
        synonym_0, synonym_1 = line_strip
        library_dict[synonym_0] = synonym_1
        library_dict[synonym_1] = synonym_0
        i_count_couple += 1
    else:
        print("Некорректный ввод ")
        print("Попробуйте заново")

request_word()

# TODO: synonym_0: synonym_1, synonym_1: synonym_0
# .get() -- решите в одно обращение задачу поиска
