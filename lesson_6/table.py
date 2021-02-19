"""

backlog:
    - сделать Alter для обновления уже существующей таблицы
"""

from lesson_6.database_drivers import SqliteDB


class Table:
    SQLITE_FIELD = {
        int: "INTEGER",
        float: "REAL",
        str: 'TEXT',
    }

    def __init__(self, db_driver, table_name: str, **fields):
        self.table_name = table_name
        self.db_driver = db_driver
        self.fields = fields

        self.create_table()

    def create_table(self):
        sql = f"CREATE TABLE IF NOT EXISTS {self.table_name} (\n"
        sql += f"\t id INTEGER PRIMARY KEY AUTOINCREMENT,\n"

        for field, type_ in self.fields.items():
            sql += f"\t {field} {self.SQLITE_FIELD[type_]},\n"
        sql = sql[:-2] + "\n);"  # убираем последнюю запятую и перенос строки ( костыль:) ). Лучше использовать join

        # sql += ",\n".join(f"\t {field} {self.SQLITE_FIELD[type_]}" for field, type_ in self.fields.items())
        # sql += "\n);"
        print(sql)
        with self.db_driver as cursor:
            cursor.execute(sql)


if __name__ == '__main__':
    driver = SqliteDB('library.sqlite3')
    book_table = Table(driver, 'books', title=int, price=float)
