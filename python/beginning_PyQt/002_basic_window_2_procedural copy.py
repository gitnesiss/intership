# procedural.py
# 1. Импортируйте необходимые модули
import sys # использовать sys для приема аргументов командной строки
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv) # 2. Создайте объект QApplication
window = QWidget() # 3. Создать окно из объекта QWidget
window.setWindowTitle("Пустое окно в PyQt - парадигма процедурная")
window.show() # 4. Вызываем show для отображения окна графического интерфейса пользователя
sys.exit(app.exec()) # 5. Запустите цикл с обытий. Используйте sys.exit для закрытия программы