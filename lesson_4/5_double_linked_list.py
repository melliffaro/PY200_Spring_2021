"""
Двусвязный список на основе односвязного списка.

    Самостоятельное задание. В двусвязном списке должны быть следующие методы:
    - **`__str__`**
    - **`__repr__`**
    - **`__getitem__`**
    - **`__setitem__`**
    - **`__len__`**
    - **`insert`**
    - **`index`**
    - **`remove`**
    - **`append`**
    - **`__iter__`**

    Необязательно все эти методы должны быть переопределены в явном виде. По максимуму используйте
    наследование, если поведение списков в контексте реализации указанных метод схоже.
    С точки зрения наследования по минимуму перегружайте методы. При необходимости рефакторите базовый класс,
    чтобы локализовать части кода во вспомогательные функции, которые имеют различное поведение
    в связном и двусвязном списках.
    Стремитесь к минимизации кода в дочернем классе.

    Есть какой-то метод класса DoubleLinkedList хотите отработать в явном виде ещё раз, не возбраняется.
"""


from Link_list import LinkedList
from typing import Any, Optional
from Link_list import DoubleNode


class DoubleLinkedList(LinkedList):
    def __init__(self, head=None, tail=None, _size=0):
        super().__init__(head, _size)
        self.tail = tail

    def append(self, data):
        if self.tail is None:  # _size == 0
            item = DoubleNode(data, None, None)
            self.head = item
            self.tail = self.head
            self._size = 1
        else:
            item = DoubleNode(data, None, self.tail)
            self.tail.next_node = item
            self.tail = item
            self._size += 1

    def _node_iter_b(self):
        current_node = self.tail
        while current_node is not None:
            yield current_node
            current_node = current_node.prev_node

    def __str__(self):
        return "<-".join(str(node) for node in self._node_iter_b())

    def remove(self, node):
        '''Удаляет и возвращает узел, а также соединяет предыдущий и следующий'''
        next_node = node.next_node
        prev_node = node.prev_node

        prev_node.next_node = next_node
        next_node.prev_node = prev_node

        node.next_node = node.prev_node = None

        return node


if __name__ == '__main__':
    DLink = DoubleLinkedList()
    DLink.append('a')
    DLink.append('1')
    DLink.append('1')
    DLink.append('1')

    DLink2 = LinkedList()
    DLink2.append('a')
    DLink2.append('1')
    DLink2.append('1')
    DLink2.append('1')

    print(DLink)
    print(DLink2)