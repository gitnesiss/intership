# basic_window.py
# Импортируем необходимые модули
import sys
from PyQt6.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
  def __init__(self):
    """Конструктор для класса "Пустое окно"""
    super().__init__()
    self.initializeUI()
  def initializeUI(self):
    """Настройка приложения."""
    self.setGeometry(300, 100, 400, 300)    # порядок цифр(
                                            # координата верхнего левого угла по X,
                                            # координата верхнего левого угла по Y,
                                            # ширина окна,
                                            # высота окна)
    self.setWindowTitle("Пустое окно в PyQt")
    self.show() # Отображение окна на экране

# Запустить программу
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = EmptyWindow()
  sys.exit(app.exec())
  