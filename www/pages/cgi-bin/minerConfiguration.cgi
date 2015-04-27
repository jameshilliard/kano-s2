#!/bin/sh -e
#set -x

if [ ! -f /config/cgminer.conf ] ; then
 cp /etc/cgminer.conf.factory /config/cgminer.conf
fi

ant_result=`cat /config/cgminer.conf | sed -e "s/api-allow/apiallow/"`

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
<script>
EOH

echo "ant_data = ${ant_result};"

cat <<EOT
function f_get_miner_conf() {
	try
	{
		for(var i = 0; i < ant_data.pools.length; i++) {
			switch(i) {
			case 0:
				jQuery("#ant_pool1url").val(ant_data.pools[i].url);
				jQuery("#ant_pool1user").val(ant_data.pools[i].user);
				jQuery("#ant_pool1pw").val(ant_data.pools[i].pass);
				break;
			case 1:
				jQuery("#ant_pool2url").val(ant_data.pools[i].url);
				jQuery("#ant_pool2user").val(ant_data.pools[i].user);
				jQuery("#ant_pool2pw").val(ant_data.pools[i].pass);
				break;
			case 2:
				jQuery("#ant_pool3url").val(ant_data.pools[i].url);
				jQuery("#ant_pool3user").val(ant_data.pools[i].user);
				jQuery("#ant_pool3pw").val(ant_data.pools[i].pass);
				break;
			}
		}
		jQuery("#ant_apiallow").val(ant_data.apiallow);
		if(ant_data.bitmainbeeper) {
			document.getElementById("ant_beeper").checked = true;
		} else {
			document.getElementById("ant_beeper").checked = false;
		}
		if(ant_data.bitmaintempoverctrl) {
			document.getElementById("ant_tempoverctrl").checked = true;
		} else {
			document.getElementById("ant_tempoverctrl").checked = false;
		}
	}
	catch(err)
	{
		alert('Invalid Miner configuration file. Edit manually or reset to default.');
	}
}
function f_submit_miner_conf() {
	_ant_pool1url = jQuery("#ant_pool1url").val();
	_ant_pool1user = jQuery("#ant_pool1user").val();
	_ant_pool1pw = jQuery("#ant_pool1pw").val();
	_ant_pool2url = jQuery("#ant_pool2url").val();
	_ant_pool2user = jQuery("#ant_pool2user").val();
	_ant_pool2pw = jQuery("#ant_pool2pw").val();
	_ant_pool3url = jQuery("#ant_pool3url").val();
	_ant_pool3user = jQuery("#ant_pool3user").val();
	_ant_pool3pw = jQuery("#ant_pool3pw").val();
	_ant_apiallow = jQuery("#ant_apiallow").val();
	_ant_beeper = "true";
	_ant_tempoverctrl = "true";
	
	if(document.getElementById("ant_beeper").checked) {
		_ant_beeper = "true";
	} else {
		_ant_beeper = "false";
	}
	if(document.getElementById("ant_tempoverctrl").checked) {
		_ant_tempoverctrl = "true";
	} else {
		_ant_tempoverctrl = "false";
	}
	
	jQuery("#cbi_apply_cgminer_fieldset").show();
	
	jQuery.ajax({
		url: '/cgi-bin/set_miner_conf.cgi',
		type: 'POST',
		dataType: 'json',
		timeout: 30000,
		cache: false,
		data: {_ant_pool1url:_ant_pool1url, _ant_pool1user:_ant_pool1user, _ant_pool1pw:_ant_pool1pw,_ant_pool2url:_ant_pool2url, _ant_pool2user:_ant_pool2user, _ant_pool2pw:_ant_pool2pw,_ant_pool3url:_ant_pool3url, _ant_pool3user:_ant_pool3user, _ant_pool3pw:_ant_pool3pw, _ant_apiallow:_ant_apiallow, _ant_beeper:_ant_beeper, _ant_tempoverctrl:_ant_tempoverctrl},
		success: function(data) {
			window.location.reload();
		},
		error: function() {
			window.location.reload();
		}
	});
}

