import serial
import serial.tools.list_ports

try:
    # НАйти и открыть COM-порт
    ports = serial.tools.list_ports.comports()
    port = next((p.device for p in ports), None)

    # Вывод в терминал или консоль доступных COM-портов.
    for port_one in ports:
        print(port_one.device)

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