#! /usr/bin/python -O
import sys
sys.path.append("/usr/local/ibs")
import core.ibs_crypt
if len(sys.argv)!=2:
    print "md5crypt.py <password>\n";
    sys.exit(1)

print ibs_crypt.md5Crypt(sys.argv[1])
