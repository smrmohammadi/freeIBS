from pysnmp.proto import v1, v2c
from pysnmp.mapping.udp import role
import pysnmp.proto.api.generic
import pysnmp.proto.cli.ucd
from core import defs
from core.lib.general import *
from core.ibs_exceptions import *

#from pysnmp.proto import v1
#from pysnmp.proto.api import generic
#from pysnmp.mapping.udp import role




def snmpset(host,community,oid,_type,value,port=161):
    client = role.manager((host,port))
    # Pass it a few options
    client.timeout = defs.SNMP_TIMEOUT
    client.retries = defs.SNMP_RETRIES
    req = v2c.SetRequest()

    # Initialize request message from C/L params
    try:
	req.cliUcdSetArgs([community,oid,_type,value])
    except Exception,e:
	toLog("snmpset failed on oid %s %s %s %s %s %s "%(host,port,oid,_type,value,e))
	raise generalException("snmpset failed for %s %s %s %s"%(host,oid,_type,value))

    # Create SNMP response message framework
    rsp = v2c.GetResponse()


    def cb_fun(answer, src):
	"""This is meant to verify inbound messages against out-of-order
        messages
	"""
	# Decode message
	rsp.decode(answer)
        
	# Make sure response matches request
	if req.match(rsp):
    	    return 1

    # Encode SNMP request message and try to send it to SNMP agent and
    # receive a response
    try:
	(answer, src) = client.send_and_receive(req.encode(), (None, 0), cb_fun)
    except Exception,e:
	toLog("snmpset failed %s %s %s %s %s %s "%(host,port,oid,_type,value,e))
	raise generalException("snmpset failed for %s %s %s %s"%(host,oid,_type,value))

    # Fetch Object ID's and associated values
    vars = rsp.apiGenGetPdu().apiGenGetVarBind()

    # Check for remote SNMP agent failure
    if rsp.apiGenGetPdu().apiGenGetErrorStatus():
	toLog("snmpset response packet: %s %s %s %s %s %s"%(rsp['pdu'].values()[0]['error_status'],vars[rsp.apiGenGetPdu().apiGenGetErrorIndex()-1][0],host,oid,_type,value))
	raise generalException("snmpset: error in response packet")

def snmpwalk(host,community,oid,detailed=0,port=161):
    client = role.manager((host, port))
    client.timeout = defs.SNMP_TIMEOUT
    client.retries = defs.SNMP_RETRIES
    snmp=v2c
    req = snmp.GetRequest(); nextReq = snmp.GetNextRequest()
    ret={}

    # Initialize request message from C/L params
    req.cliUcdSetArgs([community,oid]); nextReq.cliUcdSetArgs([community,oid])
    
    rsp = snmp.Response()
    
    # Store tables headers
    # print req.apiGenGetPdu().apiGenGetVarBind()
    headVars = map(lambda x: x[0], req.apiGenGetPdu().apiGenGetVarBind())
    #    headVars = ['.1']

    # Traverse agent MIB
    while 1:
	def cb_fun(answer, src):
    	    """This is meant to verify inbound messages against out-of-order
            messages
    	    """
    	    # Decode message
    	    rsp.decode(answer)
        
    	    # Make sure response matches request
    	    if req.match(rsp):
        	return 1
        
	# Encode SNMP request message and try to send it to SNMP agent and
	# receive a response
	(answer, src) = client.send_and_receive(req.encode(), (None, 0), cb_fun)

	# Fetch Object ID's and associated values
	vars = rsp.apiGenGetPdu().apiGenGetVarBind()

	# Check for remote SNMP agent failure
	if rsp.apiGenGetPdu().apiGenGetErrorStatus():
    	    # SNMP agent reports 'no such name' when walk is over
    	    if rsp.apiGenGetPdu().apiGenGetErrorStatus() == 2:
        	# Switch over to GETNEXT req on error
        	# XXX what if one of multiple vars fails?
        	if not (req is nextReq):
            	    req = nextReq
            	    continue
        	# One of the tables exceeded
        	for l in vars, headVars:
            	    del l[rsp['pdu'].values()[0]['error_index'].get()-1]
        	if not vars:
            	    sys.exit(0)
    	    else:
        	raise str(rsp['pdu'].values()[0]['error_status']) + ' at '\
                    + str(vars[rsp.apiGenGetPdu().apiGenGetErrorIndex()-1][0])

	# Exclude completed var-binds
	while 1:
    	    for idx in range(len(headVars)):
        	if not snmp.ObjectIdentifier(headVars[idx]).isaprefix(vars[idx][0]):
            	    # One of the tables exceeded
            	    for l in vars, headVars:
                	del l[idx]
            	    break
    	    else:
        	break

#	print headVars
	if not headVars:
    	    return ret

	# Print out results
	for (oid, val) in vars:
    	    if detailed:
		ret[oid]=val
    	    else:
		ret[oid]=repr(val.get())

	# Update request ID
	req.apiGenGetPdu().apiGenSetRequestId(req.apiGenGetPdu().apiGenGetRequestId()+1)

	# Switch over GETNEXT PDU for if not done
	if not (req is nextReq):
    	    req = nextReq

	# Load get-next'ed vars into new req
	req.apiGenGetPdu().apiGenSetVarBind(vars)
    