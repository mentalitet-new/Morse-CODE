import json
import sys
import time
import winsound
from PyQt5.QtWidgets import QApplication, QStyleFactory, QMainWindow

from main_frame import Ui_MainWindow


class MorseCode(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MorseCode, self).__init__()
        self.total_symbol = None
        self.all_symbol_encode = None
        self.setupUi(self)
        self.pushButton_dot.clicked.connect(self.symbol_dot)
        self.pushButton_dash.clicked.connect(self.symbol_dash)
        self.pushButton_play.clicked.connect(self.play)

    def play(self):
        list_symbol_ent = self.encode_algorithm(self.lineEdit_read_symbol.text())
        self.play_beep("d".join(list_symbol_ent))

    def symbol_dot(self):
        self.play_beep("*")

    def symbol_dash(self):
        self.play_beep("-")

    def __open_json_key(self):
        with open("key.json", "r") as read:
            data = json.load(read)
        return data

    def encode_algorithm(self, symbol_encode):
        self.all_symbol_encode = []
        self.total_symbol = []
        data = self.__open_json_key()
        if symbol_encode is not None:
            self.total_symbol.append(symbol_encode)
        else:
            pass

        for i in self.total_symbol[0].upper():
            k = i
            if k in data["alphabet"]:
                self.all_symbol_encode.append(data["alphabet"][k])
            elif k in data["numbers"]:
                self.all_symbol_encode.append(data["numbers"][k])
        self.statusBar.showMessage(f'Result : {"".join(self.all_symbol_encode)}')
        return self.all_symbol_encode

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
            match i:
                case "*":
                    winsound.Beep(800, 160)
                case "-":
                    winsound.Beep(800, 310)
                case "d":
                    time.sleep(0.21)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    dlgMain = MorseCode()  # create main window
    dlgMain.show()  # show window
    sys.exit(app.exec_())
