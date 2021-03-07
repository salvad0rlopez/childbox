#!/usr/bin/python

import os
import socket
import sys
import json
from interprete import *

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 2903)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
x = interprete_comandos("joder")
# Listen for incoming connections
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        connection.sendall("Childbox pi content Management System v0.1\n")
        connection.sendall("Esperando clave:")

        while True:
            data = connection.recv(250)
            print('recibido {!r}'.format(data))
            if data:
                connection.sendall("Comando recibido"+data)
                if data.find("\x04")<>-1: # si pulsamos control + D
                    print "quieres salir?, adios!s"
                    connection.close()
                else:
                    x.interpretar(data)
            else:
                print('no data from', client_address)
                break 

    finally:
        # Clean up the connection
        connection.close()