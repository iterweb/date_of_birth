import sqlite3
import sys, os
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

user = os.getlogin()

current_date = datetime.now().date()


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = ''
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM person')
        rows = cur.fetchall()
        for row in rows:
            if row[1] == current_date.day and row[2] == current_date.month:
                age = current_date.year - row[3]
                self.setWindowTitle(self.title)
                self.setGeometry(self.left, self.top, self.width, self.height)

                msg = QMessageBox(self)
                msg.setWindowTitle("Тадаааамм")
                msg.setIcon(QMessageBox.Question)
                msg.setText(f'Сегодня {row[0]} празднует свой {age}-й день рождения')

                buttonAceptar = msg.addButton("Удалить", QMessageBox.YesRole)
                buttonCancelar = msg.addButton("Далее", QMessageBox.RejectRole)
                msg.setDefaultButton(buttonAceptar)
                msg.exec_()

                with open('C:\\Users\\%s\\Desktop\\birthday.txt' %user, 'a') as birthday:
                    birthday.write(f'Сегодня {row[0]} празднует свой {age}-й день рождения\n')

                if msg.clickedButton() == buttonAceptar:
                    cur.execute("DELETE FROM person WHERE full_name=?", (row[0],))
                    con.commit()
                elif msg.clickedButton() == buttonCancelar:
                    pass

        con.close()
        try:
            self.closeEvent(self, quit())
        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
