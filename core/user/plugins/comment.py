"""
    comment Plugin: just to know informations ;)
"""
from core.user import user_plugin,user_main,attribute
from core.user.attr_updater import AttrUpdater
from core.user.attr_searcher import AttrSearcher
from core.ibs_exceptions import *
from core.errors import errorText
from core.lib.general import *

def init():
    user_main.getAttributeManager().registerHandler(CommentAttrHandler(),["comment"],["comment"],[])

	
class CommentAttrUpdater(AttrUpdater):
    def __init__(self):
	AttrUpdater.__init__(self,"comment")

    def changeInit(self,comment):
	self.useGenerateQuery({"comment":comment})

    def deleteInit(self):
	self.useGenerateQuery(["comment"])

class CommentAttrSearcher(AttrSearcher):
    def run(self):
	search_helper=self.getSearchHelper()
	user_attrs=search_helper.getTable("user_attrs")
	user_attrs.likeStrSearch(search_helper,"comment","comment_op","comment")


class CommentAttrHandler(attribute.AttributeHandler):
    def __init__(self):
	attribute.AttributeHandler.__init__(self,"comment")
	self.registerAttrUpdaterClass(CommentAttrUpdater,["comment"])
	self.registerAttrSearcherClass(CommentAttrSearcher)

