violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

# TODO здесь писать код -- вообще бесполезная штука
question_songs = {
    1: "первой",
    2: "второй",
    3: "третей",
    4: "четвертой",
    5: "пятой",
    6: "шестой",
    7: "седьмой",
    8: "восьмой",
    9: "девятой"
}

how_mach_songs = int(input("Сколько песен выбрать? "))
play_list = [] -- и зачем вам допсписок?
for i_song in range(how_mach_songs):
    sing = (input("Название {number} песни: ".format(number=question_songs[i_song + 1])))
    sing_length = violator_songs.get(sing, 0)
    play_list.append(sing_length)

total_play_list = sum(play_list)
print("Общее время звучания песен: {length} минуты".format(length=total_play_list))
