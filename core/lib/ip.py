"""
    some wrappers for IPy, use IPy directly if you need more complete API
"""

from core.lib import IPy
from core import defs
from core.errors import errorText

def isIPAddrIn(ip_addr,ip_addrrange):
    """
	check if addr is in addrrange
	return 1 if it is, and 0 if it's not
    """
    try:
	ip=IPy.IP(ip_addr)
	iprange=IPy.IP(ip_addrrange)
	if ip in iprange:
	    return 1
	return 0
    except:
	logException(LOG_ERROR,"isIPAddrIn")
	raise GeneralException(errorText("GENERAL","INVALID_IP_ADDRESS")%ip_addr)


def checkIPAddr(ip_addr):
    """
	check ip_addr if it's valid, it can be in format x.x.x.x or x.x.x.x/y.y.y.y
	in case of ip/netmask netmask is checked for validity too
	return 1 if it's valid and 0 if it's not
    """
    try:
	ip=IPy.IP(ip_addr)
	return True
    except:
	return False

def checkIPAddrWithoutMask(addr):
    if addr.find("/")!=-1:
	return False
    if len(addr.split('.')) != 4:
	return False
    try:
	ip=IPy.IP(addr)
	return True
    except:
	return False

#########################################
