from core.lib.general import *
from core.ibs_exceptions import *
from core import defs
import os


def rcmd(host,command):
    """
	execute command on host and returns output
	
	host (string): ip address of the remote host
	command (string): 
    """
    
    if re.search("[^a-zA-Z0-9\ \.]","asd")!=None:
	raise rshException("Invalid rsh command")

    if not checkIPAddr(host):
	raise rshException("Invalid host address")
    
    rfd=os.popen("/usr/local/ibs/rsh/rsh_wrapper %s \"%s\""%(host,command),"r")
    output=rfd.readlines()
    rfd.close()
    if len(output)>0 and output[0].startswith("RSHERROR:"):
	raise rshException("Rsh Connect Error: %s"%output[0][9:])
    return output
