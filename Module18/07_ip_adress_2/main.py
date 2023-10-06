# TODO здесь писать код
def test_1(ip_line):
    test_1_result = True
    if ip_line.count('.') != 3:
        print("Адрес — это четыре числа, разделённые точками.")
        test_1_result = False
    return test_1_result


def test_2(ip_line):
    test_2_result = True
    for number in ip_line:
        if not number.isdigit():
            print("{number} — это не целое число.".format(number=number))
            test_2_result = False
            break
    return test_2_result


def test_3(ip_line):
    test_3_result = True
    for number in ip_line:
        if int(number) > 255:
            print("{number} превышает 255.".format(number=number))
            test_3_result = False
    return test_3_result


# test_array = ["128.16.35.a4", "240.127.56.340", "34.56.42,5", "128.0.0.255"]
def main():
    # for line_ip in test_array:
    line_ip = input('Введите IP: ')
    if test_1(line_ip):
        line_ip = line_ip.split('.')
        if test_2(line_ip):
            if test_3(line_ip):
                print("IP-адрес корректен.")


main()
