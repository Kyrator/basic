# TODO здесь писать код


def quick_sorted(list_a):
    if len(list_a) > 1:
        x = list_a[-1]
        low = [u for u in list_a if u < x]
        eq = [u for u in list_a if u == x]
        hi = [u for u in list_a if u > x]
        list_a = quick_sorted(low) + eq + quick_sorted(hi)
    return list_a


a_list = [5, 8, 9, 4, 2, 9, 1, 8]
print(quick_sorted(a_list))

b_list = [4, 9, 2, 7, 5]
print(quick_sorted(b_list))
