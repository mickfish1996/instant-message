import socket
import threading
import os

class Sockets():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # gets the current IP address of the system.
        server = socket.gethostbyname(socket.gethostname())

        # sets the port to 2222, because that is an easy number to remember.
        socketport = 2222
        self.s.bind((server, socketport))

        # Prints your IP and port so that the user knows what their IP is.
        print(server, socketport)
        self.nm = None
        self.ip = None
        self.port = 2222
        
    def set_name(self):    
        print("\t\t\t====>  UDP CHAT APP  <====")
        print("==============================================")
        # You can enter the name that you would like to use in your chat window.
        self.nm = input("ENTER YOUR NAME: ")
        print("\nType 'quit' to exit.")
         # The user sets the IP address that they would like to send to using the IP's at the 
         # top of the screen.
        self.ip = input("Enter IP address: ")

    # This function will send the the message with the users name in an encoded transfer.
    def send(self):    
        ms = input(">> ")
        if ms == "quit":
            os._exit(1)
        sm = f"{self.nm}  : {ms}"
        self.s.sendto(sm.encode(), (self.ip,int(self.port)))

    # This will Recive the message that was sent to it. It will decode the message
    # and will display it on the right side of the screen.
    def rec(self):
        while True:
            msg = self.s.recvfrom(1024)
            print("\t\t\t\t >> " +  msg[0].decode()  )
            print(">> ")

    # This will listen for the sending and reciveing the messages.   
    def begin(self):
        x1 = threading.Thread( target = self.send )
        x2 = threading.Thread( target = self.rec )

        x1.start()
        x2.start()