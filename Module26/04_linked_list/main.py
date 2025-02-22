# TODO здесь писать код
from typing import Any, Optional


class Node:
    def __init__(self, value: Optional[Any] = None, next_node: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next_node

    def __str__(self) -> str:
        return "Node [{value}]".format(
            value=str(self.value)
        )


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self) -> str:
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return f'{values}'.format(values=' '.join(values))
        return 'LinkedList []'

    def append(self, elem: Any) -> None:
        """Добавление элемента в список"""
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def get(self, index: int) -> Any:
        """Получение элемента по индексу в списке"""
        if not 0 <= index <= self.length:
            raise IndexError("Ошибка получения элемента по индексу!!! Выход за пределы массива")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def remove(self, index: int) -> None:
        """Удаление элемента в списке"""
        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length < index:
            raise IndexError("Ошибка удаления элемента по индексу!!! Выход за пределы массива")

        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1
            prev.next = cur_node.next
            self.length -= 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
