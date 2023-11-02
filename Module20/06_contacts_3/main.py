# TODO здесь писать код
def append_contact(contacts_append):
    surname, name = input("Введите имя и фамилию нового контакта (через пробел): ").title().split()
    if (surname, name) in contacts_append:
        print("Такой человек уже есть в контактах.")
    else:
        phone = int(input("Введите номер телефона: "))
        contacts_append[surname, name] = phone
    print("Текущий словарь контактов:", contacts_append)


def find_contact(contacts_find):
    flag_no_exist_person = True
    surname = input("Введите фамилию для поиска: ").title()
    for i_person in contacts_find:
        if surname in i_person:
            flag_no_exist_person = False
            print(i_person[0], i_person[1], contacts_find[i_person])
    if flag_no_exist_person:
        print("Такого человека нет в списке.")


contacts = dict()


def main():
    choose = input(
        """Введите номер действия: 
 1. Добавить контакт 
 2. Найти человека \n""")

    if choose == '1':
        append_contact(contacts)
        main()
    elif choose == '2':
        find_contact(contacts)
        main()
    else:
        print("Неверное значение")
        main()


main()
