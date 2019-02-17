#!/usr/bin/python
#coding:utf-8

#测试函数
def printme( str_ ):
    print str_;
    return;
#
#printme("use one")
#printme("use two")

#printme()

#printme( str_ = "my string" )
#
#def printinfo( name, age = 10 ):
#    print "name", name;
#    print "age", age;
#    return;
#
#printinfo(age = 50, name = 'john')
#printinfo(name = 'zmy')

#不定长参数
#def printnum( arg, *vartuple ):
#    print "output", arg
#    for var in vartuple:
#        print var,
#    return;
#
#printnum(31)
#printnum(13, 13, 10, 22, 20)

#可写函数说明
#mysum = lambda arg1, arg2 : arg1 + arg2
#
#print mysum(10, 20)
#print mysum(20, 20)

#def mysum(arg1, arg2):
#    total = arg1 + arg2;
#    return total;
#
#print mysum(10, 20)

# 全局变量作用于函数内需要加global

#var = 0
#
#def set_global_to_one():
#    global var;
#    var = 1
#
#def print_var():
#    print var;
#
#print var
#set_global_to_one()
#print var
#print_var()

#列表反转函数
#def reverse1( li ):
#    for i in range(0, len(li)/2):
#        temp = li[i]
#        li[i] = li[-i-1]
#        li[-i-1] = temp
#
#def reverse2( li ):
#    tmpList = []
#    for i in range(len(li)):
#        tmpList.append(li.pop())
#    return tmpList
#
#mylist = [1, 2, 3, 4, 5]
#
#print reverse2(mylist)

#print len(mylist)
#print mylist[-2]
#reverse(mylist)
#print mylist

#def function():
#    '''  i love python
#    '''
#    pass
#
#print function.__doc__


#参数顺序
#def printme(str, int):
#    print str, int;
#    return;
#
#printme(int = 20, str =  'my num is')

#def add(x, y):
#    return x+y
#
#def add_twice(func, x, y):
#    return func(func(x, y), func(x, y))
#
#a = 10
#b = 20
#
#print add_twice(add, a, b)

#import support
#import os
#
##support.print_func("hello python")
#
##print dir(support)
#
#print dir(os)

#from package.pack1 import test1
#from package.pack2 import test2
#
#test1()
#test2()

#mystr = raw_input("please input")
#print "your input is: ", mystr

#可以对输入数据进行运算
#mystr = input("please input: ")
#print "your input is: ", mystr

fo = open("read.txt", "w")

print "file name", fo.name
print "is close?", fo.closed
print "file mode", fo.mode
print "is add sapce", fo.softspace
