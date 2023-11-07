# TODO здесь писать код
file = 'zen.txt'

with open(file, 'r', encoding='UTF-8') as file_zen:
    text = [i_line.strip() for i_line in file_zen]
    for i_text in text[::-1]:
        print(i_text)

