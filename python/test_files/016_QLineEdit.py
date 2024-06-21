import sys

from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QApplication,
    QLineEdit,
    QLineEdit,
    QVBoxLayout
)

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        self.setGeometry(100, 100, 500, 300)

        wQLineEdit = QLineEdit()
        wQLineEdit.setMaxLength(10)
        wQLineEdit.setPlaceholderText("Enter your text")

        wQLineEdit2 = QLineEdit()
        wQLineEdit2.setPlaceholderText("Enter your IP")
        wQLineEdit2.setInputMask('000.000.000.000;_')

        # раскомментируйте, чтобы сделать доступным только для чтения
        # wQLineEdit.setReadOnly(True)

        wQLineEdit.returnPressed.connect(self.return_pressed)
        wQLineEdit.selectionChanged.connect(self.selection_changed)
        wQLineEdit.textChanged.connect(self.text_changed)
        wQLineEdit.textEdited.connect(self.text_edited)

        # Создаём слой с вертикальным расположением
        layout = QVBoxLayout()
        # Добавляем на этот слой виджеты
        layout.addWidget(wQLineEdit)
        layout.addWidget(wQLineEdit2)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


    def return_pressed(self):
        print("Нажат возврат!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Выбор изменён")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Текст изменён...")
        print(s)

    def text_edited(self, s):
        print("Текст отредактирован...")
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
