# TODO здесь писать код

def sum_data(*args):
    summa_data = 0
    for value in args:
        if isinstance(value, (dict, list)):
            summa_data += sum_data(*value)
        elif isinstance(value, (int, float)):
            summa_data += value
    return summa_data


summa1 = sum_data([[1, 2.44, [3]], [1], 3])
print("Ответ в консоли: {summa}".format(summa=summa1))

summa2 = sum_data(1, 2, 3, 4, 5)
print("Ответ в консоли: {summa}".format(summa=summa2))
