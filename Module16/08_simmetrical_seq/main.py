# TODO здесь писать код

count_number = int(input("Количество чисел: "))
temp_array = []
array = [int(input("Число: ")) for _ in range(count_number)]

n = len(array)
count = 0

for i in range(n):
    for j in range(n - 1, i, -1):
        if array[i] != array[j]:
            temp_array.insert(0, array[i])
            count += 1
            break

print("Последовательность: ", array)
print("Нужно приписать чисел:", len(temp_array))
print("Сами числа:", temp_array)
