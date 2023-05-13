import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
import main
 
win = False
count = 0
 
 
class CheckerBoard(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Checkers")
        self.setGeometry(100, 100, 800, 800)
 
        self.board = [[0, 1, 0, 1, 0, 1, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [2, 0, 2, 0, 2, 0, 2, 0],
                      [0, 2, 0, 2, 0, 2, 0, 2],
                      [2, 0, 2, 0, 2, 0, 2, 0]]
 
        self.selected = None
 
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawBoard(qp)
        qp.end()
 
    def drawBoard(self, qp):
        size = min(self.width(), self.height())
        unit = size // 8
 
        for i in range(8):
            for j in range(8):
                x = i * unit
                y = j * unit
                if (i + j) % 2 == 0:
                    qp.fillRect(x, y, unit, unit, QColor(255, 255, 255))
                else:
                    qp.fillRect(x, y, unit, unit, QColor(0, 0, 0))
 
                if self.board[i][j] == 1:
                    qp.setBrush(QColor(255, 0, 0))
                    qp.drawEllipse(x + unit // 10, y + unit // 10, unit * 4 // 5, unit * 4 // 5)
                elif self.board[i][j] == 2:
                    qp.setBrush(QColor(0, 0, 255))
                    qp.drawEllipse(x + unit // 10, y + unit // 10, unit * 4 // 5, unit * 4 // 5)
                if self.board[i][j] == 3:
                    qp.setBrush(QColor(255, 20, 147))
                    qp.drawEllipse(x + unit // 10, y + unit // 10, unit * 4 // 5, unit * 4 // 5)
                elif self.board[i][j] == 4:
                    qp.setBrush(QColor(135, 206, 250))
                    qp.drawEllipse(x + unit // 10, y + unit // 10, unit * 4 // 5, unit * 4 // 5)
 
        if self.selected is not None:
            qp.setBrush(QColor(0, 255, 0))
            qp.drawEllipse(self.selected[0] * unit + unit // 10, self.selected[1] * unit + unit // 10, unit * 4 // 5,
                           unit * 4 // 5)
 
    def mousePressEvent(self, event):
        x = event.x() // (self.width() // 8)
        y = event.y() // (self.height() // 8)
 
        if self.selected is not None:
            if (x, y) == self.selected:
                self.selected = None
            else:
                self.movePiece(self.selected[0], self.selected[1], x, y)
                self.selected = None
        else:
            if self.board[x][y] != 0:
                self.selected = (x, y)
 
        self.update()
 
    def king(self, x, y):
        if self.board[x][y] == 2 and x == 0:
            self.board[x][y] = 4
        elif self.board[x][y] == 1 and x == 7:
            self.board[x][y] = 3
 
    def isWon(self, color):
        global col1
        if color == 1:
            col1 = 3
        if color ==2:
            col1 = 4
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == color or self.board[i][j] == col1:
                    return False
        return True
 
    def movePiece(self, x1, y1, x2, y2):
        if main.count % 2 == 0:
            move = 1
            move1 = 3
        else:
            move = 2
            move1 = 4
 
        if move != self.board[x1][y1] and move1 != self.board[x1][y1]:
            msg = QMessageBox()
            msg.setWindowTitle("Wrong move")
            msg.setText("It's not your turn!")
            x = msg.exec_()
            return
 
        if self.board[x1][y1] == 0:
            return
 
        if self.board[x2][y2] != 0:
            return
 
        dx = x2 - x1
        dy = y2 - y1
 
        def can_capture(board, color):
            captures = []
            for i in range(8):
                for j in range(8):
                    if board[i][j] == color:
                        if i > 1 and j > 1 and board[i - 1][j - 1] != color and board[i - 1][j - 1] != 0 and \
                                board[i - 2][j - 2] == 0:
                            captures.append((i, j, i - 2, j - 2))
                        elif i > 1 and j < 6 and board[i - 1][j + 1] != color and board[i - 1][j + 1] != 0 and \
                                board[i - 2][j + 2] == 0:
                            captures.append((i, j, i - 2, j + 2))
                        elif i < 6 and j > 1 and board[i + 1][j - 1] != color and board[i + 1][j - 1] != 0 and \
                                board[i + 2][j - 2] == 0:
                            captures.append((i, j, i + 2, j - 2))
                        elif i < 6 and j < 6 and board[i + 1][j + 1] != color and board[i + 1][j + 1] != 0 and \
                                board[i + 2][j + 2] == 0:
                            captures.append((i, j, i + 2, j + 2))
            return captures
 
 
        def can_any_capture(board, color):
            captures = can_capture(board, color)
            return len(captures) > 0
 
        if self.board[x1][y1] == 1 and dx == 2 and abs(dy) == 2:
            if self.board[(x1 + x2) // 2][(y1 + y2) // 2] == 2 or self.board[(x1 + x2) // 2][(y1 + y2) // 2] == 4:
                self.board[x2][y2] = self.board[x1][y1]
                self.board[x1][y1] = 0
                self.board[(x1 + x2) // 2][(y1 + y2) // 2] = 0
                if can_any_capture(self.board, move):
                    main.count -= 1
            else:
                return
 
        elif self.board[x1][y1] == 2 and dx == -2 and abs(dy) == 2:
            if self.board[(x1 + x2) // 2][(y1 + y2) // 2] == 1 or self.board[(x1 + x2) // 2][(y1 + y2) // 2] == 3:
                self.board[x2][y2] = self.board[x1][y1]
                self.board[x1][y1] = 0
                self.board[(x1 + x2) // 2][(y1 + y2) // 2] = 0
                if can_any_capture(self.board, move):
                    main.count -= 1
            else:
                return
 
        elif self.board[x1][y1] == 3 and abs(dx) == 2 and abs(dy) == 2:
            if self.board[(x1 + x2) // 2][(y1 + y2) // 2] == 2 or self.board[(x1 + x2) // 2][(y1 + y2) // 2] == 4:
                self.board[x2][y2] = self.board[x1][y1]
                self.board[x1][y1] = 0
                self.board[(x1 + x2) // 2][(y1 + y2) // 2] = 0
                if can_any_capture(self.board, move):
                    main.count -= 1
            else:
                return
 
        elif self.board[x1][y1] == 4 and abs(dx) == 2 and abs(dy) == 2:
            # Check if there is an opponent piece between the current and target positions
            if self.board[(x1 + x2) // 2][(y1 + y2) // 2] == 1 or self.board[(x1 + x2) // 2][(y1 + y2) // 2] == 3:
                self.board[x2][y2] = self.board[x1][y1]
                self.board[x1][y1] = 0
                self.board[(x1 + x2) // 2][(y1 + y2) // 2] = 0
                if can_any_capture(self.board, move):
                    main.count -= 1
            else:
                return
        # Check if the selected piece can move without capturing
        elif self.board[x1][y1] == 1 and dx == 1 and abs(dy) == 1:
            self.board[x2][y2] = self.board[x1][y1]
            self.board[x1][y1] = 0
        elif self.board[x1][y1] == 2 and dx == -1 and abs(dy) == 1:
            self.board[x2][y2] = self.board[x1][y1]
            self.board[x1][y1] = 0
        elif self.board[x1][y1] == 3 and abs(dx) == 1 and abs(dy) == 1:
            self.board[x2][y2] = self.board[x1][y1]
            self.board[x1][y1] = 0
        elif self.board[x1][y1] == 4 and abs(dx) == 1 and abs(dy) == 1:
            self.board[x2][y2] = self.board[x1][y1]
            self.board[x1][y1] = 0
        else:
            return
 
        self.king(x2, y2)
 
        main.count += 1
 
        if self.isWon(1):
            msg = QMessageBox()
            msg.setWindowTitle("Red won!")
            msg.setText("Congratulations! Red won!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.finished.connect(app.quit)
            x = msg.exec_()
 
        if self.isWon(2):
            msg = QMessageBox()
            msg.setWindowTitle("Blue won!")
            msg.setText("Congratulations! Blue won!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.finished.connect(app.quit)
            x = msg.exec_()
 
        self.selected = None
 
    def run(self):
        self.show()
 
 
def run(self):
    self.show()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkerBoard = CheckerBoard()
    checkerBoard.run()
    sys.exit(app.exec_())
 