def init():
    from core.ippool.ippool_loader import IPpoolLoader    
    global ippool_loader
    ippool_loader=IPpoolLoader()
    ippool_loader.loadAllIPpools()

    from core.ippool.ippool_actions import IPpoolActions
    global ippool_actions
    ippool_actions=IPpoolActions()
    

def getLoader():
    return ippool_loader

def getActionsManager():
    return ippool_actions
