# TODO здесь писать код
def count_letter_eng(text_func):
    all_dict = 0
    context_dict_func = {}
    rezualt_dict_func = {}
    for letter in text_func.lower():
        if letter.isalpha():
            all_dict += 1
            if letter in context_dict_func:
                context_dict_func[letter] += 1
            else:
                context_dict_func[letter] = 1
    for key_letter_func, value_letter_func in context_dict_func.items():
        if value_letter_func / all_dict in rezualt_dict_func:
            rezualt_dict_func[value_letter_func / all_dict].append(key_letter_func)
        else:
            rezualt_dict_func[value_letter_func / all_dict] = [key_letter_func]
    return rezualt_dict_func


context = "Mama myla ramu."

file_input = open('text.txt', 'w')
file_input.write(context)
file_input.close()

file_input = open('text.txt', 'r')
print("Содержимое файла text.txt:")
text = file_input.read()
print(text)
context_dict = count_letter_eng(text)
file_input.close()

print()
file_output = open('analysis.txt', 'w')
for key_letter, value_letter in sorted(context_dict.items(), reverse=True):
    for value in sorted(value_letter):
        file_output.write("{letter} {statistic}\n"
                          .format(letter=value, statistic=round(key_letter, 4)))

file_output.close()

file_output = open('analysis.txt', 'r')
print("Содержимое файла analysis.txt:")
for i_file in file_output:
    print(i_file, end='')
file_output.close()
