#!/bin/sh
#set -x

if [ ! -f /config/cgminer.conf ] ; then
 cp /etc/cgminer.conf.factory /config/cgminer.conf
fi

cat /config/cgminer.conf
