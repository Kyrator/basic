# TODO здесь писать код

list_not_sorted = [1, 4, -3, 0, 10]
len_list = len(list_not_sorted)

for i in range(len_list):
    for j in range(len_list):
        if list_not_sorted[i] < list_not_sorted[j]:
            list_not_sorted[i], list_not_sorted[j] = list_not_sorted[j], list_not_sorted[i]

print(list_not_sorted)
