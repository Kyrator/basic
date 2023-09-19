def merge_sorted_lists(list_1, list_2):
    list_1.extend(list_2)
    list_1 = set(list_1)
    return sorted(list_1)


# Пример использования:
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)


