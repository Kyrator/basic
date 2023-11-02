# TODO здесь писать код
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def crypto(list_items):
    list_items = [value
                  for id_elem, value in enumerate(list_items)
                  if is_prime(id_elem)]
    return list_items


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))
