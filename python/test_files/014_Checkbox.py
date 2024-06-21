import sys

from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QApplication,
    QLabel,
    QCheckBox,
    QComboBox,
    # QListBox,
    QLineEdit,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QSlider,
    QVBoxLayout
)

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # widget = QCheckBox()
        # Checkbox без надписи
        noTextCkBox = QCheckBox()
        # Checkbox с надписью
        textCkBox = QCheckBox(text="Option")

        # Включение трёх состояний: 
        textCkBox.setCheckState(Qt.CheckState.PartiallyChecked)
        # Или:
        # textCkBox.setTriState(True)

        # Устанавливаем начальное состояние noTextCkBox с галочкой
        # Qt.CheckState.Unchecked - Элемент не отмечен
        # Qt.CheckState.PartiallyChecked - Элемент отмечен частично
        # Qt.CheckState.Checked - Элемент отмечен 
        noTextCkBox.setCheckState(Qt.CheckState.Checked)

        # Устанавливаем сигнал на изменение состояния у noTextCkBox
        noTextCkBox.stateChanged.connect(self.show_state)
        # Устанавливаем сигнал на изменение состояния у textCkBox
        textCkBox.stateChanged.connect(self.show_state)

        # Создаём слой с вертикальным расположением
        layout = QVBoxLayout()
        # Добавляем на этот слой чекбоксы
        layout.addWidget(noTextCkBox)
        layout.addWidget(textCkBox)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.CheckState.Checked)
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
