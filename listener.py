import socket
from time import sleep

_HOST = 'localhost'
_PORT = 3000

s = socket.socket()
s.bind((_HOST, _PORT))
print(f'Aguardando conexão na porta: {_PORT}')

s.listen(5)
conn, address = s.accept()
print(f'Recebendo soliciação de {address}')

messages = [
    'Hello World, Streaming!',
    'Eu sou Luigi',
    'Cursando Spark Streaming na Alura',
    'DataNoCaps',
    'Parabéns, o trem tá rodando',
    'Final da lista'
]

for message in messages:
    message = bytes(message, 'utf-8')
    conn.send(message)
    sleep(4)

conn.close()