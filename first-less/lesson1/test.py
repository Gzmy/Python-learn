#!/usr/bin/python
#-*- coding:UTF-8 -*-
#
#class Employee:
#	'所有员工基类'
#	empCount = 0
#
#	def __init__(self, name, salary):
#		self.name = name
#		self.salary = salary
#		Employee.empCount += 1
#
#	def displayCount(self):
#		print "Total Employee %d" % Employee.empCount
#
#	def displayEmployee(self):
#		print "name : ", self.name , ", salary : ", self.salary
#
#
#Emp1 = Employee('zmy', 1000)
#Emp2 = Employee('zara', 2000)
##Em.__init__(self, zmy, 1000)
#Emp1.displayCount()
#Emp1.displayEmployee()
#Emp2.displayEmployee()
#Emp2.displayCount()
#

#class Test:
#	def prt(self):
#		print(self)
#		print(self.__class__)
#
#t = Test()
#t.prt()


#class Employee:
#	'所有员工基类'
#	empCount = 0
#
#	def __init__(self, name, salary):
#		self.name = name
#		self.salary = salary
#		Employee.empCount += 1
#	
#	def displayCount(self):
#		print "Total Employee %d" % Employee.empCount
#
#	def displayEmployee(self):
#		print "Name : ", self.name, ', Salary :', self.salary
#
#print "Employee.__doc__", Employee.__doc__
#print "Employee.__name__", Employee.__name__
#print "Employee.__module__", Employee.__module__
#print "Employee.__bases__", Employee.__bases__
#print "Employee.__dict__", Employee.__dict__

#class Point:
#	def __init__(self, x=0, y=0):
#		self.x = x
#		self.y = y
#	def __del__(self):
#		class_name = self.__class__.__name__
#		print class_name, "销毁"
#
#prt1 = Point()
#prt2 = prt1
#prt3 = prt1
#print id(prt1), id(prt2), id(prt3)
#del prt1
#del prt2
#del prt3


#class Parent:
#	parentAttr = 100
#	def __init__(self):
#		print "调用父类构造函数"
#
#	def parentMethod(self):
#		print "调用父类方法"
#
#	def setAttr(self, attr):
#		Parent.parentAttr = attr
#
#	def getAttr(self):
#		print "父类属性", Parent.parentAttr
#
#class Child(Parent):
#	def __init__(self):
#		print "调用子类构造方法"
#
#	def childMethod(self):
#		print "调用子类方法"
#
#c = Child()
#c.childMethod()
#c.parentMethod()
#c.setAttr(200)
#c.getAttr()

#class Parent:
#	def myMethod(self):
#		print "调用父类方法"
#
#class Child(Parent):
#	def myMethod(self):
#		print '调用子类方法'
#
#c = Child()
#c.myMethod()

#class Vector:
#	def __init__(self, a, b):
#		self.a = a
#		self.b = b
#
#	def __str__(self):
#		return 'Vector (%d, %d)' % (self.a, self.b)
#
#	def __add__(self, other):
#		return Vector(self.a + other.a, self.b + other.b)
#
#v1 = Vector(2, 10)
#v2 = Vector(5, -2)
#print v1 + v2

#class JustCounter:
#	__secretCount = 0  #私有变量
#	publicCount = 0
#
#	def count(self):
#		self.__secretCount += 1
#		self.publicCount += 1
#		print self.__secretCount
#
#counter = JustCounter()
#counter.count()
#counter.count()
#print counter.publicCount
#print counter.__secretCount

import re
print(re.search('www', 'www.baidu.com').span())
print(re.search('baidu', 'www.baidu.com').span())
print(re.search('com', 'www.baidu.com').span())




