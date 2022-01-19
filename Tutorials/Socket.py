import socket

s=socket.socket()
#this bind function is to bind the server with localhost with port number
s.bind(('localhost',45678))
#it will listen at a time 3 requests
s.listen(3)
print("Server Started")

while True:
    c,add=s.accept()
    name=c.recv(1024).decode()
    print("connected with address ",add)
    c.send(bytes("Welcome to Socket Programing "+name,'utf-8'))
#this recv function is for receving the information from client in bytes

