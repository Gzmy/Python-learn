#!/usr/bin/python
#coding:utf-8
#用程序打开网页

import urllib2

#response = urllib2.urlopen('http://www.baidu.com')
#html = response.read()
#print html

#请求的url地址
url = "http://www.baidu.com"

#伪装的浏览器user-agent头
user_agent = 'Mozilla/5.0(compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;)'

#创建一个字典,使请求的headers中'User-Agent':对应我们的user_agent字符串
headers = {'User-Agent':user_agent}

req = urllib2.Request(url, headers = headers)

response = urllib2.urlopen(req)

the_page = response.read()

print the_page
















