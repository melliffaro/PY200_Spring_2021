from lesson_5.a_linkedlist import LinkedList
from lesson_5.a_driver import IStructureDriver, JsonFileDriver


class LinkedListWithDriver(LinkedList):
    def __init__(self, data, driver: IStructureDriver = None):
        super().__init__(data)
        self.__driver = driver

    def read(self):
        """Взять драйвер и считать из него информацию в LinkedList"""
        ...

    def write(self):
        """Взять драйвер и записать в него информацию из LinkedList"""
        ...


if __name__ == '__main__':
    ll = LinkedListWithDriver([1, 2, 3, 4, 5])

    ll.write()
