# client.py
#
# Copyright 2002,2003 Wichert Akkerman <wichert@deephackmode.org>

"""Generic RADIUS client"""

__docformat__	= "epytext en"

import md5, select, socket
import host, packet

class Timeout(Exception):
	"""Simple exception class which is raised when a timeout occurs
	while waiting for a RADIUS server to respond."""
	pass


class Client(host.Host):
	"""Basic RADIUS client.

	This class implements a basic RADIUS client. It can send requests
	to a RADIUS server, taking care of timeouts and retries, and 
	validate its replies.

	@ivar retries: number of times to retry sending a RADIUS request
	@type retries: integer
	@ivar timeout: number of seconds to wait for an answer
	@type timeout: integer
	"""
	def __init__(self, server, authport=1812, acctport=1813, secret="", dict=None):
		"""Constructor.

		@param   server: hostname or IP address of RADIUS server
		@type    server: string
		@param authport: port to use for authentication packets
		@type  authport: integer
		@param acctport: port to use for accounting packets
		@type  acctport: integer
		@param   secret: RADIUS secret
		@type    secret: string
		@param     dict: RADIUS dictionary
		@type      dict: pyrad.dictionary.Dictionary
		"""
		host.Host.__init__(self, authport, acctport, dict)

		self.server=server
		self.secret=secret
		self._socket=None
		self.retries=3
		self.timeout=5
	

	def _SocketOpen(self):
		if not self._socket:
			self._socket=socket.socket(socket.AF_INET, 
				socket.SOCK_DGRAM)


	def _CloseSocket(self):
		if self._socket:
			self._socket.close()
			self._socket=None
	

	def CreateAuthPacket(self, **args):
		"""Create a new RADIUS packet.

		This utility function creates a new RADIUS packet which can
		be used to communicate with the RADIUS server this client
		talks to. This is initializing the new packet with the
		dictionary and secret used for the client.

		@return: a new empty packet instance
		@rtype:  pyrad.packet.Packet
		"""
		return host.Host.CreateAuthPacket(self, secret=self.secret, **args)


	def CreateAcctPacket(self, **args):
		"""Create a new RADIUS packet.

		This utility function creates a new RADIUS packet which can
		be used to communicate with the RADIUS server this client
		talks to. This is initializing the new packet with the
		dictionary and secret used for the client.

		@return: a new empty packet instance
		@rtype:  pyrad.packet.Packet
		"""
		return host.Host.CreateAcctPacket(self, secret=self.secret, **args)


	def _SendPacket(self, pkt, port):
		"""Send a packet to a RADIUS server.

		@param pkt:  the packet to send
		@type pkt:   pyrad.packet.Packet
		@param port: UDP port to send packet to
		@type port:  integer
		@return:     the reply packet received
		@rtype:      pyrad.packet.Packet
		@raise Timeout: RADIUS server does not reply
		"""

		self._SocketOpen()

		for attempt in range(self.retries):
			self._socket.sendto(pkt.RequestPacket(), (self.server, port))

			ready=select.select([self._socket], [], [], 
				self.timeout)
			if ready[0]:
				rawreply=self._socket.recv(4096)
			else:
				continue

			try:
				reply=pkt.CreateReply(dict=self.dict, packet=rawreply)
			except packet.PacketError:
				continue

			if not pkt.VerifyReply(reply, rawreply):
				continue

			break
		else:
			raise Timeout

		return reply


	def SendPacket(self, pkt):
		"""Send a packet to a RADIUS server.

		@param pkt: the packet to send
		@type pkt:  pyrad.packet.Packet
		@return:    the reply packet received
		@rtype:     pyrad.packet.Packet
		@raise Timeout: RADIUS server does not reply
		"""
		if isinstance(pkt, packet.AuthPacket):
			return self._SendPacket(pkt, self.authport)
		else:
			return self._SendPacket(pkt, self.acctport)
