site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


# TODO здесь писать код

def print_site(context, device):
    for key, value in context.items():
        if 'телефон' in value:
            value = value.split()
            value[value.index('телефон')] = device
            context[key] = ' '.join(value)
        elif 'iPhone' in value:
            value = value.split()
            value[value.index('iPhone')] = device
            context[key] = ' '.join(value)
        if isinstance(value, dict):
            print_site(value, device)
    return context


count_site = int(input("Сколько сайтов: "))
for i_count in range(1, count_site + 1):
    brand = input("Введите название продукта для нового сайта: ")
    new_site = print_site(site, brand)
    print("Сайт для {brand}: \n{new_site}".format(brand=brand, new_site=new_site))

# TODO: а где глубокое копирование?
