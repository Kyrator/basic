# TODO здесь писать код
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# array_1 = [1, 2, 3, 4]
# array_2 = [2, 4]
# array_3 = [2, 3]


print("Задача 1:")

#     Решение без множеств: 2
# без использования множеств;
# найти элементы, которые есть в каждом списке;

community_list = list()

for i_array_1 in array_1:
    for i_array_2 in array_2:
        for i_array_3 in array_3:
            if i_array_3 == i_array_2 == i_array_1:
                community_list.append(i_array_3)
                break

print("\tРешение без множеств:", *community_list)

#     Решение с множествами: 2
# с использованием множеств.
# найти элементы, которые есть в каждом списке;

community_set = set(array_1) & set(array_2) & set(array_3)
print("\tРешение с множествами:", *community_set)

print("Задача 2:")

#     Решение без множеств: 1
# без использования множеств;
# найти элементы из первого списка, которых нет во втором и третьем списках.

array_1_list = array_1[:]
array_2_list = array_2[:]
array_3_list = array_3[:]

different_list = list()
for i_array_3 in array_3_list:
    for i_array_2 in array_2_list:
        for i_array_1 in array_1_list:
            if i_array_1 == i_array_2 or i_array_1 == i_array_3:
                array_1_list.remove(i_array_1)
                break

print("\tРешение без множеств:", *array_1_list)

#     Решение с множествами: 1
# с использованием множеств.
# найти элементы из первого списка, которых нет во втором и третьем списках.


different_set = set(array_1) - set(array_2) - set(array_3)
print("\tРешение с множествами:", *different_set)
