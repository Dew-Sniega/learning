Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib2
>>> url = 'http://www.cuiqingcai.com/login'
>>> user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
>>> values = {'username' : 'cqc',  'password' : 'XXXX' }
>>> headers = { 'User-Agent' : user_agent }
>>> data = urllib.urlencode(values)
>>> request = urllib2.Request(url, headers ={ 'User-Agent' : user_agent })
>>> response = urllib2.urlopen(request)
>>> print response.read(2000)
<!DOCTYPE html>
	<!--[if IE 8]>
		<html xmlns="http://www.w3.org/1999/xhtml" class="ie8" lang="zh-CN">
	<![endif]-->
	<!--[if !(IE 8) ]><!-->
		<html xmlns="http://www.w3.org/1999/xhtml" lang="zh-CN">
	<!--<![endif]-->
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<title>静觅 &lsaquo; 登录</title>
	<link rel='dns-prefetch' href='//s.w.org' />
<link rel='stylesheet' href='http://cuiqingcai.com/wp-admin/load-styles.php?c=1&amp;dir=ltr&amp;load%5B%5D=dashicons,buttons,forms,l10n,login&amp;ver=4.7.3' type='text/css' media='all' />
<link rel="stylesheet" tyssspe="text/css" href="http://cuiqingcai.com/wp-content/themes/Yusi/login/icon.css" /><meta name='robots' content='noindex,follow' />
	<meta name="viewport" content="width=device-width" />
		</head>
	<body class="login login-action-login wp-core-ui  locale-zh-cn">
		<div id="login">
		<h1><a href="https://cn.wordpress.org/" title="基于WordPress" tabindex="-1">静觅</a></h1>
	
<form name="loginform" id="loginform" action="http://cuiqingcai.com/wp-login.php" method="post">
	<p>
		<label for="user_login">用户名或电子邮件地址<br />
		<input type="text" name="log" id="user_login" class="input" value="" size="20" /></label>
	</p>
	<p>
		<label for="user_pass">密码<br />
		<input type="password" name="pwd" id="user_pass" class="input" value="" size="20" /></label>
	</p>
		<p class="forgetmenot"><label for="rememberme"><input name="rememberme" type="checkbox" id="rememberme" value="forever"  /> 记住我的登录信息</label></p>
	<p class="submit">
		<input type="submit" name="wp-submit" id="wp-submit" class="button button-primary button-large" value="登录" />
		<input type="hidden" name="redirect_to" value="http://cuiqingcai.com/wp-admin/" />
		<input type="hidden" name="testcookie" value="1" />
	</p>
</form>

<p id="nav">
	<a href="http://cuiqingcai.com/wp-login.php?action=lostpassword">忘记密码？</a>
</p>

<script type="text/javascript">
function wp_attempt_focus
>>> 

