import sys
from core.lib import *
from core.ibs_exceptions import *
from core import defs
from pyrad import dictionary, packet, server
from core.ras import ras_main
from core.threadpool import thread_main
import socket


def init():
    global radius_server_started
    radius_server_started=False

    if defs.RADIUS_SERVER_ENABLED==0:
	return

    toLog("Initializing IBS Radius Server",LOG_DEBUG)
    global ibs_dic
    ibs_dic=dictionary.Dictionary("%s/radius_server/dictionary"%defs.IBS_ROOT)
    
    srv=IBSRadiusServer(dict=ibs_dic,addresses=defs.RADIUS_SERVER_BIND_IP,authport=defs.RADIUS_SERVER_AUTH_PORT,acctport=defs.RADIUS_SERVER_ACCT_PORT)
    srv.hosts=ras_main.getLoader().getRadiusRemoteHosts()
    thread_main.runThread(srv.Run,[],"radius")
    radius_server_started=True

def shutdown():
    if not radius_server_started:
	return
	    
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.connect((defs.RADIUS_SERVER_IP,defs.RADIUS_SERVER_ACCT_PORT))
    sock.send("\n")
    sock.close()


class IBSRadiusServer(server.Server):
	def __logRequest(self,request_pkt, request_type):
	    toLog("##############",LOG_RADIUS)
	    toLog("%s attributes from %s"%(request_type,request_pkt.source[0]),LOG_RADIUS)
	    attrs=map(lambda attr_name:"%s: %s"%(attr_name,request_pkt[attr_name]),request_pkt.keys())
	    toLog(" \n".join(attrs),LOG_RADIUS)


	def _HandleAuthPacket(self, fd, pkt):
		server.Server._HandleAuthPacket(self, fd, pkt)
	        if defs.LOG_RADIUS_REQUESTS:
		    self.__logRequest(pkt,"Authenticate")
	    
		reply=self.CreateReplyPacket(pkt)
		reply.dict=ibs_dic

		success=False
		try:
		    success=ras_main.getLoader().getRasByIP(pkt.source[0])._handleRadAuthPacket(pkt,reply)
		except:
		    logException(LOG_ERROR,"HandleAuthPacket Exception:\n")
	    
		if success: #accress ACCEPT	
		    reply.code=packet.AccessAccept
		else:
		    reply.code=packet.AccessReject
		    
		self.SendReplyPacket(fd, reply)
	
	def _HandleAcctPacket(self, fd, pkt):
		server.Server._HandleAcctPacket(self, fd, pkt)
	        if defs.LOG_RADIUS_REQUESTS:
		    self.__logRequest(pkt,"Accounting")
		
    		reply=self.CreateReplyPacket(pkt)		
		try:
		    ras_main.getLoader().getRasByIP(pkt.source[0])._handleRadAcctPacket(pkt,reply)
		except:
		    logException(LOG_ERROR,"HandleAcctPacket exception\n")

		self.SendReplyPacket(fd, reply)

