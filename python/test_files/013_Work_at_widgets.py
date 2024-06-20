import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel, QCheckBox, QComboBox, #QListBox, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # widget = QLabel("Hello")

        widget = QLabel("1")  # Создана метка с текстом 1.
        widget.setText("2")   # Создана метка с текстом 2.

        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()