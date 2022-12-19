import socket

HOST = socket.gethostbyname('localhost')
PORT = 9898

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

while True:
  msg = socket.recv(2048)
  print(msg.decode("utf-8"), end= '', flush=True)
