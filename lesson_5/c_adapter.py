from typing import Any

import numpy as np


class ServerClass:
    """Код на стороне сервера менять не можем. Сервер выполняет вычисления очень быстро."""

    def find(self, data: list, value: Any) -> int:
        return data.index(value)


class NumpyAdapter:
    def __init__(self, np_array: np.ndarray):
        self.np_array = np_array

    def index(self, value: Any) -> int:
        """Делаем для numpy массива возможность работы с методом index"""
        ...


class DictAdapter(dict):
    def index(self, value: Any) -> int:
        ...


if __name__ == '__main__':
    server = ServerClass()

    list_ = [0, 1, 2, 3]
    print(server.find(list_, 1))

    numpy_adapter = NumpyAdapter(np.array(list_))
    print(server.find(numpy_adapter, 1))

    dict_adapter = DictAdapter({i: i for i in list_})
    print(server.find(dict_adapter, 1))
