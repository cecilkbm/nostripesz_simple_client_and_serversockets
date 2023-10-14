#! /usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating the socket object

host = socket.gethostbyname()
port = 3030

serversocket.bind((host, port)) #bind to the socket

serversocket.listen(3) #listen for up to 3 connections

while True:
    clientsocket, address = serversocket.accept() #starting the connection

    print("connection recieved " % str(address))

    message = 'You are now connected to the Server' + "\r\n"
    clientsocket.send(message)

    clientsocket.close()