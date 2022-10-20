import psycopg2
import json


class PasswordsGenerator:
    def __init__(self):
        super(PasswordsGenerator, self).__init__()
        self.__cur = None
        self.__conn = None

    def __open_json(self):
        with open("data.json", "r") as read:
            data = json.load(read)
        return data

    def start_connect(self):
        self.__conn = psycopg2.connect(f'dbname={self.__open_json()["dbname"]} user={self.__open_json()["user"]} '
                                     f'password={self.__open_json()["password"]} '
                                     f'host={self.__open_json()["host"]} '
                                     f'port={self.__open_json()["port"]} ')
        self.__cur = self.__conn.cursor()

    def fetch_all(self):
        self.__cur.execute("SELECT * FROM information")
        rec = self.__cur.fetchall()
        print(rec)


if __name__ == '__main__':
    class_data = PasswordsGenerator()
    class_data.start_connect()
    class_data.fetch_all()