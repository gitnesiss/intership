from pymavlink import mavutil

# Запустить прослушивание соединения на UDP порту
# the_connection = mavutil.mavlink_connection('udpin:localhost:14551')
the_connection = mavutil.mavlink_connection("COM5", baud=57600)

# Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

# Once connected, use 'the_connection' to get and send messages