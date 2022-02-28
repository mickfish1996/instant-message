import socket      
import threading
from threading import Thread
import os

#AF_INET used for IPv4
#SOCK_DGRAM used for UDP protocol
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
#binding IP and port 
server = socket.gethostbyname(socket.gethostname())
server_port = 2222
separator_token = "<sep>"

client_sockets = set()

s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

s.bind((server, server_port))

s.listen(5)

print(f"[*] Listening as {server}:{server_port}")


def listen_for_Client(cs):
       while True:
              try:
                     msg = cs.recv(1024).decode()
                     
              except Exception as e:
                     print(f"[!] Error: {e}")
                     client_sockets.remove(cs)
                     
              else:
                     msg = msg.replace(separator_token, ": ")
              
              for client_socket in client_sockets:
                     client_socket.send(msg.encode())
                     
while True:
       client_socket, client_address = s.accept()
       print(f"[+] {client_address} connected.")
       
       client_sockets.add(client_sockets)
       
       t = Thread(target = listen_for_Client, args = (client_socket,))
       
       t.daemon = True
       
       t.start()
       
for cs in client_sockets:
       cs.close()
       
s.close