# TODO здесь писать код
rollers_list = []
man_list = []
count_couples = 0

rollers = int(input("Кол-во коньков: "))  # 4

for i_roller in range(rollers):
    i_roller += 1
    question_roller = "Размер " + str(i_roller) + "-й пары: "
    answer_roller = input(question_roller)
    rollers_list.append(answer_roller)

mans = int(input("\nКол-во людей: "))  # 3

for i_man in range(mans):
    i_man += 1
    question_man = "Размер ноги " + str(i_man) + "-го человека: "
    answer_man = input(question_man)
    man_list.append(answer_man)

count_couples = 0

for man in man_list:
    for roller in rollers_list:
        if roller == man:
            rollers_list.remove(man)
            count_couples += 1
            break

print("\nНаибольшее кол-во людей, которые могут взять ролики: ", count_couples)
