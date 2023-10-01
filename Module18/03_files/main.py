# TODO здесь писать код
line_input = input('Название файла: ')
if line_input.startswith(("@", "№", "$", "%", "^", "&", "*", "(", ")")):
    print("Ошибка: название начинается недопустимым символом.")
else:
    if line_input.endswith(".txt") or line_input.endswith(".docx"):
        print("Файл назван верно.")// 
    else:
        print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")