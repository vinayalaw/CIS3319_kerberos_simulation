# FILENAME: client.py
# AUTHOR: Vinayak Desai

import socket
import sys
import ipaddress
import time
import datetime
import pickle

#Initial setup
host = '127.0.0.1'
idC = "CIS3319USERID"
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
print("Socket successfully created\n")

#AS communication
s.connect((host, portS))
print(pickle.loads(s.recv(1024)))

timestamp = datetime.datetime.now
message = [idC, idTGS, timestamp]

s.send(pickle.dumps(message))
print("Request for TGT sent!")
returnMsg = pickle.loads(s.recv(1024))
tgt = returnMsg[4]
print("TGT received!\n")

#TGS communication
message = [idV, tgt]

s.send(pickle.dumps(message))
print("Request for service ticket sent!")
returnMsg = pickle.loads(s.recv(1024))
print("Service ticket received!\n")

#new socket setup
s.close
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created\n")

#Service communication
s.connect((host, portV))
print(pickle.loads(s.recv(1024)))

s.send(pickle.dumps(returnMsg[3]))
print("Request for service sent!")
returnMsg = pickle.loads(s.recv(1024))
print("Service authenticated!\n")

#end of client
s.close()
exit(0)