violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код
count_song = int(input("Сколько песен выбрать? "))
total_time_playlist = 0

for i_song in range(count_song):
    i_song += 1
    question = "Название " + str(i_song) + "-й песни: "
    answer = input(question)
    for i_violator_songs in violator_songs:
        if i_violator_songs[0] == answer:
            total_time_playlist += i_violator_songs[1]

print("\nОбщее время звучания песен:", round(total_time_playlist, 2), "минуты")
