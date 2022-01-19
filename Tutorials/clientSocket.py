import  socket

c=socket.socket()
c.connect(('localhost',45678))
name=input("enter name ")
c.send(bytes(name,"utf-8"))
output=c.recv(1024).decode()
print(output)