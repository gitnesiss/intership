# 2024-12-21
# Считываем с COM-порта к которому подключен ардуино со скетчем, 
# который можно посмотреть в конце этой программы
# 

import serial
import serial.tools.list_ports

try:
    # Находим доступный COM-порт
    # ports - список всех доступных COM-портов
    ports = serial.tools.list_ports.comports()
    print("Доступные COM-порты:")
    # Выводим список доступных COM-портов
    for port in ports:
        print(port.device)
    
    # С помощью генератора (p.device for p in ports) и функции next()
    # пытаемся получить устройство первого найденного COM-порта. Если порты 
    # отсутствуют, то функция next() вернет значение по умолчанию — None.
    port = next((p.device for p in ports), None)
    # Если в переменной port пусто (is None), то с помощью команды
    # raise вручную инициируем исключение
    if port is None:
        raise ValueError("COM-порты не найдены.")
    
    # Открываем COM-порт
    print("\nОткрываем COM-порт")
    ser = serial.Serial(port, baudrate = 9600)

    # Выполнение операций на COM-порту
    # Чтение данных
    print("\nЧтение данных...")
    data = ser.read(32)  # Прочитать 28 байт из COM-порта №5 на скорости 9600 
    # бод. Внизу можно посмотреть какой скетч написан для Arduino
    print("Прочитанные данные:")
    print(data)
    
    # Открываем COM-порт
    print("\nЗакрываем COM-порт")
    ser.close()  # Close the connection when done
    print("Соединение с COM-портом закрыто.")

except ValueError as ve:
    print("Ошибка:", str(ve))

except serial.SerialException as se:
    print("Ошибка на Serial-порту:", str(se))

except Exception as e:
    print("Произошла ошибка:", str(e))










#/* 
# * Программа для работы с дисплеем и получение/отправление данных 
# * от программы с кодом написанным на Python с использованием
# * библиотеки PySerial.
# */
#
##include <GyverOLED.h>
#
#// Используем буфер на стороне контроллера
##define OLED_SOFT_BUFFER_64
#
#// Выбор настройки для дисплея
#GyverOLED<SSH1106_128x64> oled;
#
#void setup() {
#  delay(50);
#  pinMode(13, OUTPUT);
#  Serial.begin(9600);
#}
#
#void loop() {
#  Serial.println("click");
#  digitalWrite(13, HIGH);
#  delay(500);
#  Serial.println("-");
#  digitalWrite(13, LOW);
#  delay(500);
#  Serial.println("clack");
#  digitalWrite(13, HIGH);
#  delay(500);
#  for (int i = 0; i < 5; i++) {
#    Serial.println("click-clack");
#    delay(50);
#    Serial.println("           ");
#    delay(50);
#  }
#}
