import serial

port = "COM5"  # Замените на соответствующее имя COM-порта
baudrate = 57600  # Замените на желаемую скорость передачи данных

ser = serial.Serial(port, baudrate=baudrate)

# Выполнение операций на COM-порту

# Чтение данных
data = ser.read(1000)  # Прочитать 10 байт из COM-порта
print(data)

# Запись данных
message = b"Hello, world!"  # Данные для отправки должны быть в байтах.
ser.write(message)

ser.close()  # Не забудьте закрыть соединение, когда закончите.