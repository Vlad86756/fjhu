from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QRadioButton
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Конкурс від Crazy People")
main_win.resize(400, 200)

question = QLabel(main_win)
question.setText("В якому році канал отримав золоту кнопку від YouTube?")
question.move(10, 10)

btn_1 = QRadioButton(main_win)
btn_1.setText("2005")
btn_1.move(100, 60)

btn_2 = QRadioButton(main_win)
btn_2.setText("2010")
btn_2.move(200, 60)

btn_3 = QRadioButton(main_win)
btn_3.setText("2015")
btn_3.move(100, 120)

btn_4 = QRadioButton(main_win)
btn_4.setText("2020")
btn_4.move(200, 120)

def show_win():
    win = QMessageBox()
    win.setText("Правильно! Ви виграли гіроскутер")
    win.exec_()
def show_lose():
    lose = QMessageBox()
    lose.setText("Ні, в 2015 році. Ви виграли фірмовий плакат")
    lose.exec_()
btn_3.clicked.connect(show_win)
btn_1.clicked.connect(show_lose)
btn_2.clicked.connect(show_lose)
btn_4.clicked.connect(show_lose)
main_win.show()
app.exec_()