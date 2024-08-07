import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = Color('red')
        self.setCentralWidget(widget)
        

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()

        # фон виджета автоматически заполнялся цветом окна
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()