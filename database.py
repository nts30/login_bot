import sqlite3 as sq


class Database:
    def __init__(self, db_file: str):
        self.connection = sq.connect(db_file)
        self.cursor = self.connection.cursor()
        self._create_db()

    def _create_db(self):
        """Создание таблицы

        :return:
        """
        if self.connection:
            print('Data base connected')
        with self.connection:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS users('
                                'id INTEGER PRIMARY KEY NOT NULL,'
                                'user_id INTEGER UNIQUE NOT NULL,'
                                'username VARCHAR(30),'
                                'time_sub NOT NULL DEFAULT 0,'
                                "signup VARCHAR(30) DEFAULT 'setusername')")

    def add_user(self, user_id):
        """Добавление пользователя в базу данных

        :param user_id: id пользователя
        :return:
        """
        try:
            with self.connection:
                self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
                self.connection.commit()
                return {
                    'status': 'OK'
                }
        except Exception as ex:
            return {
                'status': repr(ex)
            }

    def read_db(self):
        """Выборка всех значений из базы данных

        :return:
        """
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users")
            return result.fetchall()

    def user_exists(self, user_id):
        """Проверка существования пользователя

        :param user_id: id пользователя
        :return:
        """
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            return bool(result.fetchall())

    def set_username(self, user_id, username):
        """Отправка username-а пользователя

        :param user_id: id пользователя
        :param username: username пользователя
        :return:
        """
        with self.connection:
            self.cursor.execute("UPDATE users SET username = ? WHERE user_id = ?", (username, user_id))
            self.connection.commit()
            return True

    def get_signup(self, user_id):
        """Получение информации о том зарегистрирован ли пользователь

        :param user_id: id пользователя
        :return:
        """
        with self.connection:
            result = self.cursor.execute("SELECT signup FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return result[0][0]

    def delete_user(self, user_id):
        """Удаление пользователя

        :param user_id: id пользователя
        :return:
        """
        with self.connection:
            self.cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
            self.connection.commit()
            return True

    def set_signup(self, user_id, signup):
        """Подтверждение регистрации

        :param user_id: id пользователя
        :param signup: done
        :return:
        """
        with self.connection:
            self.cursor.execute("UPDATE users SET signup = ? WHERE user_id = ?", (signup, user_id))
            self.connection.commit()
            return True

    def get_username(self, user_id):
        """Получение username-а пользователя

        :param user_id: id пользователя
        :return:
        """
        with self.connection:
            result = self.cursor.execute("SELECT username FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return result[0][0]


