#!/usr/bin/env python

import socket
import time

#create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host, 
# and a well-known port
serversocket.bind((socket.gethostname(), 8870))
#become a server socket
serversocket.listen(5)

(con_sock, con_addr) = serversocket.accept()
data = con_sock.recv(2048)
print data

while (1):
	time.sleep(1000)
