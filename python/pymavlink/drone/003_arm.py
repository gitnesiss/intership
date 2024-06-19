from pymavlink import mavutil

# Start a connection listening on a UDP port
# the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

# Запустить прослушивание соединения на COM-порту
the_connection = mavutil.mavlink_connection("COM5", baud=57600)

# Дождитесь первого heartbeat
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

# По этой ссылке посмотреть следующую команду
# https://mavlink.io/en/services/command.html
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)
#                                                                                     ^
#                                                                                     |
#                                                          Параметр отвечающий за режим "ARM" или "READY TO FLY"