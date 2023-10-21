goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# TODO здесь писать код

for title, sku in goods.items():
    for article, stuff in store.items():
        if sku == article:
            total_sku = 0
            count_sku = 0
            for i_stuff in stuff:
                total_sku += (i_stuff['quantity'] * i_stuff['price'])
                count_sku += i_stuff['quantity']
            print(f"{title} — {count_sku} штук, стоимость {total_sku} рубля")
