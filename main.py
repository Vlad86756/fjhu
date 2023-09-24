from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from random import randint

app = QApplication([])
win = QWidget()
win.setWindowTitle("Лотерея")
win.resize(400, 400)
win.move(100, 100)

text=QLabel(win)
text.setText("Натисни, щоб взяти участь")
text.move(70, 10)

text2 = QLabel(win)
text2.setText("?")
text2.move(190, 70)

text3 = QLabel(win)
text3.setText("?")
text3.move(190, 100)










button = QPushButton(win)
button.setText("Випробувати удачу")
button.move(140, 130)








def show_win():
    number = randint(1, 100)
    number1= randint(1, 100)
    text2.setText(str(number))

    text3.setText(str(number1))

    if number == number1:
        text.setText("Ви виграли! Зіграйте знову")
    elif number != number1:
        text.setText("Ви програли! Зіграйте знову")

button.clicked.connect(show_win)




win.show()
app.exec_()