import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QLineEdit, QPushButton

class ToDoList(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-Do List")

        # Creating a container for displaying actions
        self.list_widget = QListWidget(self)
        self.list_widget.setGeometry(10, 10, 480, 300)
        self.list_widget.setStyleSheet("background-color: #cccccc; color: #333333; font: 12pt Arial")

        # Loading actions from a file
        try:
            with open("todos.txt", "r") as f:
                for line in f:
                    item = line.strip()
                    if item != "":
                        list_item = QListWidgetItem(item)
                        self.list_widget.addItem(list_item)
        except:
            pass

        # Creating a button and a text field for writing actions
        self.entry = QLineEdit(self)
        self.entry.setGeometry(10, 320, 480, 30)
        self.entry.setStyleSheet("background-color: #ffffff; color: #333333; font: 12pt Arial")
        self.entry.returnPressed.connect(self.add_item)
        self.button_add = QPushButton("Dodaj czynność", self)
        self.button_add.setGeometry(270, 360, 220, 30)
        self.button_add.setStyleSheet("background-color: #90ee90; color: #333333; font: 12pt Arial; font-weight: bold")
        self.button_add.clicked.connect(self.add_item)

        # Creating a button for removing actions
        self.button_remove = QPushButton("Usuń czynność", self)
        self.button_remove.setGeometry(10, 360, 250, 30)
        self.button_remove.setStyleSheet("background-color: #ffcccb; color: #333333; font: 12pt Arial; font-weight: bold")
        self.button_remove.clicked.connect(self.remove_item)

        # Positioning window
        self.setGeometry(100, 100, 500, 400)
        self.setStyleSheet("background-color: #333333")

        self.show()

    # Adding new action to container
    def add_item(self):
        item = self.entry.text().strip()
        if item != "":
            list_item = QListWidgetItem(item)
            self.list_widget.addItem(list_item)
            self.entry.clear()
            self.save_items()

    # Removing action from a container
    def remove_item(self):
        item = self.list_widget.currentItem()
        if item:
            self.list_widget.takeItem(self.list_widget.row(item))
            self.save_items()

    # Saving actions to a file
    def save_items(self):
        with open("todos.txt", "w") as f:
            for i in range(self.list_widget.count()):
                item = self.list_widget.item(i).text()
                f.write(item + "\n")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_list = ToDoList()
    sys.exit(app.exec_())
