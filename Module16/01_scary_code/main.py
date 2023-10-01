def del_element(array, element_del):
    temp_del_element = []
    for i_array in array:
        if element_del != i_array:
            temp_del_element.append(i_array)
    return temp_del_element


first = [1, 5, 3]
second = [1, 5, 1, 5]
third = [1, 3, 1, 5, 3, 3]

first.extend(second)
print("Результат работы программы:")
print("Количество цифр 5 при первом объединении: ", first.count(5))

# TODO: вы так не удалите все 5 из списка; подключите дебаггер, посмотрите, что происходит со списком в цикле
first = del_element(first, 5)
first.extend(third)

print("Количество цифр 3 при первом объединении: ", first.count(3))
print("Итоговый список:", first)

# TODO: работаем в рамках пройденного материала; срезы будут позже
