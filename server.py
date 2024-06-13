import socket

#Este codigo es para TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('192.168.180.237', 12345))

s.listen()

conn, addr = s.accept()

data = conn.recv(1024)

conn.sendall("Message for client".encode())

print(data)

s.close()

#Este codigo es para UDP 

# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# s.bind(('localhost', 12345))

# data, addr = s.recvfrom(1024)

# s.sendto("Message for client".encode(), addr)

# print(data)

# s.close()

