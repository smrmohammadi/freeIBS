from core.user import user_main
onlines=user_main.getOnline().getUserOnlines()
for user_id in onlines:
    print "%s\t%s\t%s"%(user_id,onlines[user_id].calcCurrentCredit(),onlines[user_id].getTypeObj().getInOutBytes(1))
