"""
    1. Реализовать класс JsonFileDriver, который будет описывать логику считывания (записи) элементов из (в) json файл.
    2. Реализовать класс SimpleFileDriver, который будет описывать логику считывания (записи) элементов из (в) файл.
    3. В блоке __main__ протестировать работу драйверов
"""

from typing import Sequence
from abc import ABC, abstractmethod
import json
import pickle
import yaml


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Sequence:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Sequence) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class JsonFileDriver(IStructureDriver):
    def __init__(self, filename: str):
        self._filename = filename

    def read(self) -> Sequence:
        with open(self._filename) as file:
            return json.load(file)

    def write(self, data: Sequence) -> None:
        with open(self._filename, "w") as file:
            json.dump(data, file)


class SimpleFileDriver(IStructureDriver):
    def __init__(self, filename: str):
        self._filename = filename

    def read(self) -> Sequence:
        with open(self._filename, 'rb') as file:
            return pickle.load(file)

    def write(self, data: Sequence) -> None:
        with open(self._filename, 'wb') as file:
            pickle.dump(data, file)

class YamlFileDriver(IStructureDriver):
    def __init__(self, filename: str):
        self._filename = filename

    def read(self) -> Sequence:
        with open(self._filename) as file:
            return yaml.load(file, yaml.SafeLoader)

    def write(self, data: Sequence) -> None:
        with open(self._filename, "w") as file:
            yaml.dump(data, file)

def main():
    driver: IStructureDriver = JsonFileDriver("some.json")

    a = [1, 2, 3, 4]
    driver.write(a)

    print(driver.read())

    driver: IStructureDriver = SimpleFileDriver("some.json")
    driver.write(a)

    print(driver.read())
    driver: IStructureDriver = YamlFileDriver("some.yaml")
    driver.write(a)

    print(driver.read())

if __name__ == '__main__':
    main()
