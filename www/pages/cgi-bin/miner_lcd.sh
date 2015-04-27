#!/bin/sh

ant_ip=
ant_ghs=
ant_temp=
ant_blocks=
ant_poolurl=
ant_pooluser=

ant_tmp=`ifconfig | grep "inet addr"`
i=0
for ant_var in ${ant_tmp}
do
	case ${i} in
		1 )
		ant_ip=${ant_var}
		ant_ip=${ant_ip/addr:/}
		;;
	esac
	i=`expr $i + 1`
done

ant_tmp=`cgminer-api -o lcd | tr '|' ','`

if [ "${ant_tmp}" == "Socket connect failed: Connection refused" ]; then
	ant_ghs=0
	ant_temp=0
	ant_blocks=
	ant_poolurl=no
	ant_pooluser=no
else
	old="`echo "$ant_tmp" | grep 'GHS='`"
	if [ -z "$old" ] ; then
		ant_ghs=${ant_tmp#*GHS av=}
		ant_ghs=${ant_ghs%%,*}

		ant_temp=${ant_tmp#*Temperature=}
		ant_temp=${ant_temp%%,*}

		ant_blocks=${ant_tmp#*Found Blocks=}
		ant_blocks="B:${ant_blocks%%,*} "

		ant_poolurl=${ant_tmp#*Current Pool=}
		ant_poolurl=${ant_poolurl%%,*}

		ant_pooluser=${ant_tmp#*User=}
		ant_pooluser=${ant_pooluser%%,*}
	else
		ant_ghs=${ant_tmp#*GHS=}
		ant_ghs=${ant_ghs%%,*}

		ant_temp=${ant_tmp#*temp=}
		ant_temp=${ant_temp%%,*}

		ant_blocks=

		ant_poolurl=${ant_tmp#*pool=}
		ant_poolurl=${ant_poolurl%%,*}

		ant_pooluser=${ant_tmp#*user=}
		ant_pooluser=${ant_pooluser%%,*}
	fi
	ant_var=${ant_poolurl:0:7}
	if [ "${ant_var}" == "http://" ]; then
		ant_poolurl=${ant_poolurl:7}
	fi
fi

echo "IP:${ant_ip}"			> /tmp/lcd.data
echo "${ant_ghs}GH/s"			>> /tmp/lcd.data
echo "${ant_blocks}${ant_temp}C"	>> /tmp/lcd.data
echo "Pool:${ant_poolurl}"		>> /tmp/lcd.data
echo "User:${ant_pooluser}"		>> /tmp/lcd.data
