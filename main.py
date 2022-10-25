import json
import sys
from PyQt5.QtWidgets import QApplication, QStyleFactory, QMainWindow

from main_frame import Ui_MainWindow
from main_threading import Beep


class MorseCode(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MorseCode, self).__init__()
        self.play_beep_dot = None
        self.play_beep_dash = None
        self.play_beep = None
        self.total_symbol = None
        self.all_symbol_encode = None
        self.setupUi(self)
        self.pushButton_dot.clicked.connect(self.symbol_dot)
        self.pushButton_dash.clicked.connect(self.symbol_dash)
        self.pushButton_play.clicked.connect(self.play)

    def beep_class(self, value):
        self.play_beep = Beep(self, value)
        self.play_beep.start()

    def play(self):
        list_symbol_ent = self.encode_algorithm(self.lineEdit_read_symbol.text())
        self.beep_class("".join(list_symbol_ent))

    def symbol_dot(self):
        self.beep_class("*")
        
    def symbol_dash(self):
        self.beep_class("-")

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
        self.statusBar.showMessage(f'Result : {"|".join(self.all_symbol_encode)}')
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


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    dlgMain = MorseCode()  # create main window
    dlgMain.show()  # show window
    sys.exit(app.exec_())
