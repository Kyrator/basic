# TODO здесь писать код
import random

team_first = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]
team_second = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]
team_winners = [team_first[i_player]
                if team_first[i_player] > team_second[i_player]
                else team_second[i_player]
                for i_player in range(20)]

print("Первая команда: ", team_first)
print("Вторая команда: ", team_second)
print("Победители тура: ", team_winners)
