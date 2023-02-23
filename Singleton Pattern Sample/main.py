from CentralServer import CentralServer
from Client import Client

# Instances
client1 = Client("computer", "cable")
client2 = Client("smartphone", "wi-fi")
client3 = Client("computer", "wi-fi")

# Connection establishment
central_server = CentralServer.get_central_server()
client1.establish_connection(central_server)
client2.establish_connection(central_server)
client3.establish_connection(central_server)

# Printing values
print("Client 1 type:", client1.get_type())
print("Client 1 communication:", client1.get_communication())
print("Client 1 connection:", client1.get_connection())

print("Client 2 type:", client2.get_type())
print("Client 2 communication:", client2.get_communication())
print("Client 2 connection:", client2.get_connection())

print("Client 3 type:", client3.get_type())
print("Client 3 communication:", client3.get_communication())
print("Client 3 connection:", client3.get_connection())

# Attempt to directly instantiate CentralServer 
try:
    new_server = CentralServer()
    print("CentralServer instance created.")
except Exception as e:
    print("Error:", e)
