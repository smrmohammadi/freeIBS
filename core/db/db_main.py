from core.db import dbpool

class DBHandleQuery:
    def __getattr__(self,name):
	handle=dbpool.getPool().getHandle()
	try:
	    return getattr(handle,name)
	finally:
	    dbpool.getPool().release(handle)
	    

def init():
    dbpool.initPool()
    global handle_query
    handle_query=DBHandleQuery()

    from core.event import daily_events
    daily_events.addLowLoadJob(vacuumDB,[])

def getHandle():
    return handle_query

def vacuumDB():
    getHandle().query("vacuum analyze")