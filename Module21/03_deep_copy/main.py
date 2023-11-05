import copy

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


def print_deep(site_deep, depth=0):
    for key, value in site_deep.items():
        print('\t' * depth, ("<" + key + ">"))
        if isinstance(value, dict):
            print_deep(value, depth + 1)
            print('\t' * depth, ("</" + key + ">"))
        else:
            print('\t' * (depth + 1), ''.join(value))
            print('\t' * depth, ("</" + key + ">"))

count_site = int(input("Сколько сайтов: "))
for _ in range(count_site):
    brand = input("Введите название продукта для нового сайта: ")
    site_copy = copy.deepcopy(site)
    new_site = print_site(site_copy, brand)
    # print(id(site), id(new_site))
    print("Сайт для {brand}:".format(brand=brand))
    print_deep(new_site)

# TODO: а где глубокое копирование?
