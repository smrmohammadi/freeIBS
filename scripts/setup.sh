#!/bin/bash

echo YOU MUST BE ROOT TO RUN THIS SCRIPT
echo


mkdir /var/log/ibs
chown apache /var/log/ibs
cp -f /usr/local/ibs/init.d/ibs /etc/init.d
chkconfig --add ibs
echo Enter system \(default admin\) password:
read pass
enc_pass=`/usr/local/ibs/sc/md5crypt.py $pass`
echo update admins set password=\'$enc_pass\' where username=\'system\'\; > /usr/local/ibs/db/myconf.sql
