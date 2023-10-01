# TODO здесь писать код
vowes_alphabet = "аоиеёэыуюя"
line = input("Введите текст: ")
list_vowels = [letter for letter in line for vowes in vowes_alphabet if letter == vowes ]
print("Список гласных букв: ", list_vowels)
print("Длина списка:", len(list_vowels))
