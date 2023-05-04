import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QDesktopWidget
from PyQt5.QtCore import Qt, QTimer


class Paddle(QGraphicsRectItem):
    def __init__(self, x, y): 
        # Tworzenie prostokąta o wymiarach 10x80 pikseli w pozycji (x,y)
        super().__init__(x, y, 10, 80) 
        # Ustawienie flagi umożliwiającej przesuwanie obiektu
        self.setFlag(QGraphicsRectItem.ItemIsMovable, True) 

    def moveUp(self):
        # Sprawdzenie, czy górna krawędź prostokąta nie przekracza górnej krawędzi sceny
        if self.y() > -120: 
            # Przesunięcie wiosła o 20 pikseli w górę (jest -20 a nie +20 ponieważ środek sceny jest na środku ekranu i do góry wartości się zmniejszają)
            self.setY(self.y() - 20) 

    def moveDown(self):
        if self.y() < 125:
            self.setY(self.y() + 20)
        

class Ball(QGraphicsRectItem):
    def __init__(self, x, y, dx, dy):
        # Tworzenie piłki o wymiarach 10x10 pikseli w pozycji (x,y)
        super().__init__(x, y, 10, 10) 
        # Ustawienie prędkości piłki w osi x
        self.dx = dx 
        # Ustawienie prędkości piłki w osi y
        self.dy = dy 
    def move(self):
        # Przesunięcie piłki o wartość prędkości w osi x
        self.setX(self.x() + self.dx) 
        # Przesunięcie piłki o wartość prędkości w osi y
        self.setY(self.y() + self.dy) 

    def reverseX(self):
        # Odwrócenie kierunku ruchu piłki w osi x
        self.dx = -self.dx 

    def reverseY(self):
        # Odwrócenie kierunku ruchu piłki w osi y
        self.dy = -self.dy 


    def setPos(self,x,y):
        # Ustawienie wartości współrzędnej x piłki
        self.setX(x) 
        # Ustawienie wartości współrzędnej y piłki
        self.setY(y) 

class Pong(QGraphicsView):
    def __init__(self):
        super().__init__()
        # Ustawiamy rozmiar okna gry
        self.setFixedSize(405, 340)
        # Ustawiamy tytuł okna
        self.setWindowTitle("Pong")
        # Tworzymy scenę, na której będzie toczyła się gra
        self.scene = QGraphicsScene()
        # Dodajemy scenę do widoku
        self.setScene(self.scene)
        # Tworzymy paletki i piłkę
        self.paddle1 = Paddle(0, 110)
        self.paddle2 = Paddle(390, 110)
        self.ball = Ball(195, 155,5,5)
        # Dodajemy paletki i piłkę do sceny
        self.scene.addItem(self.paddle1)
        self.scene.addItem(self.paddle2)
        self.scene.addItem(self.ball)
        # Ustawiamy tło sceny
        self.setBackgroundBrush(Qt.black)
        # Ustawiamy ramki wokół elementów gry
        self.scene.setSceneRect(0, 0, 400, 320)
        # Ramka
        self.paddle1.setPen(Qt.white)
        # Wypełnienie
        self.paddle1.setBrush(Qt.white)
        self.paddle2.setPen(Qt.white)
        self.paddle2.setBrush(Qt.white)
        self.ball.setPen(Qt.white)
        self.ball.setBrush(Qt.white)
        # Tworzymy timer, który będzie służył do aktualizacji stanu gry
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(20)

     # Metoda służąca do aktualizacji stanu gry
    def update(self):
        # Sprawdzamy, czy piłka zderzyła się z paletką nr 1
        if self.ball.collidesWithItem(self.paddle1):
            self.ball.reverseX()
        # Sprawdzamy, czy piłka zderzyła się z paletką nr 2
        elif self.ball.collidesWithItem(self.paddle2):
            self.ball.reverseX()
        # Sprawdzamy, czy piłka zderzyła się z górną lub dolną ścianą
        elif self.ball.y() < -155 or self.ball.y() > 155:
            self.ball.reverseY()
        # Sprawdzamy, czy piłka minęła paletkę nr 1
        elif self.ball.x() < -195:
            self.ball.setPos(0, 0)
        # Sprawdzamy, czy piłka minęła paletkę nr 2
        elif self.ball.x() > 195:
            self.ball.setPos(0, 0)
        # Przesuwamy piłkę
        self.ball.move()
        # Odświeżamy widok
        self.viewport().update()

    # Metoda służąca do obsługi naciśnięcia klawisza
    def keyPressEvent(self, event):
        # Sprawdzamy, który klawisz został naciśnięty
        if event.key() == Qt.Key_W:
            # Przesuwamy paletkę nr 1 w górę
            self.paddle1.moveUp()
        elif event.key() == Qt.Key_S:
            # Przesuwamy paletkę nr 1 w dół
            self.paddle1.moveDown()
        elif event.key() == Qt.Key_Up:
            # Przesuwamy paletkę nr 2 w górę
            self.paddle2.moveUp()
        elif event.key() == Qt.Key_Down:
            # Przesuwamy paletkę nr 2 w dół
            self.paddle2.moveDown()

if __name__ == '__main__':
    app = QApplication([])
    pong = Pong()
    # Ustawiamy okno gry na środku ekranu
    screen_geometry = app.desktop().screenGeometry()
    x = (screen_geometry.width() - pong.width()) / 2
    y = (screen_geometry.height() - pong.height()) / 2
    pong.setGeometry(int(x), int(y), pong.width(), pong.height())
    # Wyświetlamy okno gry
    pong.show()
    app.exec_()