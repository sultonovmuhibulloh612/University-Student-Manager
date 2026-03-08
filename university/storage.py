from .classes import Student, Proforg, Starosta
import os
import sqlite3

class DBStorage:
    def __init__(self, date):
        self.date = date
        self.selfpath = 'data'
        self.Load()

    def Load(self):
        # Создаем папку data, если ее нет
        if not os.path.exists(self.selfpath):
            os.mkdir(self.selfpath)
        
        # ПРАВИЛЬНОЕ объединение путей
        db_path = os.path.join(self.selfpath, 'book.sqlite')
        
        # Подключение к БД с параметрами для Flask
        self.db = sqlite3.connect(
            db_path,
            detect_types=sqlite3.PARSE_DECLTYPES,
            check_same_thread=False
        )
        self.db.row_factory = sqlite3.Row  # Возвращать строки как словари
        self.dbc = self.db.cursor()
        
        # Создаем таблицу, если ее нет
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS book(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                passport_number TEXT,
                name TEXT,
                surname TEXT,
                age INTEGER,
                group_name TEXT,
                time TIMESTAMP,
                status_in_group TEXT,
                additional_data BLOB
            )
        """)
        self.db.commit()



    def Add(self, item):
        item.DBStore(self.db)
        self.db.commit()

    def GetItem(self, id, role=None):
        if id > 0:
            if role == "Студент":
                item = Student()
                self.dbc.execute("select * from book where id=?", (id,))
                item.DBLoad(self.dbc.fetchone())
                return item

            elif role == "Староста":
                item = Starosta()
                self.dbc.execute("select * from book where id=?", (id,))
                item.DBLoad(self.dbc.fetchone())
                return item

            elif role == "Профорг":
                item = Proforg()
                self.dbc.execute("select * from book where id=?", (id,))
                item.DBLoad(self.dbc.fetchone())
                return item

        else:
            if role == "Студент":
                item = Student()
                return item

            elif role == "Староста":
                item = Starosta()
                return item

            elif role == "Профорг":
                item = Proforg()
                return item

    def Delete(self, id):
        """Удаление объекта из базы данных по его ID."""
        self.db.execute("DELETE FROM book WHERE id=?", (id,))
        self.db.commit()
    
    def GetItems(self):
        self.dbc.execute("SELECT * FROM book ORDER BY id DESC")
        for r in self.dbc.fetchall():  # Проход по всем строкам результата
            print(r['status_in_group'])
            if r['status_in_group'] == "Студент":
                item = Student()
            elif r['status_in_group'] == "Староста":
                item = Starosta()
            elif r['status_in_group'] == "Профорг":
                item = Proforg()
            else:
                continue
            item.DBLoad(r)  # Загрузка данных в объект
            yield item
    def close(self):
        """Закрытие соединения с базой данных."""
        if self.db:
            self.db.close()