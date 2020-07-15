import sqlite3
from data import DATA_PATH

connect = sqlite3.connect(DATA_PATH)
cursor = connect.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS user_data
                (id text, full_name text)""")
connect.commit()                  # создать таблицу если она не существует, в скобках передаем названия и типы столбцов

cursor.execute("""CREATE TABLE IF NOT EXISTS to_do
                (id text, note_name text, note_body text, note_date text)""")
connect.commit()                  # создать таблицу если она не существует, в скобках передаем названия и типы столбцов


class MyDataBase:
    def __init__(self):
        pass

    @staticmethod
    def in_todo(user_id: str, note_name: str, note_body: str, note_date: str):
        cursor.execute(f"""INSERT INTO to_do VALUES ('{user_id}','{note_name}','{note_body}','{note_date}')""")
        connect.commit()

    @staticmethod
    def select_todo(column, user_id):
        return cursor.execute(f"""SELECT {column} FROM to_do WHERE id = '{user_id}'""").fetchone()

        # выбрать колоку(или *) в таблице туду

    @staticmethod
    def update_todo(column, value, user_id):
        cursor.execute(f"""UPDATE to_do SET {column} = '{value}' WHERE id = '{user_id}'""")
        # в таблице туду установить новое значение где id = user_id

    @staticmethod
    def del_todo(user_id):
        cursor.execute(f"""DELETE FROM to_do WHERE id = '{user_id}'""")
        connect.commit()

    @staticmethod
    def in_data(user_id, full_name):
        cursor.execute(f"""SELECT id FROM user_data WHERE id={user_id}""")
        # выбрать столбец id в таблице user_data, где id=user_id
        if cursor.fetchone() is None:
            cursor.execute(f"""INSERT INTO to_do VALUES ('{user_id}','{full_name}')""")
            connect.commit()

        else:
            pass

    @staticmethod
    def del_data(user_id):
        cursor.execute(f"""DELETE FROM user_data WHERE id = '{user_id}')""")
        # Удалить из таблицы
        connect.commit()

    @staticmethod
    def close_connection():
        connect.close()


data_cursor = MyDataBase()
