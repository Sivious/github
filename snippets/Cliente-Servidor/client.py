#!/usr/bin/python

import socket
import sys

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSocket.connect((sys.argv[1], 8000))

userInput = "dummy"

while 1 and userInput <> "quit":
	userInput = raw_input("Please enter a string: ")
	tcpSocket.send(userInput)
	print tcpSocket.recv(2048)

tcpSocket.close()
