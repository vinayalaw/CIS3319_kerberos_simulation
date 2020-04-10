# FILENAME: server.py
# AUTHOR: Vinayak Desai

import socket
import sys
import ipaddress
import time
import datetime
import pickle

#Initial setup
host = '127.0.0.1'
idV = "CIS3319SERVERID"
idTGS = "CIS3319TGSID"
portS = 8000
portV = 8002
lifetime2 = 60
lifetime4 = 86400
keyV = 0
keyTGS = 0 

#Socket setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")
s.bind((host, portS))
s.listen(5)
c, addr = s.accept()
print("Client connection acknowledged!")
c.send(pickle.dumps("Connection Acknowldged!\n"))

#Client communication(AS)
request = pickle.loads(c.recv(1024))
idC = request[0]
print("Request for TGT received!")

timestamp = datetime.datetime.now
ticketTGS = [keyTGS, request[0], request[1], timestamp, lifetime2]
message = [keyTGS, request[1], timestamp, lifetime2, ticketTGS]

c.send(pickle.dumps(message))
print("TGT sent to client!\n")

#Client communication(TGS)
request = pickle.loads(c.recv(1024))
print("Request for service ticket received!")

timestamp = datetime.datetime.now
ticketV = [keyV, idC, request[0], timestamp, lifetime4]
message = [keyV, request[0], timestamp, ticketV]

c.send(pickle.dumps(message))
print("Service Ticket sent to client!\n")

#end of server
s.close()
exit(0)