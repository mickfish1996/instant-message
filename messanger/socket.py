import socket
import threading
import os

class Sockets():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(("192.168.0.105", 2222))
        self.nm = None
        self.ip = None
        self.port = None
        
    def set_name(self):    
        print("\t\t\t====>  UDP CHAT APP  <====")
        print("==============================================")
        self.nm = input("ENTER YOUR NAME: ")
        print("\nType 'quit' to exit.")

        self.ip,self.port = input("Enter IP address and Port Number: ").split()

    def send(self):    
        ms = input(">> ")
        if ms == "quit":
            os._exit(1)
        sm = f"{self.nm}  : {ms}"
        self.s.sendto(sm.encode(), (self.ip,int(self.port)))

    def rec(self):
        while True:
            msg = self.s.recvfrom(1024)
            print("\t\t\t\t >> " +  msg[0].decode()  )
            print(">> ")
            
    def begin(self):
        x1 = threading.Thread( target = self.send )
        x2 = threading.Thread( target = self.rec )

        x1.start()
        x2.start()