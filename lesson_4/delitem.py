class MyList(list):

    def __delitem__(self, key):
        print(f'Удален объект по ключу {key}')

        super().__delitem__(key)

        ...


if __name__ == '__main__':
    list_ = MyList([1, 2, 3, 4])
    del list_[2]
    print(list_)
