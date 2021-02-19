from lesson_6.database_drivers import SqliteDB


class BookLibrary:
    DATABASE = 'library.sqlite3'
    BOOKS_TABLE = 'books'

    def __init__(self):
        self.__driver = SqliteDB(self.DATABASE)

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

    def create_books_table(self):
        sql = f"""
        CREATE TABLE {self.BOOKS_TABLE} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ...
        ); 
        """

        self.__driver.execute(sql)

    def insert(self):
        # cur.executemany("insert into characters(c) values (?)", theIter)
        ...


if __name__ == '__main__':
    library = BookLibrary()
    library.get_book_by_year(5)

