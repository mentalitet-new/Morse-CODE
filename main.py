import json
import time

import winsound


class MorseCode:
    def __init__(self):
        super(MorseCode, self).__init__()
        self.__all_symbol_encode = []
        self.__total_symbol = []

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

    def play_beep(self, dot_dash):
        for i in dot_dash:
            print(i)
            if i == "*":
                winsound.Beep(800, 160)
            elif i == "-":
                winsound.Beep(800, 310)
            elif i == "d":
                time.sleep(0.21)


if __name__ == '__main__':
    class_data = MorseCode()
    symbol = class_data.encode_algorithm("SOS")
    # print(symbol)
    # print(class_data.decode_algorithm(symbol))
    join_symbol = "d".join(symbol)
    print(join_symbol)
    class_data.play_beep(join_symbol)
    # time.sleep(0.21)
    # winsound.Beep(800, 160)
    # winsound.Beep(800, 160)
    # winsound.Beep(800, 160)
    # time.sleep(0.21)
    # winsound.Beep(800, 310)
    # winsound.Beep(800, 310)
    # winsound.Beep(800, 310)
    # time.sleep(0.21)
    # winsound.Beep(800, 160)
    # winsound.Beep(800, 160)
    # winsound.Beep(800, 160)