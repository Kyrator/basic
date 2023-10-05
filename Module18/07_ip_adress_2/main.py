# TODO здесь писать код

line_ip = input('Введите IP: ')
if line_ip.count('.') == 3:
    line_check = line_ip.split('.')
    for number in line_check:
      if not number.isdigit():
        print("{number} — это не целое число.".format(number=number))
        break
    for number in line_check:
      if int(number) > 255:
        print("{number} превышает 255.".format(number=number))
        break
    print("IP-адрес корректен.")
        

else:
  print("Адрес — это четыре числа, разделённые точками.")