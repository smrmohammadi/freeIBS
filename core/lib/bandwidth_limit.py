import ras

def applyLimitOnUser(userObj,instance,limit_kbytes):
    if ras.isLanServer(userObj.rases[instance-1][0]):
	pppdApplyLimit("ppp"+str(userObj.rases[instance-1][1]),limit_kbytes)

def removeLimitOnUser(userObj,instance):
    if ras.isLanServer(userObj.rases[instance-1][0]):
	pppdRemoveLimit("ppp"+str(userObj.rases[instance-1][1]))

def pppdApplyLimit(interface,limit_kbytes):
    os.system("/sbin/tc qdisc add dev %s root tbf rate %skbps limit 20000 burst 1540"%(interface,limit_kbytes))

def pppdRemoveLimit(interface):
    os.system("/sbin/tc qdisc del dev %s root tbf"%interface)