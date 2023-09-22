# TODO здесь писать код

count_number = int(input("Количество чисел: "))
temp_array = []
array = [int(input("Число: ")) for _ in range(count_number)]

length = len(array)
count = 0

for i in range(length):
    for j in range(length - 1, i, -1):
        if array[i] != array[j]:
            temp_array.insert(0, array[i])
            count += 1
            break

print("Последовательность: ", array)
print("Нужно приписать чисел:", len(temp_array))
print("Сами числа:", temp_array)
