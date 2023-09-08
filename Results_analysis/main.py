import sys
from openpyxl import load_workbook
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget


class Results_win(QWidget):
    def __init__(self):
        super(Results_win,self).__init__()
        uic.loadUi('Results.ui',self)


def show_Results_win():
    app = QtWidgets.QApplication(sys.argv)
    results_win = Results_win()
    results_win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    show_Results_win()