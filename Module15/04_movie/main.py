films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# TODO здесь писать код

favorite_films = []

count_favorite_films = int(input("Сколько фильмов хотите добавить? "))

while count_favorite_films:
    film = input("Введите название фильма: ")
    if film not in films:
        print(f"Ошибка: фильма {film} у нас нет :(")
    elif film not in favorite_films:
        favorite_films.append(film)
        count_favorite_films -= 1
    else:
        print(f"{film} уже есть в списке любимых.")

print("Ваш список любимых фильмов: ", ", ".join(favorite_films))
