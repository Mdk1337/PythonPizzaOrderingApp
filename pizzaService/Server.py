import socket
import pickle
import random

from pizzaService import Pizza

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((socket.gethostname(), 13337))
sock.listen(5)

client, addr = sock.accept()
print (f"Client connected. {addr}")
msg = client.recv(1024)
pizza = pickle.loads(msg)

timeToDeliver = random.randint(10, 51)
client.send(str(timeToDeliver).encode("utf-8"))

print(pizza.__str__())