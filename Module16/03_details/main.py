shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]


# TODO здесь писать код

def count_stuff(search_stuff, array_goods):
    goods_count = 0
    goods_total_cost = 0
    for i_goods in array_goods:
        if i_goods[0] == search_stuff:
            goods_count += 1
            goods_total_cost += i_goods[1]
    print("Кол-во деталей —", goods_count)  # 3
    print("Общая стоимость —", goods_total_cost)  # 4500


stuff = input("Название детали: ")  # седло

count_stuff(stuff, shop)
