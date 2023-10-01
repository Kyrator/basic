# TODO здесь писать код

humans = int(input("Количество человек: "))
numer = int(input("Какое число в считалке? "))
print("Значит, выбывает каждый ", numer, "-й человек", sep="")

humans_list = [i_man + 1 for i_man in range(humans)]
temp_number = humans_list[0]
temp = 0
print()

while len(humans_list) > 1:
    print("Текущий круг людей: ", humans_list)
    print("Начало счёта с номера ", humans_list[temp])
    temp_number = (((numer - 1) + temp) % len(humans_list))
    print("Выбывает человек под номером", humans_list[temp_number])
    humans_list.remove(humans_list[temp_number])
    temp = temp_number % len(humans_list)
    print()

print("Остался человек под номером", humans_list[0])
