#some kind of configuration file :p
from core.defs_lib.defs_loader import DefsLoader

DEBUG_THREADS=4 #dangerous
DEBUG_ALL=3
DEBUG_WARNINGS=2
DEBUG_ERRORS=1
DEBUG_NOTHING=0

DEBUG_LEVEL=3 #debug level

LOG_RADIUS_REQUESTS=1 #LOG radius requests in /var/log/IBSng/ibs_radius.log
LOG_SERVER_REQUESTS=1 #LOG server requests in /var/log/IBSng/ibs_server.log, Normally not useful
LOG_DATABASE_QUERIES=1 #LOG every query we send to database

IBS_ROOT="/usr/local/IBSng"
IBS_CORE="%s/core"%IBS_ROOT
IBS_ADDONS="%s/addons/"%IBS_ROOT

#######  DATABASE
DB_POOL_DEFAULT_CONNECTIONS=3
DB_POOL_MAX_CONNECTIONS=30
DB_POOL_MAX_RELEASE_TIME=60
DB_POOL_CHECK_INTERVAL=60 #seconds
DB_PASSWORD="ibsdbpass"

#######  THREAD POOL
THREAD_POOL_DEFAULT_SIZE=7
MAX_SERVER_THREADS=3
MAX_EVENT_THREADS=4
MAX_OTHER_THREADS=3
MAX_RADIUS_THREADS=5
THREAD_POOL_MAX_SIZE=150
THREAD_POOL_MAX_RELEASE_TIME=600

MAXLONG=0x7fffffff

def init():
    global defs_loader
    defs_loader=DefsLoader()
    defs_loader.setGlobalsDic(globals())   
    defs_loader.loadAll()
    
def getDefsLoader():
    return defs_loader

def getDBHandle():
    from core.db import db_pg
    return db_pg.db_pg("IBSng",None,5432,"ibs",DB_PASSWORD)
