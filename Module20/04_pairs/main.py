# TODO здесь писать код
import random


def random_list(n):
    return [random.randint(1, 10) for _ in range(n)]


def divide_list(original_list_div):
    return [(original_list_div[i], original_list_div[i + 1]) for i in range(0, len(original_list_div), 2)]


def divide_list2(original_list_div2):
    return list(zip(original_list_div2[::2], original_list_div2[1::2]))


original_list = random_list(10)
new_list = divide_list(original_list)
new_list_2 = divide_list2(original_list)
print("Оригинальный список:", original_list)
print("Новый список:", new_list)
print("Новый список (спобоб_2):", new_list_2)
