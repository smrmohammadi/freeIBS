from core.user import user_main
user_pool=user_main.getUserPool()
print "Hits: %s Misses: %s Total: %s"%(user_pool.hits,user_pool.misses,user_pool.hits+user_pool.misses)
print "POOL LEN: %s POOL: %s"%(user_pool._UserPool__pool_len,user_pool._UserPool__pool_by_id)