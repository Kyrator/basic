# TODO здесь писать код
list_player = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_list_players = []

for i in range(len(list_player)):
    if i % 2 == 0:
        new_list_players.append(list_player[i])

print(new_list_players)
