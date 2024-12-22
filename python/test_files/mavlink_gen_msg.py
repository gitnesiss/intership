#!/usr/bin/env python

"""
Сгенерируйте сообщение, используя разные версии MAVLink, поместите его в буфер и затем прочитайте из него.
"""

from __future__ import print_function
from builtins import object

from pymavlink.dialects.v10 import ardupilotmega as mavlink1
from pymavlink.dialects.v20 import ardupilotmega as mavlink2

class fifo(object):
    def __init__(self):
        self.buf = []
    def write(self, data):
        self.buf += data
        return len(data)
    def read(self):
        return self.buf.pop(0)

def test_protocol(mavlink, signing=False):
    # мы будем использовать fifo как буфер кодирования/декодирования
    f = fifo()

    print("Создание сообщения MAVLink...")
    # создайте экземпляр mavlink, который будет выполнять ввод-вывод на файловом объекте 'f'
    mav = mavlink.MAVLink(f)

    if signing:
        mav.signing.secret_key = bytearray(chr(42)*32, 'utf-8' )
        mav.signing.link_id = 0
        mav.signing.timestamp = 0
        mav.signing.sign_outgoing = True

    # установите параметр WP_RADIUS на MAV в конце ссылки
    mav.param_set_send(7, 1, b"WP_RADIUS", 101, mavlink.MAV_PARAM_TYPE_REAL32)

    # если хотите, в качестве альтернативы создайте объект MAVLink_param_set, 
    # который можно отправить через ваш собственный транспорт
    m = mav.param_set_encode(7, 1, b"WP_RADIUS", 101, mavlink.MAV_PARAM_TYPE_REAL32)

    m.pack(mav)

    # get the encoded message as a buffer
    b = m.get_msgbuf()

    bi=[]
    for c in b:
        bi.append(int(c))
    print("Буфер, содержащий закодированное сообщение:")
    print(bi)

    print("Расшифровка сообщения...")
    # декодировать входящее сообщение
    m2 = mav.decode(b)

    # показать какие поля у него есть
    print("Получил сообщение с идентификатором %u и поля %s" % (m2.get_msgId(), m2.get_fieldnames()))

    # распечатать поля
    print(m2)


print("Тестирование mavlink1\n")
test_protocol(mavlink1)

print("\nТестирование mavlink2\n")
test_protocol(mavlink2)

print("\nТестирование mavlink2 с подписью\n")
test_protocol(mavlink2, True)