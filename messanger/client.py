import socket
import threading
import os

def listen_for_Client(cs)
while True:
   try:
      msg = cs.recv(1024).decode()