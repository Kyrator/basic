# TODO здесь писать код
def chat_read():
    try:
        with open('messanger.txt', 'w') as messanger:
            messanger.seek(0)
            lines = messanger
            for line in lines:
                print(line, end='')
    except EnvironmentError:
        print("Система: Сообщений пока нет.\n")


def chat_add(name):
    message = input('Введите сообщение: ')
    with open('messanger.txt', 'a') as messanger:
        messanger.write(f"{name}: {message}\n")


user_name = input('Insrt name: ')
while True:
    try:
        choice_input = input("1. Посмотреть текущий текст чата."
                             "\n2. Отправить сообщение."
                             "\nВведите 1 / 2\n")
        if choice_input == '1':
            chat_read()
        elif choice_input == '2':
            chat_add(user_name)
        else:
            raise ValueError
        print()
    except ValueError:
        print("Система: Такого пункта выбора нет.\n")
