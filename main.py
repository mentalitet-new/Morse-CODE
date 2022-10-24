import json


class MorseCode:
    def __init__(self):
        super(MorseCode, self).__init__()
        self.__all_symbol_encode = []
        self.__cur = None
        self.__conn = None
        self.__total_symbol = []

    def __open_json_data(self):
        with open("connect.json", "r") as read:
            data = json.load(read)
        return data

    def __open_json_key(self):
        with open("key.json", "r") as read:
            data = json.load(read)
        return data

    def encode_algorithm(self, symbol_encode):
        data = self.__open_json_key()
        if symbol_encode is not None:
            self.__total_symbol.append(symbol_encode)
        else:
            pass

        for i in self.__total_symbol[0].upper():
            k = i
            if k in data["alphabet"]:
                self.__all_symbol_encode.append(data["alphabet"][k])
            elif k in data["numbers"]:
                self.__all_symbol_encode.append(data["numbers"][k])
        return self.__all_symbol_encode

    def decode_algorithm(self, symbol_decode):
        data = self.__open_json_key()
        decode_list_password = symbol_decode
        if decode_list_password is not None:
            for i in range(len(decode_list_password)):
                for key, value in data["alphabet"].items():
                    if value == decode_list_password[i]:
                        decode_list_password[i] = key
                for key, value in data["numbers"].items():
                    if value == decode_list_password[i]:
                        decode_list_password[i] = key
            return decode_list_password
        else:
            return None


if __name__ == '__main__':
    class_data = MorseCode()
    symbol = class_data.encode_algorithm("SOS123")
    print(symbol)
    print(class_data.decode_algorithm(symbol))

