from core.plugins import plugin_loader
from core import defs
from core.server import handlers_manager

def init():
    from core.user import user_actions,user_plugin,attribute_manager

    global attr_manager
    attr_manager=attribute_manager.AttributeManager()
    
    global user_loader
    from core.user.user_loader import UserLoader
    user_loader=UserLoader()

    global user_pool
    from core.user.user_pool import UserPool
    user_pool=UserPool()
    
    global user_action_manager
    user_action_manager=user_actions.UserActions()

    global user_plugin_manager
    user_plugin_manager=user_plugin.UserPluginManager()

    plugin_loader.loadPlugins(defs.IBS_CORE+"/user/plugins")

    from core.user.user_handler import UserHandler
    handlers_manager.getManager().registerHandler(UserHandler())


def getActionManager():
    return user_action_manager

def getUserPluginManager():
    return user_plugin_manager

def getAttributeManager():
    return attr_manager

def getUserLoader():
    return user_loader

def getUserPool():
    return user_pool