#!/usr/bin/python
#coding:utf-8

'''
用BeautifulSoup4爬虫
'''

import urllib2
import re
from bs4 import BeautifulSoup

#urllib2 进行url请求
#根据url获取对应服务器端的请求

def OpenPage(url):
	#请求头
	Myheaders = {};
	#构造request请求
	req = urllib2.Request(url, headers=Myheaders)
	#激活请求,获取响应
	f = urllib2.urlopen(req)
	data = f.read()
	return data.decode("GBK").encode("utf-8")

def Test1():
	url = "http://www.shengxu6.com/book/2967.html"
	print OpenPage(url)

#从主页获取各个章节的html
def ParseMainPage(page):
	#parser python自带的标准html解析引擎
	soup = BeautifulSoup(page, "html.parser")

	return soup

def Test2():
	url = "http://www.shengxu6.com/book/2967.html"
	page = OpenPage(url)
	ParseMainPage(page)

if __name__ == "__main__":
	#Test1()
	Test2()
	

