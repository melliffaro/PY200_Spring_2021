from abc import ABC, abstractmethod

from lesson_5.a_driver import IStructureDriver, JsonFileDriver


class DriverBuilder(ABC):
    @abstractmethod
    def build(self):
        ...


class JsonFileBuilder(DriverBuilder):
    DEFAULT_NAME = 'untitled.json'

    @classmethod
    def build(cls) -> IStructureDriver:
        filename = input('Введите название json файла: (.json)').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.json'):
            filename = f'{filename}.json'

        return JsonFileDriver(filename)


class FabricDriverBuilder:
    DRIVERS = {
        'json_file': JsonFileBuilder
    }
    DEFAULT_DRIVER = 'json_file'

    @classmethod
    def get_driver(cls):
        driver_name = input("Введите название драйвера: ")
        driver_name = driver_name or cls.DEFAULT_DRIVER

        return cls.DRIVERS[driver_name]().build()


if __name__ == '__main__':
    driver = FabricDriverBuilder.get_driver()
