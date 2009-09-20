#!/usr/bin/env python

import socket
import thread
import time

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = "192.168.0.1"
port = 80


def try_connect(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((host,port));
	except:
		return
	print host

for i in range(2,9900):
    port = i
    thread.start_new_thread(try_connect, ("192.168.0." + str(i),port))
    time.sleep(0.1)

time.sleep(20)


