# TODO здесь писать код
class Date:
    """Класс Дата"""
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """Функция вывода"""
        return "День: 10	Месяц: 12	Год: 2077".format(
            self.day, self.month, self.year
        )

    @classmethod
    def is_date_valid(cls, dates: str) -> bool:
        """Функция проверяет числа даты на корректность"""
        day, month, year = map(int, dates.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999

    @classmethod
    def from_string(cls, dates: str) -> 'Date':
        """Функция устанавливает числа даты """
        day, month, year = map(int, dates.split('-'))
        return cls(day, month, year)


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
