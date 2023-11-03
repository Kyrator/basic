# TODO здесь писать код
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': {
                'a': 'test depth level_3'
            }
        }
    }
}


def find_key(dictionary, key, depth_find=None):
    if depth_find is None:
        if key in dictionary:
            return dictionary[key]

        for value_dict_with_depth in dictionary.values():
            if isinstance(value_dict_with_depth, dict):
                item = find_key(value_dict_with_depth, key, depth_find)
                if item:
                    return item
    elif depth_find > 0:
        if key in dictionary:
            return dictionary[key]

        for value_dict_with_depth in dictionary.values():
            if isinstance(value_dict_with_depth, dict):
                item = find_key(value_dict_with_depth, key, depth_find - 1)
                if item:
                    return item
    else:
        return None


find_value = input("Введите искомый ключ: ")
question = input("Хотите ввести максимальную глубину? Y/N: ").lower()
if question == "y":
    depth = int(input("Введите максимальную глубину: "))
    print("Значение ключа:", find_key(site, find_value, depth))
elif question == "n":
    print("Значение ключа:", find_key(site, find_value))
