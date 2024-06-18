from pymavlink import mavutil

# Start a connection listening on a UDP port
# the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

# Запустить прослушивание соединения на COM-порту
the_connection = mavutil.mavlink_connection("COM5", baud=57600)

# Дождитесь первого heartbeat
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

# Once connected, use 'the_connection' to get and send messages

while 1:
    msg = the_connection.recv_match(type='SYSTEM_TIME', blocking=True)
    print(msg)