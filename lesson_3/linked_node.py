from typing import Any, Optional


class Node:
    """
    Внутренний класс, класса LinkedList.

    Пользователь напрямую не работает с узлами списка, узлами оперирует список.
    """

    def __init__(self, value: Any, next_: Optional['Node'] = None):
        """
        Создаем новый узел для односвязного списка

        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # Вызывается сеттер

    @property
    def next(self):
        """Getter возвращает следующий узел связного списка"""
        return self.__next

    @next.setter
    def next(self, next_: Optional['Node']):
        """Setter проверяет и устанавливает следующий узел связного списка"""
        if not isinstance(next_, self.__class__) and next_ is not None:
            msg = f"Устанавливаемое значение должно быть экземпляром класса {self.__class__.__name__} " \
                  f"или None, не {next_.__class__.__name__}"
            raise TypeError(msg)
        self.__next = next_


def linked_nodes(left: Node, right: Optional[Node]) -> None:
    left.next = right


if __name__ == '__main__':
    node_first = Node(1)
    node_second = Node(2)

    node_first.next = node_second

    # вспомогательная функция linked_nodes

