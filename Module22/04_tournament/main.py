# TODO здесь писать код

player_list = {}
info = []

file_input = open('first_tour.txt', 'r', encoding='UTF-8')
print("Содержимое файла first_tour.txt:")
for i_file in file_input:
    print(i_file, end='')
    info.append((str(i_file)).strip())

score_plan = int(info[0])

for i_player in info[1::]:
    surname, name, score_player = i_player.split()
    player_list[surname, name] = int(score_player)

file_input.close()

file_output = open('second_tour.txt', 'w', encoding='UTF-8')
all_second_tour = 0
position = 0
for value in player_list.values():
    if value > 80:
        all_second_tour += 1
file_output.write("{all_second_tour}\n".format(all_second_tour=all_second_tour))
for player, score in sorted(player_list.items(), key=lambda x: x[1], reverse=True):
    if score > score_plan:
        position += 1
        file_output.write("{position}) {name} {surname} {score}\n".format(
            position=position,
            name=(str(player[1][0]).upper() + '.'),
            surname=player[0],
            score=score
        ))

file_output.close()

print()
print()

file_input = open('second_tour.txt', 'r', encoding='UTF-8')
print("Содержимое файла second_tour.txt:")
for i_file in file_input:
    print(i_file, end='')
    info.append((str(i_file)).strip())
file_input.close()