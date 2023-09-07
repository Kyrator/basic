# TODO здесь писать код


def calculate_years(first_year, second_year):
    print(f"Годы от {first_year} до {second_year} с тремя одинаковыми цифрами:")
    for year in range(first_year, second_year + 1):
        count = 0
        temp = year
        while temp >= 10:
            number = temp % 10
            temp //= 10
            for i in str(temp):
                if int(i) == number:
                    count += 1
        if count > 2:
            print(year)


def main():
    first_year = int(input("Введите первый год: "))
    second_year = int(input("Введите второй год: "))
    calculate_years(first_year, second_year)


main()
