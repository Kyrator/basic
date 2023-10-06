# TODO здесь писать код
upper_letter = 1
digit_letter = 3
lock = True

while lock:
    count_upper = 0
    count_digit = 0
    password = input("Придумайте пароль: ")
    for i in password:
        if i.isupper():
            count_upper += 1
        elif i.isdigit():
            count_digit += 1
        else:
            pass
    if (count_digit < 3) or (count_upper < 1) or (len(password) < 8):
        print("Пароль ненадёжный. Попробуйте ещё раз.")
    else:
        lock = False

print("Это надёжный пароль")
