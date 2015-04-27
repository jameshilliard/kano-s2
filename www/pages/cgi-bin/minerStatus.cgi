#!/bin/sh -e

# CGI output must start with at least empty line (or headers)
printf "Content-type: text/html\r\n\r\n"

cat <<-EOH
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
<meta http-equiv="cache-control" content="no-cache" />
<link rel="stylesheet" type="text/css" media="screen" href="/css/cascade.css" />
<!--[if IE 6]><link rel="stylesheet" type="text/css" media="screen" href="/css/ie6.css" /><![endif]-->
<!--[if IE 7]><link rel="stylesheet" type="text/css" media="screen" href="/css/ie7.css" /><![endif]-->
<!--[if IE 8]><link rel="stylesheet" type="text/css" media="screen" href="/css/ie8.css" /><![endif]-->
<script type="text/javascript" src="/js/xhr.js"></script>
<script type="text/javascript" src="/js/jquery-1.10.2.js"></script>
<script type="text/javascript" src="/js/json2.min.js"></script>
<title>Ant Miner/K</title>
</head>
<body class="lang_en">
	<p class="skiplink">
		<span id="skiplink1"><a href="#navigation">Skip to navigation</a></span>
		<span id="skiplink2"><a href="#content">Skip to content</a></span>
	</p>
	<div id="menubar">
		<h2 class="navigation"><a id="navigation" name="navigation">Navigation</a></h2>
		<div class="clear"></div>
	</div>
	<div id="menubar" style="background-color: #0a2b40;">
		<div class="hostinfo" style="float: left; with: 500px;">
			<img src="/images/antminer_logo.png" width="92" height="50" alt="" title="" border="0" />
		</div>
		<div class="clear"></div>
	</div>
	<div id="maincontainer">
		<div id="tabmenu">
			<div class="tabmenu1">
				<ul class="tabmenu l1">
					<li class="tabmenu-item-status"><a href="/index.html">System</a></li>
					<li class="tabmenu-item-system"><a href="/cgi-bin/minerConfiguration.cgi">Miner Configuration</a></li>
					<li class="tabmenu-item-network active"><a href="/cgi-bin/minerStatus.cgi">Miner Status</a></li>
					<li class="tabmenu-item-system"><a href="/network.html">Network</a></li>
				</ul>
				<br style="clear: both" />
			</div>
		</div>
		<div id="maincontent">
			<noscript>
				<div class="errorbox">
					<strong>Java Script required!</strong><br /> You must enable Java Script in your browser or LuCI will not work properly.
				</div>
			</noscript>
			<h2 style="padding-bottom:10px;"><a id="content" name="content">Miner Status</a></h2>
			<div class="cbi-map" id="cbi-cgminerstatus">
				<!-- tblsection -->
				<fieldset class="cbi-section" id="cbi-table-table">
					<legend>Summary</legend>
					<div class="cbi-section-descr"></div>
					<div class="cbi-section-node">
						<table class="cbi-section-table">
							<tr class="cbi-section-table-titles">
								<th class="cbi-section-table-cell">Elapsed</th>
								<th class="cbi-section-table-cell">GH/S(5s)</th>
								<th class="cbi-section-table-cell">GH/S(5m)</th>
								<th class="cbi-section-table-cell">GH/S(avg)</th>
								<th class="cbi-section-table-cell">FoundBlocks</th>
								<th class="cbi-section-table-cell">Getworks</th>
								<th class="cbi-section-table-cell">Accepted</th>
								<th class="cbi-section-table-cell">Rejected</th>
								<th class="cbi-section-table-cell">HW</th>
								<th class="cbi-section-table-cell">Utility</th>
								<th class="cbi-section-table-cell">Discarded</th>
								<th class="cbi-section-table-cell">Stale</th>
								<th class="cbi-section-table-cell">LocalWork</th>
								<th class="cbi-section-table-cell">WU</th>
								<th class="cbi-section-table-cell">DiffA</th>
								<th class="cbi-section-table-cell">DiffR</th>
								<th class="cbi-section-table-cell">DiffS</th>
								<th class="cbi-section-table-cell">BestShare</th>
							</tr>
							<tr class="cbi-section-table-descr">
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
							</tr>
