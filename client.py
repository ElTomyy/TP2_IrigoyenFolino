import socket

#Este codigo es para UDP
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Este codigo es para TCP 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Iniciando enlace nuclear")

s.connect(('192.168.180.237', 2200))

print("BOBMA DETONADAaaaaAAAAAaAA")

s.send("Hola Servidor".encode())

response = s.recv(1024).decode()

print(response)



