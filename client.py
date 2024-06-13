import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 12345))

s.send("Hola Servidor".encode())

response = s.recv(1024).decode()

