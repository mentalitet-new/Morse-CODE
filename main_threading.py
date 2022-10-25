import time
import winsound
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow


class Beep(QtCore.QThread):
    beep_connect = QtCore.pyqtSignal(str)

    def __init__(self, parent=QMainWindow, *args):
        super(Beep, self).__init__(parent)
        self.args = args

    def run(self):
        for i in self.args[0]:
            match i:
                case "*":
                    winsound.Beep(800, 160)
                case "-":
                    winsound.Beep(800, 310)
                case "d":
                    time.sleep(0.21)