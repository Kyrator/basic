def reverse(elements):
    temp = []
    for element in elements:
        temp.insert(0, element)
    return temp


first = [1, 5, 3]
second = [1, 5, 1, 5]
third = [1, 3, 1, 5, 3, 3]

first.extend(second)
print("Результат работы программы:")
print("Количество цифр 5 при первом объединении: ", first.count(5))

first = reverse(first)

for i_first in first:
    if i_first == 5:
        first.remove(5)

first = reverse(first)

first.extend(third)

print("Количество цифр 3 при первом объединении: ", first.count(3))
print("Итоговый список:", first)

# TODO: работаем в рамках пройденного материала; срезы будут позже
