import re

def checkMacAddress(mac_addr):
    """
	return True if mac_addr is valid, else return False
    """
    if re.match("[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}",mac_addr)!=None:
	return True
    return False
    