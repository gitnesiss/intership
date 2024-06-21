import sys # Только для доступа к аргументам командной строки
from PyQt6.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Пустое окно в PyQt")
        self.show() # Отображение окна на экране


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Создаём виджет Qt — окно.
    window = EmptyWindow()
    # window.show()  # Важно: окно по умолчанию скрыто.

    # Запускаем цикл событий.
    sys.exit(app.exec())
