#### Default definition file
#### Run defs2sql.py [-i,-u] defs.defaults.py to create a sql script file from this file
#### -i option tells defs_sc.py to use insert queries (When you install IBS) 
#### -u tells defs.sc_py to use update queries (When updating defs table)

#### WARNING: all of variables should be defined in python syntax

#######  SERVER IP/PORT
IBS_SERVER_PORT=1235
IBS_SERVER_IP="127.0.0.1"

###### RADIUS SERVER
RADIUS_SERVER_ENABLED=1 #ENABLE RADIUS SERVER?
RADIUS_SERVER_BIND_IP=["0.0.0.0"]
RADIUS_SERVER_AUTH_PORT=1812
RADIUS_SERVER_ACCT_PORT=1813

ENCRYPT_PASSWORDS=0

MAX_USER_POOL_SIZE=10000

BW_TC_COMMAND="tc"
BW_IPTABLES_COMMAND="iptables"