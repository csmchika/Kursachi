import mysql.connector
from mysql.connector import Error


class DataBase:

    def __init__(self):
        pass

    def create_connection(self, host_name, user_name, user_password):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password
            )
            print("Подключение к базе данных прошло успешно")
        except Error as e:
            print(f"Возникла ошибка {e}")

    def create_database(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            print("База данных успешно создана")
        except Error as e:
            print(f"Возникла ошибка {e}")

    def execute_query(self, query):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Таблица/Запись успешно вставлены")
        except Error as e:
            print(f"Возникла ошибка {e}")

    def delete_database(self, delete):
        cursor = self.connection.cursor()
        try:
            cursor.execute(delete)
            self.connection.commit()
            print("База данных успешно удалена")
        except Error as e:
            print(f"Возникла ошибка {e}")


kursovayadb = DataBase()
kursovayadb.create_connection("localhost", "root", "0000")
kursovayadb.create_database("CREATE DATABASE kursovayadb")
kursovayadb.execute_query('USE kursovayadb')

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  name TEXT NOT NULL,
  age INT,
  gender TEXT,
  nationality TEXT,
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""
kursovayadb.execute_query(create_users_table)

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
  id INT AUTO_INCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  user_id INTEGER NOT NULL,
  FOREIGN KEY fk_user_id (user_id) REFERENCES users(id),
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

kursovayadb.execute_query(create_posts_table)

create_users = """
INSERT INTO
  `users` (`name`, `age`, `gender`, `nationality`)
VALUES
  ('Лёха', 17, 'Муж.', 'Россия'),
  ('Алёна', 18, 'Жен.', 'Россия'),
  ('Евгения', 19, 'Жен.', 'Россия'),
  ('Антон', 20, 'Муж.', 'Россия'),
  ('Элизабет', 21, 'Жен.', 'Франция');
"""

kursovayadb.execute_query(create_users)

kursovayadb.delete_database('DROP DATABASE IF EXISTS kursovayadb')
