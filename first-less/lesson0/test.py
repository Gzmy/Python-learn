#!/usr/bin/python
#-*-coding:UTF-8-*-
# print mystr
# 列表解析
# 获取1到100的平方序列
# 期望结果是[1, 4, 9, ...]
#print [x ** 2 for x in range(1, 101)]

# 获取3的倍数的平方
#print [x ** 2 for x in range(1, 101) if x % 3 == 0]

#print 'hello python'

#函数定义

#for letter in 'Python':
#if letter == 'h':
#		pass
#		print '这是pass块'
#	print'当前字母:', letter
#
#print"good bye!"

#for x in range(0, 11):
#	print x
#print "完了"

#2到100之间的素数,循环嵌套
#i = 2
#while(i < 100):
#	j = 2
#	while(j <= (i/j)):
#		if not(i%j):break
#		j = j + 1
#	if(j > i/j):
#		print i, "是素数"
#	i = i + 1
#
#
#print"goodbye"


#for letter in 'python':
#	if letter == 'h':
#		break
#	print'当前字母:', letter
#
#var = 10
#while var > 0:
#	print'当前变量值:', var
#	var = var - 1
#	if var == 5:
#		break
#
#
#x = 190.29821903801
#int (x)
#print x
#
#
#list1 = ['python', 'home', 'dream', 'gzy']
#list2 = [1, 2, 3, 4, 5, 6]
#
#print 'list1[3,4]', list1[1:4]
#
#
#dict = {
#		'name':'zara', 'age':7, 'class':'first'
#		};
#print "dict['name']", dict ['name'];
#print "dict['age']", dict['age'];
#
#
#a = 10
#def cahnge(a):
#	a = 20
#	print"函数内取值:", a
#cahnge(a)
#print"函数外取值:", a
#
#
#def printinfo(arg1, *vartuple):
#	"打印任何传入参数"
#	print"输出:"
#	print arg1
#	for va in vartuple:
#		print va
#	return
#
#printinfo(10)
#printinfo(10,20,30)
#

#sum = lambda arg1, arg2 : arg1 + arg2
#sum = lambda arg1, arg2, arg3 : arg1 + arg2 + arg3
#
#print "值为:", sum(10, 20, 30)
#

#import support#引入模块
#调用模块内的函数
#support.print_func(666)
#
#money = 2000
#def AddMoney():
#	global money
#	money = money + 1
#
#print money
#AddMoney()
#print money
#
#str = raw_input("请输入:")
#print "输入内容", str
#
#str = input("请输入")
#print "输入内容:", str
#

#import os
#
#os.remove("foo.txt")

try:
	fh = open("testfile", "w");
	fh.write("这是一个测试文件,用于测试异常!")
except IOError:
	print "Error:没有找到文件或读取文件失败"
else:
	print "内容写入文件成功"
	fh.close()









