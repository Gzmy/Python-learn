#!/usr/bin/python
#coding:utf-8

import urllib2

def write_file(file_name, text):
	print '正在存储文件' + file_name
	f = open(file_name, 'w+')
	f.write(text)
	f.close()

def load_page(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	html = response.read()

	return html

def tieba_spider(url, begin_page, end_page):
	user_agent = 'Mozilla/5.0(compatible; MSIE 9.0; Windows NT6.1; Trident/5.0;'
	headers = {'User-Agent':user_agent}
	
	for i in range(begin_page, end_page):
		pn = 50 * (i - 1)
		html = load_page(url+str(pn))

		file_name = str(i) +'.html'
		print '正在下载第' + str(i) + '个网页'
		write_file(file_name, html)

if __name__ == '__main__':
	bdurl = str(raw_input('请输入贴吧地址,去掉pn=后面的数字:'))

	begin_page = int(raw_input('请输入开始的页数'))
	end_page = int(raw_input('请输入结束的页数'))

	tieba_spider(bdurl, begin_page, end_page)
