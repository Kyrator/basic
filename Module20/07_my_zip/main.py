# TODO здесь писать код
line = 'abcde'
tuple_line = (10, 20, 30, 40, 50)


def minimal(line_1, line_2):
    return min(len(line_1), len(line_2))


itog = ((line[index_elem], tuple_line[index_elem])
        for index_elem in range(minimal(line, tuple_line)))

print("Результат:")
print(itog)
for i in itog:
    print(i)
