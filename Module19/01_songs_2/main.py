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
total_play_list = 0
how_mach_songs = int(input("Сколько песен выбрать? "))
for i_song in range(how_mach_songs):
    # TODO: это явно не одна строка =)
    sing = (input("Название {number} песни: ".format(number=(i_song + 1))))
    total_play_list += violator_songs.get(sing, 0)

print("Общее время звучания песен: {length} минуты".format(length=total_play_list))
