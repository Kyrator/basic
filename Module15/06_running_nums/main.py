# TODO здесь писать код

old_list = [1, 4, -3, 0, 10]
new_list = []

move = int(input("Сдвиг: "))
print("Изначальный список:", old_list)
count_list = len(old_list)
move = move % count_list  # don't jump behind border
for i in range(count_list):
    new_list.append(old_list[(i - move) % count_list])

print('Сдвинутый список:', new_list)
