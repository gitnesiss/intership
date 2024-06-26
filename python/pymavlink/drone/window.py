import sys
import serial
import serial.tools.list_ports

from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QApplication,
    QComboBox,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton
)

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Подключение к Serial port")

        self.combobox_comport = QComboBox()
        ports = list(serial.tools.list_ports.comports())
        self.combobox_comport.addItem("")
        self.combobox_comport.addItems([name.device for name in ports])

        self.combobox_comport.currentTextChanged.connect(self.find_com_ports)

        # Создаём кнопку с надписью
        buttonRefresh = QPushButton("Обновить список COM портов")
        buttonConnect = QPushButton("Подключиться к COM порту")


        ### !!!
        ### !!!
        ### !!! Работа со слоями https://habr.com/ru/companies/skillfactory/articles/648845/
        ### !!!
        ### !!!


        # Создаём слой с вертикальным расположением
        layoutV = QVBoxLayout()
        layoutH = QHBoxLayout()
        layoutH.addWidget(buttonRefresh)
        layoutH.addWidget(self.combobox_comport)
        layoutV.addWidget(layoutH(self))
        layoutV.addWidget(buttonConnect)

        widget = QWidget()
        widget.setLayout(layoutV)

        self.setCentralWidget(widget)

    def find_com_ports(self, s):
        print(s)

        try:
            # Найти и открыть COM-порт
            ports = serial.tools.list_ports.comports()
            port = next((p.device for p in ports), None)

            if port is None:
                raise ValueError("No COM port found.")

            ser = serial.Serial(port, baudrate=57600)

            # Выполнение операций на COM-порту

            ser.close()  # Закрыть соединение когда завершается программа

        except ValueError as ve:
            print("Error:", str(ve))

        except serial.SerialException as se:
            print("Serial port error:", str(se))

        except Exception as e:
            print("An error occurred:", str(e))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
