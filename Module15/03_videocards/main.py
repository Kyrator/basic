# TODO здесь писать код
def add_videocard():
    videocards_add = []
    count_videocard = int(input("Количество видеокарт: "))
    for id_position in range(1, count_videocard + 1):
        print(id_position, end="")
        vedeocard = int(input(" Видеокарта: "))
        videocards_add.append(vedeocard)
    return videocards_add


# search max of element in array
def search_max(videocards_search):
    max_videocard = 0
    for videocard in videocards_search:
        if max_videocard < videocard:
            max_videocard = videocard
    return max_videocard


# remove max element in array
def remove_max(list_videocards, max_videocard):
    new_list_videocards_remove = []
    for videocard in list_videocards:
        if videocard != max_videocard:
            new_list_videocards_remove.append(videocard)
    return new_list_videocards_remove


def main():
    videocards = add_videocard()
    max_videocard = search_max(videocards)
    new_list_videocards = remove_max(videocards, max_videocard)
    print("\nСтарый список видеокарт: [", *videocards, "]", sep=' ')
    print("Новый список видеокарт: [", *new_list_videocards, "]", sep=' ')


main()
