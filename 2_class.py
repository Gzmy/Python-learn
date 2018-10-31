#!/usr/bin/python
#coding:utf-8

#a = b = 2
#print id(a)
#print id(b)
#
#b = 1
#print id(b)
#
#b = 2
#print id(b)

#a,b = 1,1
#
#if a == b :
#    print "success!"
#elif 1 > 2: #else if 的缩写
#    print "error"
#print "finish"
#
#count = 1
#while count < 10:
#    if count % 2 == 0:
#        print count
#    else:
#        print '奇数'
#    count += 1

#for循环可以遍历一切可以遍历的对象 list tuple dict
#list1 = [1, 2, 3, 4]
#for x in list1:
#    print x

#range(start, stop, step) 开始,结束,步长, 返回一个list
#print range(0, 10, 2)
#for x in range(20):
#    if x % 2 == 0:
#        print x

#pass 无为 do nothing

#list1 = [x ** 2 for x in range(20)]
#print list1

#函数
#def Sum(x=100, y=200):
#    return 3, 5 #返回元组
#a, b = Sum()
#
#print a, b

#handler = open("log.txt", "r")
#word = {} #保存字符串以及字符串出现次数
#for x in handler:
#    x = x[:-1]
#    if x in word:
#        word[x] += 1
#    else:
#        word[x] = 1
#print word
#handler.close()

#x, y = 1, 2
#x, y = y, x
#print x, y

#注意!
#True, False = False, True
#if True:
#	print "error"

#函数可以改变作用域


