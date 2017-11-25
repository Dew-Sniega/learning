#爬取落网专栏每个文章的url和标题

# -*- coding:utf-8 -*-
import urllib
import urllib2
import re


user_agent = 'Mozilla/5.0 (Windows NT 6.1)'
headers = { 'User-Agent' : user_agent }

for i in range (1,70):
    url = 'http://www.luoo.net/essay/index/p/'+str(i)+'.html'
    print url

    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

    pattern = re.compile('<div class="essay-wrapper".*?<a href="(.*?)">', re.S)
    items = re.findall(pattern, html)
    for item in items:
        print item.replace('" title=', ' ').replace('class="title', '')

        
#输入回车加载下一页，输入Q退出
    input = raw_input()
    if input == "":
        print "nextPage:"
        continue
    elif input =="Q":
        break

