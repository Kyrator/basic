# TODO здесь писать код
def recursive(value):
  if value  == 1:
    print(value)

  else:
    recursive(value-1)
    print(value)

number_till = int(input("Введите num: "))
print()
recursive(number_till)
