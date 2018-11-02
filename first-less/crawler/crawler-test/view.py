#!/usr/bin/python
#coding:utf-8
#用程序打开网页

import urllib2
import re
form bs4 import BeautifulSoup
'''

yum install python-pip
BeautifulSoup4
pip install BeautifulSoup4
'''

#使用Python获取url响应
def OpenPage(url):
	Myheaders = {}
	#urllib2.Request方法构建http请求
	request = urllib2.Request(url, headers=Myheaders)
	#根据构建请求,获取服务器响应内容
	f = urllib2.urlopen(request)
	return f