EOH

# Read miner status
ant_elapsed=
ant_ghs5s=
ant_ghs5m=
ant_ghsav=
ant_foundblocks=
ant_getworks=
ant_accepted=
ant_rejected=
ant_hw=
ant_utility=
ant_discarded=
ant_stale=
ant_localwork=
ant_wu=
ant_diffa=
ant_diffr=
ant_bestshare=

ant_tmp=`cgminer-api -o`
if [ "${ant_tmp}" == "Socket connect failed: Connection refused" ]; then
	ant_elapsed=0
	ant_ghs5s=0
	ant_ghs5m=0
	ant_ghsav=0
	ant_foundblocks=0
	ant_getworks=0
	ant_accepted=0
	ant_rejected=0
	ant_hw=0
	ant_utility=0
	ant_discarded=0
	ant_stale=0
	ant_localwork=0
	ant_wu=0
	ant_diffa=0
	ant_diffr=0
	ant_bestshare=0
else
	ant_elapsed=${ant_tmp#*Elapsed=}
	ant_elapsed=${ant_elapsed%%,*}

	has_mhs="`echo "$ant_tmp" | grep 'MHS 5s'`"
	if [ "$has_mhs" ] ; then
		ant_mhs5s=${ant_tmp#*MHS 5s=}
		ant_mhs5s=${ant_mhs5s%%,*}
		ant_mhs5s=${ant_mhs5s%%.*}
		ant_ghs5s=$((${ant_mhs5s}/1000))

		if [ "$ant_elapsed" -lt "300" ] ; then
			ant_ghs5m=
		else
			ant_mhs5m=${ant_tmp#*MHS 5m=}
			ant_mhs5m=${ant_mhs5m%%,*}
			ant_mhs5m=${ant_mhs5m%%.*}
			ant_ghs5m=$((${ant_mhs5m}/1000))
		fi

		ant_mhsav=${ant_tmp#*MHS av=}
		ant_mhsav=${ant_mhsav%%,*}
		ant_mhsav=${ant_mhsav%%.*}
		ant_ghsav=$((${ant_mhsav}/1000))
	else
		ant_ghs5s=${ant_tmp#*GHS 5s=}
		ant_ghs5s=${ant_ghs5s%%,*}

		ant_ghsav=${ant_tmp#*GHS av=}
		ant_ghsav=${ant_ghsav%%,*}
	fi

	ant_foundblocks=${ant_tmp#*Found Blocks=}
	ant_foundblocks=${ant_foundblocks%%,*}

	ant_getworks=${ant_tmp#*Getworks=}
	ant_getworks=${ant_getworks%%,*}

	ant_accepted=${ant_tmp#*Accepted=}
	ant_accepted=${ant_accepted%%,*}

	ant_rejected=${ant_tmp#*Rejected=}
	ant_rejected=${ant_rejected%%,*}

	ant_hw=${ant_tmp#*Hardware Errors=}
	ant_hw=${ant_hw%%,*}

	ant_utility=${ant_tmp#*Utility=}
	ant_utility=${ant_utility%%,*}

	ant_discarded=${ant_tmp#*Discarded=}
	ant_discarded=${ant_discarded%%,*}

	ant_stale=${ant_tmp#*Stale=}
	ant_stale=${ant_stale%%,*}

	ant_localwork=${ant_tmp#*Local Work=}
	ant_localwork=${ant_localwork%%,*}

	ant_wu=${ant_tmp#*Work Utility=}
	ant_wu=${ant_wu%%,*}

	ant_diffa=${ant_tmp#*Difficulty Accepted=}
	ant_diffa=${ant_diffa%%,*}
	ant_diffa=${ant_diffa%%.*}

	ant_diffr=${ant_tmp#*Difficulty Rejected=}
	ant_diffr=${ant_diffr%%,*}
	ant_diffr=${ant_diffr%%.*}

	ant_diffs=${ant_tmp#*Difficulty Stale=}
	ant_diffs=${ant_diffs%%,*}
	ant_diffs=${ant_diffs%%.*}

	ant_bestshare=${ant_tmp#*Best Share=}
	ant_bestshare="`echo "${ant_bestshare%%,*}"|sed -r ':L;s=\b([0-9]+)([0-9]{3})\b=\1,\2=g;t L'`"
fi

if [ "${ant_elapsed}" = "" ]; then
	ant_elapsed=0
fi

ant_days=$((${ant_elapsed}/86400))
ant_hours=$((${ant_elapsed}/3600-${ant_days}*24))
ant_minutes=$((${ant_elapsed}/60-${ant_days}*1440-${ant_hours}*60))
ant_seconds=$((${ant_elapsed}-${ant_days}*86400-${ant_hours}*3600-${ant_minutes}*60))

ant_elapsed=
if [ ${ant_days} -gt 0 ]; then
ant_elapsed=${ant_elapsed}${ant_days}d
fi
if [ ${ant_hours} -gt 0 ]; then
ant_elapsed=${ant_elapsed}${ant_hours}h
fi
if [ ${ant_minutes} -gt 0 ]; then
ant_elapsed=${ant_elapsed}${ant_minutes}m
fi
if [ ${ant_seconds} -gt 0 ]; then
ant_elapsed=${ant_elapsed}${ant_seconds}s
fi

echo "<tr class=\"cbi-section-table-row cbi-rowstyle-1\" id=\"cbi-table-1\">"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_elapsed\">${ant_elapsed}</div>"
echo "<div id=\"cbip-table-1-elapsed\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_ghs5s\">${ant_ghs5s}</div>"
echo "<div id=\"cbip-table-1-ghs5s\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_ghs5m\">${ant_ghs5m}</div>"
echo "<div id=\"cbip-table-1-ghs5m\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_ghsav\">${ant_ghsav}</div>"
echo "<div id=\"cbip-table-1-ghsav\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_foundblocks\">${ant_foundblocks}</div>"
echo "<div id=\"cbip-table-1-foundblocks\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_getworks\">${ant_getworks}</div>"
echo "<div id=\"cbip-table-1-getworks\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_accepted\">${ant_accepted}</div>"
echo "<div id=\"cbip-table-1-accepted\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_rejected\">${ant_rejected}</div>"
echo "<div id=\"cbip-table-1-rejected\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_hw\">${ant_hw}</div>"
echo "<div id=\"cbip-table-1-hw\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_utility\">${ant_utility}</div>"
echo "<div id=\"cbip-table-1-utility\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_discarded\">${ant_discarded}</div>"
echo "<div id=\"cbip-table-1-discarded\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_stale\">${ant_stale}</div>"
echo "<div id=\"cbip-table-1-stale\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_localwork\">${ant_localwork}</div>"
echo "<div id=\"cbip-table-1-localwork\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_wu\">${ant_wu}</div>"
echo "<div id=\"cbip-table-1-wu\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_diffa\">${ant_diffa}</div>"
echo "<div id=\"cbip-table-1-diffaccepted\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_diffr\">${ant_diffr}</div>"
echo "<div id=\"cbip-table-1-diffrejected\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_diffs\">${ant_diffs}</div>"
echo "<div id=\"cbip-table-1-diffstale\"></div>"
echo "</td>"
echo "<td class=\"cbi-value-field\">"
echo "<div id=\"ant_bestshare\">${ant_bestshare}</div>"
echo "<div id=\"cbip-table-1-bestshare\"></div>"
echo "</td>"
echo "</tr>"

cat <<-EOP
						</table>
					</div>
				</fieldset>
				<!-- /tblsection -->
				<!-- tblsection -->
				<fieldset class="cbi-section" id="cbi-table-table">
					<legend>Pools</legend>
					<div class="cbi-section-descr"></div>
					<div class="cbi-section-node">
						<table id="ant_pools" class="cbi-section-table">
							<tr class="cbi-section-table-titles">
								<th class="cbi-section-table-cell">Pool</th>
								<th class="cbi-section-table-cell">URL</th>
								<th class="cbi-section-table-cell">User</th>
								<th class="cbi-section-table-cell">Status</th>
								<th class="cbi-section-table-cell">Priority</th>
								<th class="cbi-section-table-cell">GetWorks</th>
								<th class="cbi-section-table-cell">Accepted</th>
								<th class="cbi-section-table-cell">Rejected</th>
								<th class="cbi-section-table-cell">Discarded</th>
								<th class="cbi-section-table-cell">Stale</th>
								<th class="cbi-section-table-cell">Diff</th>
								<th class="cbi-section-table-cell">Diff1#</th>
								<th class="cbi-section-table-cell">DiffA#</th>
								<th class="cbi-section-table-cell">DiffR#</th>
								<th class="cbi-section-table-cell">DiffS#</th>
								<th class="cbi-section-table-cell">LSDiff</th>
								<th class="cbi-section-table-cell">LSTime</th>
							</tr>
							<tr class="cbi-section-table-descr">
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
							</tr>
EOP

ant_tmp=`cgminer-api -o pools`
if [ "${ant_tmp}" != "Socket connect failed: Connection refused" ]; then
	ant_last_len=0
	ant_len=0
	ant_when=${ant_tmp#*When=}
	ant_when=${ant_when%%,*}
	while :;
	do
		ant_tmp=${ant_tmp#*POOL=}
		ant_len=${#ant_tmp}

		if [ ${ant_len} -eq ${ant_last_len} ]; then
			break
		fi
		ant_last_len=${ant_len}

		echo "<tr class=\"cbi-section-table-row cbi-rowstyle-1\" id=\"cbi-table-1\">"

		ant_pool_index=
		ant_pool_url=
		ant_pool_user=
		ant_pool_status=
		ant_pool_priority=
		ant_pool_getworks=
		ant_pool_accepted=
		ant_pool_rejected=
		ant_pool_discarded=
		ant_pool_stale=
		ant_pool_diff=
		ant_pool_diff1=
		ant_pool_diffa=
		ant_pool_diffr=
		ant_pool_diffs=
		ant_pool_lsdiff=
		ant_pool_lstime=

		ant_pool_index=${ant_tmp%%,*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-pool\">${ant_pool_index}</div>"
		echo "<div id=\"cbip-table-1-pool\"></div>"
		echo "</td>"

		ant_pool_url=${ant_tmp#*URL=}
		ant_pool_url=${ant_pool_url%%,*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-url\">${ant_pool_url}</div>"
		echo "<div id=\"cbip-table-1-url\"></div>"
		echo "</td>"

		ant_pool_user=${ant_tmp#*User=}
		ant_pool_user=${ant_pool_user%%,Last Share Time=*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-user\">${ant_pool_user}</div>"
		echo "<div id=\"cbip-table-1-user\"></div>"
		echo "</td>"

		ant_pool_status=${ant_tmp#*Status=}
		ant_pool_status=${ant_pool_status%%,*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-status\">${ant_pool_status}</div>"
		echo "<div id=\"cbip-table-1-status\"></div>"
		echo "</td>"

		ant_pool_priority=${ant_tmp#*Priority=}
		ant_pool_priority=${ant_pool_priority%%,*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-priority\">${ant_pool_priority}</div>"
		echo "<div id=\"cbip-table-1-priority\"></div>"
		echo "</td>"

		ant_pool_getworks=${ant_tmp#*Getworks=}
		ant_pool_getworks=${ant_pool_getworks%%,*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-getworks\">${ant_pool_getworks}</div>"
		echo "<div id=\"cbip-table-1-getworks\"></div>"
		echo "</td>"

		ant_pool_accepted=${ant_tmp#*Accepted=}
		ant_pool_accepted=${ant_pool_accepted%%,*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-accepted\">${ant_pool_accepted}</div>"
		echo "<div id=\"cbip-table-1-accepted\"></div>"
		echo "</td>"

		ant_pool_rejected=${ant_tmp#*Rejected=}
		ant_pool_rejected=${ant_pool_rejected%%,*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-rejected\">${ant_pool_rejected}</div>"
		echo "<div id=\"cbip-table-1-rejected\"></div>"
		echo "</td>"

		ant_pool_discarded=${ant_tmp#*Discarded=}
		ant_pool_discarded=${ant_pool_discarded%%,*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-discarded\">${ant_pool_discarded}</div>"
		echo "<div id=\"cbip-table-1-discarded\"></div>"
		echo "</td>"

		ant_pool_stale=${ant_tmp#*Stale=}
		ant_pool_stale=${ant_pool_stale%%,*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-stale\">${ant_pool_stale}</div>"
		echo "<div id=\"cbip-table-1-stale\"></div>"
		echo "</td>"

		has_diff="`echo "$ant_tmp" | grep ',Diff='`"
		if [ "$has_diff" ] ; then
			ant_pool_diff=${ant_tmp#*Diff=}
			ant_pool_diff=${ant_pool_diff%%,*}
		fi
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-diff\">${ant_pool_diff}</div>"
		echo "<div id=\"cbip-table-1-diff\"></div>"
		echo "</td>"

		ant_pool_diff1=${ant_tmp#*Diff1 Shares=}
		ant_pool_diff1=${ant_pool_diff1%%,*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-diff1shares\">${ant_pool_diff1}</div>"
		echo "<div id=\"cbip-table-1-diff1shares\"></div>"
		echo "</td>"

		ant_pool_diffa=${ant_tmp#*Difficulty Accepted=}
		ant_pool_diffa=${ant_pool_diffa%%,*}
		ant_pool_diffa=${ant_pool_diffa%%.*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-diffaccepted\">${ant_pool_diffa}</div>"
		echo "<div id=\"cbip-table-1-diffaccepted\"></div>"
		echo "</td>"

		ant_pool_diffr=${ant_tmp#*Difficulty Rejected=}
		ant_pool_diffr=${ant_pool_diffr%%,*}
		ant_pool_diffr=${ant_pool_diffr%%.*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-diffrejected\">${ant_pool_diffr}</div>"
		echo "<div id=\"cbip-table-1-diffrejected\"></div>"
		echo "</td>"

		ant_pool_diffs=${ant_tmp#*Difficulty Stale=}
		ant_pool_diffs=${ant_pool_diffs%%,*}
		ant_pool_diffs=${ant_pool_diffs%%.*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-diffstale\">${ant_pool_diffs}</div>"
		echo "<div id=\"cbip-table-1-diffstale\"></div>"
		echo "</td>"

		ant_pool_lsdiff=${ant_tmp#*Last Share Difficulty=}
		ant_pool_lsdiff=${ant_pool_lsdiff%%,*}
		ant_pool_lsdiff=${ant_pool_lsdiff%%.*}
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-lastsharedifficulty\">${ant_pool_lsdiff}</div>"
		echo "<div id=\"cbip-table-1-lastsharedifficulty\"></div>"
		echo "</td>"

		ant_pool_lstime=${ant_tmp#*Last Share Time=}
		ant_pool_lstime=${ant_pool_lstime%%,*}
		has_colon="`echo "$ant_pool_lstime=" | grep ':'`"
		if [ -z "$has_colon" ] ; then
			ant_pool_lstime=$((${ant_when}-${ant_pool_lstime}))
			if [ "$ant_pool_lstime" -ge "10000" ] ; then
				if [ "$ant_pool_diffa" -eq "0" ] ; then
					ant_pool_lstime="Never"
				else
					ant_pool_lstime="Long ago"
				fi
			else
				ant_pool_lstime=${ant_pool_lstime}s
			fi
		fi

		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-lastsharetime\">${ant_pool_lstime}</div>"
		echo "<div id=\"cbip-table-1-lastsharetime\"></div>"
		echo "</td>"
	done
fi

cat <<-EOD
						</table>
					</div>
				</fieldset>
				<!-- /tblsection -->
				<!-- tblsection -->
				<fieldset class="cbi-section" id="cbi-table-table">
					<legend>AntMiner</legend>
					<div class="cbi-section-descr"></div>
					<div class="cbi-section-node">
						<table id="ant_devs" class="cbi-section-table">
							<tr class="cbi-section-table-titles">
								<th class="cbi-section-table-cell">Chain#</th>
								<th class="cbi-section-table-cell">ASIC#</th>
								<th class="cbi-section-table-cell">Frequency</th>
								<th class="cbi-section-table-cell">Temp</th>
								<th class="cbi-section-table-cell">ASIC status</th>
								<th class="cbi-section-table-cell">ASIC info</th>
							</tr>
							<tr class="cbi-section-table-descr">
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
								<th class="cbi-section-table-cell"></th>
							</tr>
EOD

ant_fan1=0
ant_fan2=0
ant_fan3=0
ant_fan4=0

ant_tmp=`cgminer-api -o stats`
if [ "${ant_tmp}" != "Socket connect failed: Connection refused" ]; then

	ant_chain_acn=
	ant_freq=
	ant_fan=
	ant_temp=
	ant_chain_acs=

	ant_freq=${ant_tmp#*frequency=}
	ant_freq=${ant_freq%%,voltage=*}

	tot_lines=0
	tot_temp=0
	for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ; do
		ant_chain_acn=${ant_tmp#*chain_acn$i=}
		ant_chain_acn=${ant_chain_acn%%,*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			tot_lines=$(($tot_lines+1))
			ant_temp=${ant_tmp#*temp$i=}
			ant_temp=${ant_temp%%,*}
			tot_temp=$(($tot_temp+$ant_temp))
		fi
	done
	av_temp=$(($tot_temp/$tot_lines))

	total_o=0
	for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ; do

		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=

		ant_chain_acn=${ant_tmp#*chain_acn$i=}
		ant_chain_acn=${ant_chain_acn%%,*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			ant_fan=${ant_tmp#*fan$i=}
			ant_fan=${ant_fan%%,*}
			case $i in
				1) ant_fan1=${ant_fan} ;;
				2) ant_fan2=${ant_fan} ;;
				3) ant_fan3=${ant_fan} ;;
				4) ant_fan4=${ant_fan} ;;
			esac

			ant_temp=${ant_tmp#*temp$i=}
			ant_temp=${ant_temp%%,*}
			tdiff=$(($ant_temp-$av_temp))
			if [ "$tdiff" -gt "10" -o "$tdiff" -lt "-10" ] ; then
				ant_temp="<font color=red><b>$ant_temp</b></font>"
			elif [ "$tdiff" -gt "5" -o "$tdiff" -lt "-5" ] ; then
				ant_temp="<font color=#e83><b>$ant_temp</b></font>"
			fi

			ant_chain_acs=${ant_tmp#*chain_acs$i=}
			ant_chain_acs=${ant_chain_acs%%,*}
			ant_os="`echo "$ant_chain_acs"|tr -c -d o |wc -c`"
			total_o=$(($total_o+$ant_os))
			ant_xms="`echo "$ant_chain_acs"|tr -c -d x- |wc -c`"
			if [ "$ant_os" != "64" ] ; then
				per0=$(($ant_os*10000/64))
				per="`echo "$per0" | sed -e "s/\(..\)$/.\1/"`"
				ant_acs_per="<font color=red>$per% good</font>"
				ant_acs_info="<font color=red>$ant_os/$ant_xms&nbsp;&nbsp;$per%</font>"
			else
				ant_acs_info="$ant_os/$ant_xms&nbsp;&nbsp;100%"
			fi
			ant_chain_acs="`echo "$ant_chain_acs"|sed -e "s|\([x-][x -]*\)|<font color=red>\1</font>|g"`"

			echo "<tr class=\"cbi-section-table-row cbi-rowstyle-1\" id=\"cbi-table-1\">"
			echo "<td class=\"cbi-value-field\">"
			echo "<div id=\"cbi-table-1-chain\">${i}</div>"
			echo "<div id=\"cbip-table-1-chain\"></div>"
			echo "</td>"
			echo "<td class=\"cbi-value-field\">"
			echo "<div id=\"cbi-table-1-asic\">${ant_chain_acn}</div>"
			echo "<div id=\"cbip-table-1-asic\"></div>"
			echo "</td>"
			echo "<td class=\"cbi-value-field\">"
			echo "<div id=\"cbi-table-1-frequency\">${ant_freq}</div>"
			echo "<div id=\"cbip-table-1-frequency\"></div>"
			echo "</td>"
			echo "<td class=\"cbi-value-field\">"
			echo "<div id=\"cbi-table-1-temp\">${ant_temp}</div>"
			echo "<div id=\"cbip-table-1-temp\"></div>"
			echo "</td>"
			echo "<td class=\"cbi-value-field\">"
			echo "<div id=\"cbi-table-1-status\">${ant_chain_acs}</div>"
			echo "<div id=\"cbip-table-1-status\"></div>"
			echo "</td>"
			echo "<td class=\"cbi-value-field\">"
			echo "<div id=\"cbi-table-1-info\">${ant_acs_info}</div>"
			echo "<div id=\"cbip-table-1-info\"></div>"
			echo "</td>"
			echo "</tr>"
		fi

	done
	if [ "$total_o" != "0" ] ; then
		exp=$(($total_o*1000/640))
		echo "</table>";
		echo '<table id="expected" class="cbi-section-table">';
		echo "<tr class=\"cbi-section-table-row cbi-rowstyle-1\" id=\"cbi-table-1\">"
		echo "<td class=\"cbi-value-field\" nowrap>"
		echo "<div id=\"cbi-table-1-chain\"><font color=blue>&nbsp;Chip count ($total_o) hash rate should be:&nbsp;</font></div>"
		echo "<div id=\"cbip-table-1-chain\"></div>"
		echo "</td>"
		echo "<td class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-asic\"><font color=blue>&nbsp;${exp}GH/S(5m)&nbsp;</font></div>"
		echo "<div id=\"cbip-table-1-asic\"></div>"
		echo "</td>"
		echo "<td width=100% class=\"cbi-value-field\">"
		echo "<div id=\"cbi-table-1-asic\">&nbsp;</div>"
		echo "<div id=\"cbip-table-1-asic\"></div>"
		echo "</td></tr>"
	fi
fi

cat <<-EOF
						</table>
					</div>
					<div class="cbi-section-node" style="margin-top:8px;">
						<table id="ant_fans" class="cbi-section-table">
							<tr class="cbi-section-table-titles">
								<th class="cbi-section-table-cell" style="width:10%;">Fan#</th>
								<th class="cbi-section-table-cell">Fan1</th>
								<th class="cbi-section-table-cell">Fan2</th>
								<th class="cbi-section-table-cell">Fan3</th>
								<th class="cbi-section-table-cell">Fan4</th>
							</tr>
							<tr class="cbi-section-table-row">
								<th class="cbi-rowstyle-1 cbi-value-field">Speed (r/min)</th>
EOF

echo "<td id=\"ant_fan1\" class=\"cbi-rowstyle-1 cbi-value-field\">${ant_fan1}</td>"
echo "<td id=\"ant_fan2\" class=\"cbi-rowstyle-1 cbi-value-field\">${ant_fan2}</td>"
echo "<td id=\"ant_fan3\" class=\"cbi-rowstyle-1 cbi-value-field\">${ant_fan3}</td>"
echo "<td id=\"ant_fan4\" class=\"cbi-rowstyle-1 cbi-value-field\">${ant_fan4}</td>"

cat <<-EOT
							</tr>
						</table>
					</div>
				</fieldset>
				<!-- /tblsection -->
				<br />
			</div>
			<div class="clear"></div>
		</div>
	</div>
	<div class="clear"></div>
	<div style="text-align: center; bottom: 0; left: 0; height: 1.5em; font-size: 80%; margin: 0; padding: 5px 0px 2px 8px; background-color: #918ca0; width: 100%;">
		<font style="color:#fff;">Copyright &copy; 2013-2014, Bitmain Technologies</font>
	</div>
</body>
</html>
EOT
