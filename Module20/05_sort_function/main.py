# TODO здесь писать код
def tpl_sort(values_tpl):
    for item in values_tpl:
        if not isinstance(item, int):
            return values_tpl
    return tuple(sorted(values_tpl))


# Пример вызова функции:

tpl = (6, 3, -1, 8, 4, 10, -5)

print(tpl_sort(tpl))
