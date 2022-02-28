# Instant Messaging App

This software will create a peer to peer connection and allow the users of the two computers to send messages back and forth, currently you need to enter the port 
and ip address of the other computer for this to work.

The reason That I want to write this software is because I want to learn how networking works and I think that this is a good first step to take to learning it.

[Software Demo Video](https://youtu.be/S5oN9BrsJbU)

# Network Communication

The architecture that I am currently using for this software is peer to peer. in the future I am wanting to make the transition to a client server connection.

I am using a UDP connection, the reason being that when I was researching networking I saw that UDP was faster, though when I transition over to the client server setup
I will make it a tcp connection.

The format of the messages being sent are encoded and passed using threading.

# Development Environment

The tools that I am using for this is VS code

I am using python as the languge and I am using the socket and threading packages.

# Useful Websites

* [Geeks for Geeks](https://www.geeksforgeeks.org/simple-chat-room-using-python/)
* [Plain English](https://python.plainenglish.io/chat-app-using-udp-5b486241748c)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Transition to client server setup
* Create GUI
