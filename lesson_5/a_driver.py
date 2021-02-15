from abc import ABC, abstractmethod


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> list:
        """Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер"""
        pass

    @abstractmethod
    def write(self, data: list) -> None:
        """Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер"""
        pass


class JsonFileDriver(IStructureDriver):
    ...
