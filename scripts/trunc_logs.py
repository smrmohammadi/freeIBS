#!/usr/bin/python

import os

log_path='/var/log/ibs/'
MAX_LOG_SIZE = 10 * 1024 * 1024
files=os.listdir(log_path)
for i in files:
    if i.startswith('thread_debug'):
	try:
	    size = os.stat(log_path+i)[6]
	    if size > MAX_LOG_SIZE:
		os.remove(log_path+i)
	except:
#	    raise
	    continue