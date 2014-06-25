#!/usr/bin/env python

import socket 

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#sentencia para que, si se cae el server, el socket se cierre y 
#este reutilizable en poco tiempo

tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpSocket.bind(("0.0.0.0", 8000)) 

#Escuchar conexiones, el argumento 2 indica el numero de conexiones
#simultaneas que puede manejar

tcpSocket.listen(2)

print "Waiting for a client..."

#Continuacion se debe indicar que se aceptan las conexiones
(client, (ip, port)) = tcpSocket.accept()

#Enviamos un mensaje al cliente
client.send("Welcome to THE SERVER")

print "Received connection from : ", ip

print "Starting ECHO output ... "

data = 'dummy'

while len(data) :
	data = client.recv(2048)
	print "*********************"
	print "Client sent: ", data
	client.send(data) 

print "Closing connection ..."
client.close()

print "Shutting down server ..."
tcpSocket.close()

