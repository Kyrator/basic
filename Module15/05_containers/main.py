# TODO здесь писать код


store = []
count_box = int(input("Количество контейнеров: "))

while count_box:
    weight_box = int(input("Введите вес контейнера: "))
    if weight_box <= 200:
        store.append(weight_box)
        count_box -= 1
    else:
        print("Слижком большой вес коробки, максимальное допустимое значение 200 кг.")

new_box = int(input("\nВведите вес нового контейнера: "))

store.append(new_box)
len_store = len(store)
for i in range(len_store):
    for j in range(len_store):
        if store[i] < store[j]:
            store[i], store[j] = store[j], store[i]

answer = len_store - store.index(new_box)

print("\nНомер, который получит новый контейнер:", answer)
