import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Задаём название окна
        self.setWindowTitle("My App - Соединение виджетов друг с другом.")

        # Задаём минимальный и максимальный размер окна (ширина, высота)
        self.setMinimumSize(QSize(400, 200))

        # Создаём экземпляр класса метки
        self.label = QLabel()

        # Создаём экземпляр класса Линии с надписью
        self.input = QLineEdit()
        # Создаём сигнал от экземпляра QLineEdit() к слоту экземпляра QLineEdit()
        # При изменении текста в input будет меняться текст в label
        self.input.textChanged.connect(self.label.setText)

        # Создаём макет расположения виджетов Вертикальную коробку
        layout = QVBoxLayout()
        # Добавляем на макет виджеты
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        # Создаём контейнер в который устанавливаем макет.
        container = QWidget()
        # Помещаем в контейнер макет.
        container.setLayout(layout)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
