#!/usr/bin/python

import xmlrpclib
import sys


def printUsage():
    print """
	Usage: client.py <filename> <system password>
	
	    filename: filename containing python codes to run in running ibs
    
    """
    

def readFile(file_name):
    fd=open(file_name)
    contents=fd.read(1024*1024)
    fd.close()
    return contents

def sendRequest(contents,system_password):
    server=xmlrpclib.ServerProxy("http://localhost:1235")
    return getattr(server,"util.runDebugCode")({"command":contents,
						"auth_name":"system",
						"auth_pass":system_password,
						"auth_type":"ADMIN",
						"auth_remoteaddr":"127.0.0.1"
						})


def main():
    if len(sys.argv)!=3:
	printUsage()
	sys.exit(1)

    file_name=sys.argv[1]
    system_password=sys.argv[2]
    contents=readFile(file_name)
    result=sendRequest(contents,system_password)
    print result

if __name__=="__main__":
    main()
    
