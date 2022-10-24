import psycopg2
import json


class PasswordsGenerator:
    def __init__(self):
        super(PasswordsGenerator, self).__init__()
        self.__cur = None
        self.__conn = None
        self.__total_symbol = []

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
        return rec

    def encode_algorithm(self, symbol):
        all_symbol = []
        with open("key.json", "r") as read:
            data = json.load(read)

        if symbol is not None:
            self.__total_symbol.append(symbol)
        else:
            pass

        for i in self.__total_symbol[0]:
            k = i
            if k in data["alphabet"]:
                all_symbol.append(data["alphabet"][k])
            elif k in data["numbers"]:
                all_symbol.append(data["numbers"][k])
        return all_symbol


if __name__ == '__main__':
    class_data = PasswordsGenerator()
    class_data.start_connect()
    class_data.fetch_all()
    print(class_data.encode_algorithm("1AD12"))

    print(class_data.encode_algorithm("1AD12"))

