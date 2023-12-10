# TODO здесь писать код
import time
from typing import Dict


class LRUCache:
    def __init__(self, size: int) -> None:
        self.size = size
        self.dict_cache = {}
        self.timer = {}

    @property
    def cache(self) -> str:
        """Метод возвращает самый старый элемент"""
        return self.dict_cache[self.timer[min(self.timer.keys())]]

    @cache.setter
    def cache(self, new_elem: Dict[str, str]) -> None:
        """Метод добавляет новый элемент"""
        if len(self.dict_cache) >= self.size:
            self.elem_cache_del()

        key, value = new_elem
        self.dict_cache[key] = value
        self.timer[time.time()] = key

    def elem_cache_del(self) -> None:
        """Удаляем самый старый элемент """
        old_time = min(self.timer.keys())
        old_elem = self.timer[old_time]
        del self.dict_cache[old_elem]
        del self.timer[old_time]

    def get(self, elem: str) -> str:
        """Получаем значение по ключу"""
        return self.dict_cache[elem] + '\n'

    def print_cache(self) -> None:
        """Выводим текущий кэш"""
        print('LRU Cache:')
        for key, value in self.dict_cache.items():
            print('{key} : {value}'.format(key=key, value=value))
        print()


# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
