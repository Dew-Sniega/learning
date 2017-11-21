# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
 
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    html = response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

content_pattern_zz = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>',re.S)
content_list = re.findall(content_pattern_zz, html)
for item in content_list:
       print "作者："
       print item

print "_______________________________________"

content_pattern_xiaolian = re.compile('<div class="stats">.*?<i class="number">(.*?)</i>',re.S)
content_list = re.findall(content_pattern_xiaolian, html)
for item in content_list:
       print "smile："
       print item

print "_______________________________________"

content_pattern_pl = re.compile('<span class="stats-comments">.*?<i class="number">(.*?)</a>',re.S)
content_list = re.findall(content_pattern_pl, html)
for item in content_list:
       print "评论数："
       print item
