# TODO здесь писать код
def check_symbol (symbol):
    answer = False
    for letter in alphabet:
        if letter == symbol:
            answer = True
    return answer

def caeser_cipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33]) 
                 if check_symbol (sym) else sym
                 for sym in string
                 ]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
input_str = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

output_str = caeser_cipher(input_str, shift)
print(output_str)

# TODO: зачем if sym != ' ' else ' ', когда символы, которые не в алфавите лучше оставить "как есть"?
