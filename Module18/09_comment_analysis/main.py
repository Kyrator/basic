# TODO здесь писать код
def count_uppercase_lowercase(text):
    lower = 0
    upper = 0
    for letter in text:
        if letter.islower():
            lower += 1
        elif letter.isupper():
            upper += 1
    return upper, lower

# Пример использования:
text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
