#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox

def victory():
    victory_win = QMessageBox()
    victory_win.setText('Верно!')
    victory_win.exec()
    window.close()

def lose():
    lose_display = QMessageBox()
    lose_display.setText('Неверно!')
    lose_display.exec()
    window.close()
    

#создание приложения и главного окна
app = QApplication([])
window = QWidget()

window.setWindowTitle('krushclub music')
window.resize(500, 500)
#создание виджетов главного окна

question = QLabel('В каком году канал получил "золотую кнопку" от YouTube')

r_btn1 = QRadioButton('2005')
r_btn2 = QRadioButton('2015')
r_btn3 = QRadioButton('2010')
r_btn4 = QRadioButton('2020')

#расположение виджетов по лэйаутам

v_line = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()

h_line1.addWidget(question, alignment = Qt.AlignCenter)
h_line2.addWidget(r_btn1, alignment = Qt.AlignCenter)
h_line2.addWidget(r_btn3, alignment = Qt.AlignCenter)
h_line3.addWidget(r_btn2, alignment = Qt.AlignCenter)
h_line3.addWidget(r_btn4, alignment = Qt.AlignCenter)

v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)

window.setLayout(v_line)

#обработка нажатий на переключатели

r_btn2.clicked.connect(victory)
r_btn1.clicked.connect(lose)
r_btn3.clicked.connect(lose)
r_btn4.clicked.connect(lose)
 
#отображение окна приложения 


window.show()
app.exec()