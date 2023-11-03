nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


# TODO здесь писать код
def out_list(*args):
    list_data = []
    for value in args:
        if isinstance(value, (dict, list)):
            list_data.extend(out_list(*value))
        else:
            list_data.append(value)
    return list_data


print("Ответ: {nice_list_new}".format(nice_list_new=out_list(nice_list)))
