import socket
import threading
import os
from dotenv import load_dotenv
from flaskModule.app import run_app
from socketData import socket_send_data

load_dotenv()

# server config
host = os.getenv('HOST')
port = int(os.getenv('PORT'))
maxUsr = int(os.getenv('MAX_USR'))

# server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.setblocking(True)
server.listen(maxUsr)

# initial
# restful flask framework
threading._start_new_thread(run_app())

# socket
while True:
    print("wait...", flush=True)
    client, addr = server.accept()
    print('Connected by ', addr[0], flush=True)
    threading._start_new_thread(socket_send_data, (client,))
