#!/usr/bin/python -O
import sys
sys.path.append("/usr/local/ibs")
import string
import ibs_client

s=ibs_client.SendCommand()
command=string.replace(sys.argv[1],",",chr(255))
s.send(command + "\r\n")
print s.recv()
s.close()
