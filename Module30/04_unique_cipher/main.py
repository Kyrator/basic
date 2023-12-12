# TODO здесь писать код
from collections import Counter


def count_unique_characters(line: str) -> int:
    """ Функция принимает строчку,
  переводит в нижний регистр,
  получает словарь символов,
  отфильтровывает количество значения которые равны единице
  и возвращает
  """
    return sum(filter(lambda x: x == 1, (Counter(line.lower()).values())))


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
