from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QRadioButton
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Конкурс від Crazy People")
main_win.resize(400, 200)

question = QLabel(main_win)
question.setText("Як звали першого ютуб-блогера, який набрав 100000000 підписників?")
question.move(10, 10)

btn_1 = QRadioButton(main_win)
btn_1.setText("PewDiePie ")
btn_1.move(100, 60)

btn_2 = QRadioButton(main_win)
btn_2.setText("Рет і Лінк")
btn_2.move(200, 60)

btn_3 = QRadioButton(main_win)
btn_3.setText("SlivkiShow")
btn_3.move(300, 60)

btn_4 = QRadioButton(main_win)
btn_4.setText("TheBrianMaps")
btn_4.move(100, 120)

btn_5 = QRadioButton(main_win)
btn_5.setText("Mister Max")
btn_5.move(200, 120)

btn_6 = QRadioButton(main_win)
btn_6.setText("EeOneGuy")
btn_6.move(300, 120)


def show_win():
    win = QMessageBox()
    win.setText("Ви виграли зустріч з творцями каналу!")
    win.exec_()
def show_lose():
    win = QMessageBox()
    win.setText("Пощастить іншим разом!")
    win.exec_()
btn_1.clicked.connect(show_win)
btn_3.clicked.connect(show_lose)
btn_2.clicked.connect(show_lose)
btn_4.clicked.connect(show_lose)
btn_5.clicked.connect(show_lose)
btn_6.clicked.connect(show_lose)
main_win.show()
app.exec_()