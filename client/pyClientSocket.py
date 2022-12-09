import socket

HOST = '127.0.0.1'
PORT = 9943

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(s.getpeername(), flush=True)

while True:
    serverMessage = str(s.recv(1024), encoding='utf-8')
    print(serverMessage, flush=True)
