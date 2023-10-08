# TODO здесь писать код
def max_words(words):
    max_count = 0
    word_max_words = ''
    for i_word in words:
        if len(i_word) > max_count:
            max_count = len(i_word)
            word_max_words = i_word
    return word_max_words


line_input = input('Введите строку: ').split()
word = max_words(line_input)
count_word = len(word)
print('Самое длинное слово: \"{word}\" '.format(word=word))
print("Длина этого слова: {count} символ.".format(count=count_word))
