import serial
import time

# Настройка порта (замените на ваш порт)
ser = serial.Serial('COM2', baudrate=115200, timeout=1)

# def send_sbgc_command(cmd, data):
#     # Формирование пакета
#     length = len(data) + 2  # +2 (CMD + CRC)
#     # packet = bytearray([0x3E, length, cmd] + data)
#     packet = bytearray([0x3E, 0x06, 0x01, 0x64, 0xC8, 0x00, 0x00])
#     print(packet)
    
#     # Расчет CRC
#     crc = 0
#     for b in packet[1:]:  # Все байты кроме HEADER
#         crc ^= b
#     packet.append(crc)

#     print(packet)
    
#     # Отправка
#     ser.write(packet)
#     time.sleep(0.1)  # Пауза для обработки

#     print(f"CRC: {hex(crc)}")

# # Пример: установить углы pitch=100, yaw=200 (CMD 0x01)
# send_sbgc_command(0x01, [100, 200, 0, 0])  # DATA: [pitch, yaw, roll, flags]



# Установить pitch=30°, yaw=45°, roll=0°
pitch = 30   # 0x1E
yaw = 45     # 0x2D
roll = 0     # 0x00
flags = 0    # 0x00 (флаги по умолчанию)

# Формируем пакет:
packet = bytearray([
    0x3E,             # HEADER
    0x06,             # LENGTH (4 данных + 2 байта CMD+CRC)
    0x01,             # CMD (управление моторами)
    pitch & 0xFF,     # DATA: pitch (младший байт)
    yaw & 0xFF,       # DATA: yaw
    roll & 0xFF,      # DATA: roll
    flags             # DATA: флаги
])

# Расчет CRC (XOR всех байтов кроме HEADER)
crc = 0x06 ^ 0x01 ^ pitch ^ yaw ^ roll ^ flags
packet.append(crc)

# Отправка
ser.write(packet)



ser.close()