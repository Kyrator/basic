# TODO здесь писать код
line = input("Введите строку: ")
count_letter = 1
new_line = []


for i in range(len(line)):
    if i == len(line)-1:
        line_append = line[i] + str(count_letter)
        new_line.extend(line_append)
        count_letter = 1
    else:    
        if line[i] == line[i+1]:
            count_letter += 1
        elif line[i] != line[i+1]:
            line_append = line[i] + str(count_letter)
            new_line.extend(line_append)
            count_letter = 1


new_line = ''.join(new_line)
print(new_line)
