# TODO здесь писать код
class Property:
    def __init__(self, worth):
        self.__worth = worth

    def get_worth(self):
        return self.__worth

    def calc_tax(self) -> int:
        property_worth = self.__worth
        return property_worth / 1


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.tax = 1000

    @property
    def calc_tax(self) -> int:
        return self.get_worth() / self.tax


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.tax = 200

    @property
    def calc_tax(self) -> int:
        return self.get_worth() / self.tax


class CountryHouse(Property):
    def __init__(self, worth: int):
        super().__init__(worth)
        self.tax = 500

    @property
    def calc_tax(self) -> int:
        return self.get_worth() / self.tax


class Citizen:
    __bank_count = []
    __apartment = []
    __car = []
    __country_house = []

    def __init__(self, name):
        self.name = name

    def __input_bank_count(self):
        try:
            bank_count_amount = int(input("Введите количество счетов: "))
            self.__bank_count = [int(input(f'Введите количество его денег на {i_count + 1} счету: '))
                                 for i_count in range(bank_count_amount)]
        except ValueError:
            print("Ошибка ввода")

    def __input_apartment(self):
        try:
            apartment_amount = int(input("Введите количество квартир: "))
            self.__apartment = [Apartment(int(input(f'Введите стоимость {i_count + 1} квартиры: ')))
                                for i_count in range(apartment_amount)]
        except ValueError:
            print("Ошибка ввода")

    def __input_car(self):
        try:
            car_amount = int(input("Введите количество машин: "))
            self.__car = [Car(int(input(f'Введите стоимость {i_count + 1} машины: ')))
                          for i_count in range(car_amount)]
        except ValueError:
            print("Ошибка ввода")

    def __input_country_house(self):
        try:
            country_house_amount = int(input("Введите количество загородных домов: "))
            self.__country_house = [CountryHouse(int(input(f'Введите стоимость {i_count + 1} дома: ')))
                                    for i_count in range(country_house_amount)]
        except ValueError:
            print("Ошибка ввода")

    def input_info(self):
        self.__input_bank_count()
        self.__input_apartment()
        self.__input_car()
        self.__input_country_house()

    def get_info_about_tax(self):
        bank_all = sum(self.__bank_count)
        tax_apart = sum(apart.calc_tax for apart in self.__apartment)
        tax_car = sum(car.calc_tax for car in self.__car)
        tax_country_house = sum(country.calc_tax for country in self.__country_house)

        print(
            "\nНалог на квартиру = ", tax_apart,
            "\nНалог на машину = ", tax_car,
            "\nНалог на загородный дом = ", tax_country_house,
            "\n"
        )
        all_tax = tax_apart + tax_car + tax_country_house
        if bank_all < all_tax:
            print(
                f"Денег {bank_all} не хватает для оплты налогов {round(all_tax, 2)}. Внесите деньги на расчетный счет")
        else:
            print(f"Денег {bank_all} хватает для оплаты налогов {round(all_tax, 2)}. Можно спать спокойно.")


user_1 = Citizen("Иванов Иван Иванович")
user_1.input_info()
user_1.get_info_about_tax()
