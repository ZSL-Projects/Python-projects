from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
import random

pytania = {
  0 : "Czy Psy są lepsze od kotów",
  1 : "Czy 2 + 2 = 5?",
  2 : "Czy Bangladesz ma więcej obywateli niż Francja?",
  3 : "Czy kwadrat jest prostokątem?",
  4 : "Czy wieloryb to ryba?",
  5 : "Czy cyfra 5 jest liczbą pierwszą?",
  6 : "Czy miasto Detroit leży w stanie Michigan?",
  7 : "Czy Chiny mają większą powierzchnię od Stanów Zjednoczonych?",
  8 : "Czy wszystkie kąty w kwadracie są proste?",
  9 : "Czy brzechwa to część łuku?",
  10 : "Czy Aladyn był dżinem?",
  11: "Czy Wołga to najdłuższa rzeka w Europie?",
  12 : "Czy Henryk Sienkiewicz otrzymał nagrodę Nobla?",
  13 : "Czy lazurowe wybrzeże to riwiera włoska?",
  14 : "Czy 'tak' może być stosowany jako zaimek?",
  15 : "Czy delfiny oddychają powietrzem atmosferycznym?",
  16 : "Czy pęd jest wielkością wektorową?",
  17 : "Czy zoologia to nauka o leczeniu zwierząt?",
  18 : "Czy Messi jest najlepszym piłkarzem w historii?",
  19 : "Czy Quebec to stolica Kanady?"
}

odpowiedzi = {
  0 : "Tak",
  1 : "Nie",
  2 : "Tak",
  3 : "Tak",
  4 : "Nie",
  5 : "Tak",
  6 : "Tak",
  7 : "Tak",
  8 : "Tak",
  9 : "Nie",
  10 : "Nie",
  11 : "Tak",
  12 : "Tak",
  13 : "Nie",
  14 : "Tak",
  15 : "Tak",
  16 : "Tak",
  17 : "Nie",
  18 : "Tak",
  19 : "Nie"
}
tablica = []
def losowanie():
    while len(tablica) < 10:
        number = random.randint(0, 19)
        if number not in tablica:
            tablica.append(number)
def main():
    app = QApplication([])

    window = QWidget()
    window.setGeometry(100, 100, 200, 200)
    window.setWindowTitle("QUIZ")
    layout = QVBoxLayout()

    question = pytania[tablica[i]]
    label = QLabel(question)
    button = QPushButton("Tak")
    button2 = QPushButton("Nie")

    def on_clicked():
        answer = odpowiedzi[tablica[i]]
        if button.text() == answer:
            global o
            o += 1
        window.close()
    def on_clicked2():
        answer = odpowiedzi[tablica[i]]
        if button2.text() == answer:
            global o
            o += 1
        window.close()

    button.clicked.connect(on_clicked)
    button2.clicked.connect(on_clicked2)

    button.setStyleSheet("background-color: green; color: white; font-weight: bold")
    button2.setStyleSheet("background-color: green; color: white; font-weight: bold")
    button.setFont(QFont("Arial", 12))
    button2.setFont(QFont("Arial", 12))
    label.setAlignment(QtCore.Qt.AlignCenter)



    layout.addWidget(label)
    layout.addWidget(button)
    layout.addWidget(button2)
    window.setLayout(layout)

    window.show()

    app.exec()
def main2(o):
    app = QApplication([])
    window2 = QWidget()
    window2.setGeometry(100, 100, 200, 200)
    window2.setWindowTitle("ODPOWIEDZI")
    layout2 = QVBoxLayout()

    if o == 1:
        text = 'Odpowiedziałeś poprawnie na 1 pytanie'
    elif 5 > o:
        text = 'Odpowiedziałeś poprawnie na ', o, ' pytania'
    else:
        text = 'Odpowiedziałeś poprawnie na ', o, ' pytań'
    text = str(text)
    text = text.replace("'", '')
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace(',', '')
    label2 = QLabel(text)
    label2.setAlignment(QtCore.Qt.AlignCenter)
    label2.setStyleSheet("font-weight: bold")
    layout2.addWidget(label2)
    window2.setLayout(layout2)
    window2.show()
    app.exec()

if __name__ == '__main__':
    i = 0
    global o
    o = 0
    losowanie()
    while i < 10:
        main()
        i += 1
    main2(o)
