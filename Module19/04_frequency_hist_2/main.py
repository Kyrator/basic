# TODO здесь писать код

dictionary = dict()
line = input("Введите текст: ")
for sym in line:
    if sym in dictionary:
        dictionary[sym] += 1
    else:
        dictionary[sym] = 1
print("Оригинальный словарь частот:")
for key, value in dictionary.items():
    print(key, ":", value, sep='')

invert_dict = dict()
for key, value in dictionary.items():
    if value in invert_dict:
        invert_dict[value] += [key]
    else:
        invert_dict[value] = [key]
for invert_key, invert_value in invert_dict.items():
    print(f"{invert_key} : {invert_value}")
