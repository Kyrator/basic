def method_set(list_set):
    for i in list_set:
        if list_set.count(i) > 1:
            list_set.remove(i)
            print(i)
    return list_set


def merge_sorted_lists(list_1, list_2):
    list_1.extend(list_2)
    list_1 = method_set(list_1)
    return sorted(list_1)


# Пример использования:
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)