jQuery(document).ready(function() {
	f_get_miner_conf();
});
</script>
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
					<li class="tabmenu-item-system active"><a href="/cgi-bin/minerConfiguration.cgi">Miner Configuration</a></li>
					<li class="tabmenu-item-network"><a href="/cgi-bin/minerStatus.cgi">Miner Status</a></li>
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
			<h2 style="padding-bottom:10px;"><a id="content" name="content">Miner Configuration</a></h2>
			<div class="cbi-map" id="cbi-cgminer">
				<fieldset class="cbi-section" id="cbi_msg_cgminer_fieldset" style="display:none">
					<span id="cbi_msg_cgminer" style="color:red;"></span>
				</fieldset>
				<fieldset class="cbi-section" id="cbi_apply_cgminer_fieldset" style="display:none">
					<img src="/resources/icons/loading.gif" alt="Loading" style="vertical-align:middle" />
					<span id="cbi-apply-cgminer-status">Waiting for changes to be applied...</span>
				</fieldset>
				<fieldset class="cbi-section" id="cbi-cgminer-cgminer">
					<div class="cbi-section-descr"></div>
					<fieldset class="cbi-section" id="cbi-cgminer-default">
						<legend>Pool 1</legend>
						<div class="cbi-value" id="cbi-cgminer-default-pool1url">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool1url">URL</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool1url" id="ant_pool1url" value="" />
							</div>
						</div>
						<div class="cbi-value" id="cbi-cgminer-default-pool1user">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool1user">Worker</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool1user" id="ant_pool1user" value="" />
							</div>
						</div>
						<div class="cbi-value" id="cbi-cgminer-default-pool1pw">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool1pw">Password</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool1pw" id="ant_pool1pw" value="" />
							</div>
						</div>
					</fieldset>
					<fieldset class="cbi-section" id="cbi-cgminer-default">
						<legend>Pool 2</legend>
						<div class="cbi-value" id="cbi-cgminer-default-pool2url">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool2url">URL</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool2url" id="ant_pool2url" value="" />
							</div>
						</div>
						<div class="cbi-value" id="cbi-cgminer-default-pool2user">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool2user">Worker</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool2user" id="ant_pool2user" value="" />
							</div>
						</div>
						<div class="cbi-value" id="cbi-cgminer-default-pool2pw">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool2pw">Password</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool2pw" id="ant_pool2pw" value="" />
							</div>
						</div>
					</fieldset>
					<fieldset class="cbi-section" id="cbi-cgminer-default">
						<legend>Pool 3</legend>
						<div class="cbi-value" id="cbi-cgminer-default-pool3url">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool3url">URL</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool3url" id="ant_pool3url" value="" />
							</div>
						</div>
						<div class="cbi-value" id="cbi-cgminer-default-pool3user">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool3user">Worker</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool3user" id="ant_pool3user" value="" />
							</div>
						</div>
						<div class="cbi-value cbi-value-last"
							id="cbi-cgminer-default-pool3pw">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool3pw">Password</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool3pw" id="ant_pool3pw" value="" />
							</div>
						</div>
					</fieldset>
					<fieldset class="cbi-section" id="cbi-cgminer-default">
						<legend>Setup</legend>
						<div class="cbi-value cbi-value-last"
							id="cbi-cgminer-default-apiallow">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool3pw">API Allow</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.apiallow" id="ant_apiallow" value="" />
							</div>
						</div>
						<div class="cbi-value" id="cbi-cgminer-default-pool3url">
							<label class="cbi-value-title" for="keep">Beeper ringing</label>
							<div class="cbi-value-field">
								<input type="checkbox" name="ant_beeper" id="ant_beeper" checked />
							</div>
						</div>
						<div class="cbi-value" id="cbi-cgminer-default-pool3user">
							<label class="cbi-value-title" for="keep">Stop running when temprerature is over 80℃</label>
							<div class="cbi-value-field">
								<input type="checkbox" name="ant_tempoverctrl" id="ant_tempoverctrl" checked />
							</div>
						</div>
					</fieldset>
					<br />
				</fieldset>
				<br />
			</div>
			<div class="cbi-page-actions">
				<input class="cbi-button cbi-button-save right" type="button" onclick="f_submit_miner_conf();" value="Save&Apply" />
				<input class="cbi-button cbi-button-reset right" type="button" onclick="f_get_miner_conf();" value="Reset" />
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