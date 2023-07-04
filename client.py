import socket
from threading import Thread
from tkinter import *

# nickname=input("Choose your nickname:")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip="127.0.0.1"
port=8000
client.connect((ip,port))
print("Connected with the server")

class GUI:
    def __init__(self):
        self.Window=Tk()
        self.Window.withdraw()
        self.login=Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300)
        self.text=Label(self.login,text="Please enter username to continue",justify=CENTER,font="Helvetica 14 bold")
        self.text.place(relheight=0.15,relx=0.1,rely=0.07)

        self.name=Label(self.login,text="Name:",font="Helvetica 12")
        self.name.place(relheight=0.2,relx=0.1,rely=0.2)

        self.entryBox=Entry(self.login,font="Helvetica 14")
        self.entryBox.place(relwidth=0.4,relheight=0.12,relx=0.35,rely=0.25)
        self.loginButton=Button(self.login,text="Login",font="Helvetica 14 bold",command=lambda:self.goAhead(self.entryBox.get()))
        self.loginButton.place(relx=0.4,rely=0.55)

        self.Window.mainloop()

    def goAhead(self,name):
        self.login.destroy()
        self.name=name
        rcv=Thread(target=self.receive)
        rcv.start()


    def receive(self):
        while True:
            try:
                message=client.recv(2048).decode("utf-8")
                if message=="NICKNAME":
                    client.send(self.name.encode("utf-8"))
                else:
                    pass
            except:
                print("An error occured")
                client.close()
                break
g=GUI()
# def write():
    # while True:
        # message="{}:{}".format(nickname,input(""))
        # client.send(message.encode("utf-8"))

# receiveThread=Thread(target=receive)
# receiveThread.start()
# writeThread=Thread(target=write)
# writeThread.start()
