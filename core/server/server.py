from core.server import handlers_manager,xmlrpcserver
from core.threadpool import thread_main
from core import defs

def init():
    global server    
    handlers_manager.init()
    server=xmlrpcserver.XMLRPCServer((defs.IBS_SERVER_IP,defs.IBS_SERVER_PORT))
    
    
def startServer():
    thread_main.runThread(server.serve_forever,[],"server")
    