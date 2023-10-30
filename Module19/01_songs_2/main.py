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

total_play_list = 0
how_mach_songs = int(input("Сколько песен выбрать? "))
for i_song in range(how_mach_songs):
    sing = (input("Название {number} песни: ".format(number=(i_song + 1))))
    # TODO: так все же зачем два обращения к словарю? достаточно одного будет
    if violator_songs.get(sing):
        total_play_list += violator_songs.get(sing, 0)
    else:
        print("Такой песни в плейлисте нет")

print(f"Общее время звучания песен: {round(total_play_list, 2)} минуты")
