import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QApplication,
    QLabel, QCheckBox, QComboBox, #QListBox, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider,
    QVBoxLayout
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.setGeometry(100, 100, 500, 300)

        # Ещё один вариант создания метки с надписью
        # widget = QLabel("Hello")

        # Создана метка с текстом 1.
        wqlable1 = QLabel("1")
        wqlable2 = QLabel()
        # Создана метка с текстом 2, которая перезапишет цифру 1.
        wqlable2.setText("2") 


        font1 = wqlable1.font()
        font2 = wqlable2.font()
        # Установить размер текста
        font1.setPointSize(30)
        font2.setPointSize(20)
        # Установить шрифт в виджет
        wqlable1.setFont(font1)
        wqlable2.setFont(font2)
        # Установить выравнивание шрифта в виджете
        # Qt.AlignmentFlag.AlignLeft - выравнивание по левому краю
        # Qt.AlignmentFlag.AlignRight - выравнивание по правому краю
        # Qt.AlignmentFlag.AlignTop - выравнивание по верху
        # Qt.AlignmentFlag.AlignBottom - выравнивание по низу
        # Qt.AlignmentFlag.AlignCenter - центрировать горизонтально и вертикально
        wqlable1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        wqlable2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.wqlable3 = QLabel()
        self.wqlable3.setPixmap(QPixmap('./test_picture/cat.jpg'))
        self.wqlable3.setScaledContents(True)

        # Создаём слой с вертикальным расположением
        layout = QVBoxLayout()
        # Добавляем на этот слой чекбоксы
        layout.addWidget(wqlable1)
        layout.addWidget(wqlable2)
        layout.addWidget(self.wqlable3)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
