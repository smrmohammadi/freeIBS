#! /usr/bin/python -O
#Check if IBS and postgresql running and restart them if it's necassary
#This shouldn't happen, but it's better to be on safe side
#
#

import os
import time
import sys
sys.path.append("/usr/local/ibs")
from core.ibs_exceptions import *
from core.ibs_client import SendCommand
import signal

def main():
    global logger
    logger=Logger("/var/log/ibs/ibs_check.log")
    signal.signal(signal.SIGHUP,signal.SIG_IGN)
    time.sleep(15*60)
    while(1):
	time.sleep(10*60)
	checkIBS()
	checkPostgresql()
#	checkRadius()


def checkIBS():
    ret=pidof("ibs.py")
    if len(ret)==0:
	logger.write("ibs.py process not found")
	restartIBS()
    else:
	try:
	    ret=pingIBS()
	    if ret==0:
		logger.write("ibs ping failed!")
		restartIBS()
	except:
	    restartIBS()

def checkPostgresql():
    ret=pidof("postmaster")
    if len(ret)==0:
	restartPostgresql()
	restartIBS()


def checkRadius():
    ret=pidof("radiusd")
    if len(ret)==0:
	restartRadius()

def restartIBS():
    logger.write("restarting ibs...")
    os.system("killall ibs.py")
    time.sleep(20)
    os.system("killall -9 ibs.py")
    os.system("service ibs startibs")    
    time.sleep(10)

def restartPostgresql():
    logger.write("restarting postgresql...")
    os.system("service postgresql stop")
    try:
	os.remove("/var/lib/pgsql/data/postmaster.pid")
    except:
	pass
    os.system("service postgresql start")

def restartRadius():
    logger.write("restarting radius...")
    os.system("service radius restart")


def pidof(process_name):
    fd=os.popen("ps -C %s |grep %s"%(process_name,process_name))
    lines=fd.readlines()
    fd.close()
    return map(lambda t:t.strip(),lines)
    
def pingIBS():
    def handler(signum, frame):
        logger.write("IBS Ping failed")
	raise IOError, "Couldn't recive from IBS server"
	    
    # Set the signal handler and a 5-second alarm
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(15)

    try:
	sock=SendCommand()
	sock.send("ping()\r\n")
	line=sock.recv()
	signal.alarm(0) 	             # Disable the alarm
	return 1
    except:
	signal.alarm(0) 	             # Disable the alarm
	return 0
    

pid=os.fork()
if pid==0:
    main()
    
