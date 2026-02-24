import socket

# This is the "target" we want to check
target = "google.com"
port = 80

communication_tool = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
communication_tool.settimeout(2)

result = communication_tool.connect_ex((target, port))

if result == 0:
    print("The door is OPEN!")
else:
    print("The door is CLOSED.")

communication_tool.close()