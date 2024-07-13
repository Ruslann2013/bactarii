import socket

new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
new_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
new_socket.connect(('localhost', 10000))
while True:
    new_socket.send('Привет'.encode())