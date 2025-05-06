import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit,
    QGridLayout, QInputDialog
)

class InputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog demo")
        self.resize(400, 200)

        # Layout Grid
        layout = QGridLayout()

        # Tombol dan kolom untuk memilih dari list
        self.btn_list = QPushButton("Choose from list")
        self.btn_list.clicked.connect(self.choose_from_list)
        self.line_list = QLineEdit()
        layout.addWidget(self.btn_list, 0, 0)
        layout.addWidget(self.line_list, 0, 1)

        # Tombol dan kolom untuk input nama
        self.btn_name = QPushButton("get name")
        self.btn_name.clicked.connect(self.get_name)
        self.line_name = QLineEdit()
        layout.addWidget(self.btn_name, 1, 0)
        layout.addWidget(self.line_name, 1, 1)

        # Tombol dan kolom untuk input angka
        self.btn_integer = QPushButton("Enter an integer")
        self.btn_integer.clicked.connect(self.get_integer)
        self.line_integer = QLineEdit()
        layout.addWidget(self.btn_integer, 2, 0)
        layout.addWidget(self.line_integer, 2, 1)

        self.setLayout(layout)

    def choose_from_list(self):
        items = ["C", "C++", "Java", "Python"]
        item, ok = QInputDialog.getItem(self, "Select Language", "List of languages:", items, 0, False)
        if ok:
            self.line_list.setText(item)

    def get_name(self):
        name, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your name:")
        if ok:
            self.line_name.setText(name)

    def get_integer(self):
        num, ok = QInputDialog.getInt(self, "Integer Input Dialog", "Enter a number:")
        if ok:
            self.line_integer.setText(str(num))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InputDialogDemo()
    window.show()
    sys.exit(app.exec_())
