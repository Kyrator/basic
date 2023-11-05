# TODO здесь писать код
file_input = 'numbers.txt'
file_output = 'answer.txt'
summa = 0


print("Содержимое файла {file}".format(file=file_input))
file_input_text = open(file_input, 'r', encoding='UTF-8')
for i_line in file_input_text:
    print(i_line, end='')
    for i_elem in i_line:
        if i_elem.isdigit():
            summa += int(i_elem)
file_input_text.close()
print()
file_output_text = open(file_output, 'w', encoding='UTF-8')
file_output_text.write(str(summa))
file_output_text.close()

print("Содержимое файла {file}".format(file=file_output))
file_input_text = open(file_output, 'r', encoding='UTF-8')
for i_out_line in file_input_text:
    print(i_out_line)
file_output_text.close()
