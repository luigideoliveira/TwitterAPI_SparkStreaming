import socket
from time import sleep

_HOST = 'localhost'
_PORT = 3000

s = socket.socket()
s.connect((_HOST, _PORT))

while True:
    data = s.recv(1024)
    print(data.decode('utf-8'))
    sleep(2)