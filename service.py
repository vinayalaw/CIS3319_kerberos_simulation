# FILENAME: service.py
# AUTHOR: Vinayak Desai

import socket
import sys
import ipaddress
import time
import datetime
import pickle

host = '127.0.0.1'
portV = 8002
lifetime4 = 86400
keyV = 0

#Socket setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")
s.bind((host, portV))
s.listen(5)
c, addr = s.accept()
print("Client connection acknowledged!")
c.send(pickle.dumps("Connection Acknowldged!\n"))

#client communication(V)
request = pickle.loads(c.recv(1024))
timestamp = request[3] + 1
c.send(pickle.dumps(timestamp))

#end of service
s.close
exit(0)