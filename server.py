import socket
from threading import Thread

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
ip="127.0.0.1"
port=8000
server.bind((ip,port))
server.listen()

clients=[]
nicknames=[]
print("Server is running...")

def clientthread(con,nickname):
    con.send("Welcome to the chat room".encode("utf-8"))
    while True:
        try:
            message=con.recv(2048).decode("utf-8")
            if message:
                print(message)
                broadcast(message,con)
            else:
                remove(con)
                removeNickname(nickname)
        except:
            continue
def broadcast(message,con):
    for i in clients:
        if i !=con:
            try:
                i.send(message.encode("utf-8"))
            except:
                remove(i)
def remove(con):
    if con in clients:
        clients.remove(con)
def removeNickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)
    
while True:
    con,adr=server.accept()
    con.send("NICKNAME".encode("utf-8"))
    nickname=con.recv(2048).decode("utf-8")
    clients.append(con)
    nicknames.append(nickname)
    message="{} joined".format(nickname)
    print(message)
    broadcast(message,con)
    newThread=Thread(target=clientthread,args=(con,nickname))
    newThread.start()
