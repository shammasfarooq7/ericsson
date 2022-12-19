import socket
import getch
HOST = socket.gethostbyname('localhost')
PORT = 9898
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((HOST, PORT))
socket.listen()

while True:
  clientsocket, address = socket.accept()
  print(f"connetion established")
  while True:
    data_stream = getch.getche()
    clientsocket.send(bytes(data_stream, 'utf-8'))
