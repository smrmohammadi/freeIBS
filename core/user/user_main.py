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

    global credit_change_log_actions
    from core.user.credit_change_log import CreditChangeLogActions
    credit_change_log_actions=CreditChangeLogActions()

    global add_user_save_actions
    from core.user.add_user_save import AddUserSaveActions
    add_user_save_actions=AddUserSaveActions()

    global ras_msg_dispatcher
    from core.user.ras_msg_dispatcher import RasMsgDispatcher
    ras_msg_dispatcher=RasMsgDispatcher()
    
    global online
    from core.user.online import OnlineUsers
    online=OnlineUsers()
    
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

def getCreditChangeLogActions():
    return credit_change_log_actions

def getAddUserSaveActions():
    return add_user_save_actions

def getRasMsgDispatcher():
    return ras_msg_dispatcher

def getOnline():
    return online