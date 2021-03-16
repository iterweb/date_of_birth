import sys

import sqlite3
import os
from datetime import datetime

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox, QLabel

from PyQt5.QtCore import pyqtSlot


current_date = datetime.now().date()

sum_current_date = current_date.month + current_date.day


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Добавить дату'
        self.left = 200
        self.top = 100
        self.width = 290
        self.height = 180
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create full_name
        self.full_name = QLineEdit(self)
        self.full_name.move(20, 30)
        self.full_name.resize(250, 30)
        self.label = QLabel('Имя', self)
        self.label.move(20, 5)

        # Create day_born
        self.day_born = QLineEdit(self)
        self.day_born.move(20, 90)
        self.day_born.resize(40, 30)
        self.label = QLabel('День', self)
        self.label.move(20, 60)

        # Create month_born
        self.month_born = QLineEdit(self)
        self.month_born.move(99, 90)
        self.month_born.resize(40, 30)
        self.label = QLabel('Месяц', self)
        self.label.move(100, 60)

        # Create year_born
        self.year_born = QLineEdit(self)
        self.year_born.move(190, 90)
        self.year_born.resize(80, 30)
        self.label = QLabel('Год', self)
        self.label.move(190, 60)

        # Create a button in the window
        self.button = QPushButton('Ок', self)
        self.button.move(20, 140)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        if int(self.day_born.text()) >= 32:
            QMessageBox.question(self, self.title, "Месяц, не может содержать больше, чем 31 день", QMessageBox.Ok,
                                 QMessageBox.Ok)
            self.day_born.setText("")
        elif int(self.month_born.text()) >= 13:
            QMessageBox.question(self, self.title, "В году только 12 месяцев", QMessageBox.Ok, QMessageBox.Ok)
            self.month_born.setText("")
        elif current_date.year < int(self.year_born.text()):
            QMessageBox.question(self, self.title, "Этот год еще не наступил", QMessageBox.Ok, QMessageBox.Ok)
            self.year_born.setText("")

        else:
            try:
                cur.execute("INSERT INTO person VALUES (?,?,?,?)", (self.full_name.text(), self.day_born.text(), self.month_born.text(), self.year_born.text()))
                con.commit()
                #con.close()

                QMessageBox.question(self, self.title, "Сохранено", QMessageBox.Ok, QMessageBox.Ok)
                self.full_name.setText("")
                self.day_born.setText("")
                self.month_born.setText("")
                self.year_born.setText("")
            except:
                QMessageBox.question(self, self.title, "Это имя уже занято", QMessageBox.Ok, QMessageBox.Ok)
                self.full_name.setText("")


if __name__ == '__main__':

    if not os.path.exists('data.db'):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE person (
                                            full_name varchar(250) unique,
                                            day_born integer,
                                            month_born integer,
                                            year_born integer)''')
    else:
        con = sqlite3.connect('data.db')
        cur = con.cursor()

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

