guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код
def asked():
    print("Сейчас на вечеринке 5 человек:", guests)
    return input("Гость пришёл или ушёл? ")


answer = asked()
while answer != "Пора спать":
    if answer == "пришёл":
        new_guest = input("Имя гостя: ")
        if len(guests) < 6:
            print("Привет,", new_guest, "!")
            guests.append(new_guest)
        else:
            print("Прости,", new_guest, ", но мест нет.")
    elif answer == "ушёл":
        leave_guest = input("Имя гостя: ")
        print("Пока, ", leave_guest, "!")
        guests.remove(leave_guest)
    print()
    answer = asked()


print("\nВечеринка закончилась, все легли спать.")