from typing import Optional, Iterator

from faker import Faker

from lesson_6.database_drivers import SqliteDB


class BookLibrary:
    DATABASE = 'library.sqlite3'
    BOOKS_TABLE = 'books'

    def __init__(self):
        self.__driver = SqliteDB(self.DATABASE)

    def create_books_table(self):
        sql = f"""
        CREATE TABLE IF NOT EXISTS {self.BOOKS_TABLE} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- первичный ключ, идентифицирует записи в таблице БД
            title TEXT NOT NULL, -- название книг не может быть пустым
            isbn13 TEXT UNIQUE NOT NULL, -- идентификатор книги не может повторяться
            pages INTEGER NOT NULL, -- количество страниц в книге не может быть пустым
            year INTEGER NOT NULL, -- год издания книги не может быть пустым
            price REAL NOT NULL, -- цена книги не может быть пустой
            discount INTEGER -- а вот скидка может быть пустой
        ); 
        """
        with self.__driver as cursor:  # использование менеджера контекста для выполнения запроса
            cursor.execute(sql)

    def insert_book(self, title: str, isbn13: str, pages: int, year: int, price: float,
                    discount: Optional[int] = None):
        sql = f"""
        INSERT INTO {self.BOOKS_TABLE}(
            title,
            isbn13,
            pages,
            year,
            price,
            discount
        )
        VALUES (?, ?, ?, ?, ?, ?);  -- оставляем заглушки в виде ?
        """
        with self.__driver as cursor:  # использование менеджера контекста для выполнения запроса
            cursor.execute(sql, [title, isbn13, pages, year, price, discount])

    @staticmethod
    def book_generator(count: int = 10) -> Iterator[tuple]:
        """

        (
            title: str,
            isbn13: str,
            pages: int,
            year: int,
            price: float,
            discount: Optional[int] = None
        )

        :param count: количество книг для случайной генерации
        :return: Кортеж с описанием книги
        """
        fake = Faker()

        for _ in range(count):
            fake_title = fake.pystr()
            fake_isbn13 = fake.isbn13()
            fake_page = fake.pyint(min_value=0, max_value=1000)
            fake_year = fake.pyint(min_value=1600, max_value=2021)
            fake_price = fake.pyfloat(min_value=0, max_value=10000, right_digits=2)
            fake_discount = fake.random_element([None, *range(10, 91, 10)])

            yield fake_title, fake_isbn13, fake_page, fake_year, fake_price, fake_discount

    def init_books(self, count):
        sql = f"""
        INSERT INTO {self.BOOKS_TABLE}(
            title,
            isbn13,
            pages,
            year,
            price,
            discount
        )
        VALUES (?, ?, ?, ?, ?, ?);  -- оставляем заглушки в виде ?
        """

        with self.__driver as cursor:  # использование менеджера контекста для выполнения запроса
            cursor.executemany(sql, self.book_generator(count))

    def get_book_by_year(self, year):
        sql = f"""
        SELECT *
        FROM {self.BOOKS_TABLE}
        WHERE year = {year}
        """

        with self.__driver as cursor:
            return cursor.execute(sql)

    def get_book_by_title(self, title):
        ...

    def get_book_by_price(self, price):
        ...

    def insert(self):
        # cur.executemany("insert into characters(c) values (?)", theIter)
        ...


if __name__ == '__main__':
    library = BookLibrary()
    # library.create_books_table()
    #
    # library.insert_book('test', '1221-3212-33', 20, 2020, 34.56)

    # for book in library.book_generator():
    #     print(book)

    library.init_books(100)
