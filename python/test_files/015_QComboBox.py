import sys

from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QApplication,
    QComboBox,
    QVBoxLayout
)

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # Создание экземпляра класса QComboBox()
        # Отсчёт в комбобоксе с 0
        wcombo1 = QComboBox()
        wcombo1.addItems(["Zero", "One", "Two", "Three", "Four", "Five"])
        
        wcombo2 = QComboBox()
        wcombo2.addItems(["Белый"])
        wcombo2.addItems(["Синий"])
        wcombo2.addItems(["Красный"])

        self.wcombo3 = QComboBox()
        self.wcombo3.addItems(["Zero", "One", "Two", "Three", "Four", "Five"])

        self.wcombo4 = QComboBox()
        self.wcombo4.setEditable(True)
        self.wcombo4.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

        # Отправляет текущий индекс (позицию) выбранного элемента.
        wcombo1.currentIndexChanged.connect(self.index_changed)

        # Есть альтернативный сигнал отправки текста.
        wcombo1.editTextChanged.connect(self.text_changed)

        # Отправляет сигнал, вместо номера индекса, ниименование метки (текст с метки).
        wcombo2.currentTextChanged.connect(self.text_changed)

        # Соединяем сигнал с методами
        self.wcombo3.activated.connect(self.check_index)
        self.wcombo3.activated.connect(self.current_text)
        self.wcombo3.activated.connect(self.current_text_via_index)
        self.wcombo3.activated.connect(self.current_count)

        # Создаём слой с вертикальным расположением
        layout = QVBoxLayout()
        # Добавляем на этот слой виджеты
        layout.addWidget(wcombo1)
        layout.addWidget(wcombo2)
        layout.addWidget(self.wcombo3)
        layout.addWidget(self.wcombo4)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


    def index_changed(self, i): # i — это int
        print(i)

    def text_changed(self, s): # s — это str
        print(s)



    def check_index(self, index):
        cindex = self.wcombo3.currentIndex()
        print(f"Index signal: {index}, currentIndex {cindex}")

    def current_text(self, _): # We receive the index, but don't use it.
        ctext = self.wcombo3.currentText()
        print("Current text", ctext)

    def current_text_via_index(self, index):
        ctext = self.wcombo3.itemText(index)  # Get the text at index.
        print("Current itemText", ctext)

    def current_count(self, index):
        count = self.wcombo3.count()
        print(f"Index {index+1}/{count}")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
