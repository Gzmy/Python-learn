#!/usr/bin/python
#coding:utf-8

#class Empolyee:
#    '所有员工基类'
#    empCount = 0
#
#    def __init__(self, name, salary):
#        self.name = name;
#        self.salary = salary;
#        Empolyee.empCount += 1
#
#    def displayCount(self):
#        print "Tatal Empolyee %d" %Empolyee.empCount;
#
#    def displayEmplyee(self):
#        print "name : ", self.name, ", salary: ", self.salary;
#
#emp1 = Empolyee('zara', 200)
#emp2 = Empolyee("mani", 500)
#
#emp1.displayEmplyee()
#emp2.displayEmplyee()
#
#print Empolyee.__dict__;
#print Empolyee.__doc__;
#print Empolyee.__name__;
#
#class Point:
#    def __init__(self, x = 0, y = 0):
#        self.x = x
#        self.y = y
#    def __del__(self):
#        class_name = self.__class__.__name__;
#        print class_name, "destroy"
#
#
#pt1 = Point()
#pt2 = pt1
#pt3 = pt1
#print id(pt1), id(pt2), id(pt3)
#
#del pt1
#del pt2
#del pt3

#class Test:
#    def ptr(self):
#        print self;
#        print self.__class__;
#
#t = Test()
#t.ptr()


class Parent:
    parentNum = 100
    def __init__(self):
        print "调用父类构造"

    def parentMethod(self):
        print "调用父类方法"

    def setAttr(self, attr):
        Parent.parentNum = attr

    def getAttr(self):
        print "父类属性: ", Parent.parentNum

class Child(Parent):
    def __init__(self):
        print "调用子类构造"

    def childMethod(self):
        print "调用子类方法"

    def __str__(self):
        msg = "this is test message"
        return msg


#c = Child()
#c.childMethod()
#c.parentMethod()
#c.setAttr(200)
#c.getAttr()

#print Child()

class sweetPotato:
    '模拟烤地瓜'

    def __init__(self):
        self.cookLevel = 0        #烤的等级
        self.cookString = "生的"  #地瓜文字描述
        self.condIments = []      #配料

    def cook(self, time):
        self.cookLevel += time

        if self.cookLevel > 8:
            self.cookString = "烤成灰"
        elif self.cookLevel > 5:
            self.cookString = "烤好了"
        elif self.cookLevel > 3:
            self.cookString = "半生不熟"
        else:
            self.cookString = "生的"

    def addIments(self, iment):
        self.condIments.append(iment)

    def __str__(self):
        msg = self.cookString + "地瓜"
        if len(self.condIments) > 0:
            msg = msg + "("
            for temp in self.condIments:
                msg = msg + temp + ", "
            msg = msg.strip(", ")

            msg = msg + ")"

        return msg

#mySweet = sweetPotato()
#mySweet.cook(4)
#print mySweet.cookLevel
#print mySweet.cookString
#print mySweet.condIments
#print mySweet
#
#mySweet.addIments("fan qie jinag")
#mySweet.cook(2)
#print mySweet.cookLevel
#print mySweet.cookString
#print mySweet

#一个对象与另外一个对象有一定的关系，那么一个对象是另外一个可用对象的属性
class Home:
    def __init__(self, area):
        self.area = area
        #self.light = 'on'
        self.containsItem = []

    def __str__(self):
        msg = "当前房间可用面积：" + str(self.area)
        if len(self.containsItem) > 0:
            msg = msg + "容纳的物品: "
            for temp in self.containsItem:
                msg = msg + temp.getName() + ", "
            msg = msg.strip(", ")
        return msg

    def accommDateItem(self, item):
        needArea = item.getUsedArea()
        if self.area > needArea:
            self.containsItem.append(item)
            self.area -= needArea
            print "ok, in room"
        else:
            print "err, 房间可用面积为：%d，存放所需面积：%d"%(self.area, needArea)

class Bed:
    def __init__(self, area, name = '床'):
        self.name = name
        self.area = area

    def __str__(self):
        msg = "床的面积为：" + str(self.area)
        return msg

    def getUsedArea(self):
        return self.area

    def getName(self):
        return self.name


#newHome = Home(100)
#print newHome
#
#newBed = Bed(20)
#print newBed
#
#newHome.accommDateItem(newBed)
#print newHome


#人类
class Human:
    def __init__(self, name):
        self.name = name
        self.blood = 100
        self.gun = None

    def __str__(self):
        return self.name + "剩余血量:" + str(self.blood)

    def addBullet(self, charger, bullet):
        charger.addBullet(bullet)

    def addCharger(self, gun, charger):
        gun.addCharger(charger)

    def getGun(self, gun):
        self.gun = gun

    def shootGun(self, foe):
        self.gun.shoot(foe)

    def loseBlood(self, harm):
        self.blood -= harm


#弹夹类
class Charger:
    def __init__(self, size):
        self.size = size
        self.sizeList = []

    def __str__(self):
        return "弹夹当前的子弹数量为:" + str(self.size)

    def addBullet(self, bullet):
        if len(self.sizeList) < self.size:
            self.sizeList.append(bullet)

    def shootBullet(self):
        if len(self.sizeList) > 0:
            zidan = self.sizeList[-1]
            self.sizeList.pop()
            return zidan
        else:
            return None

#子弹类
class Bullet:
    def __init__(self, harm):
        self.harm = harm

    def hurt(self, foe):
        foe.loseBlood(self.harm)


#枪类
class Gun:
    def __init__(self):
        self.charger = None

    def __str__(self):
        if self.charger:
            return "枪当前有弹夹"
        else:
            return "枪没有弹夹"

    def addCharger(self, charger):
        if not self.charger:
            self.charger = charger

    def shoot(self, foe):
        zidan = self.charger.shootBullet()
        if zidan:
            zidan.hurt(foe)
        else:
            print "没子弹了"

laowang = Human("老王")

danjia = Charger(30)
print danjia

i = 0
while i < 5:
    zidan = Bullet(5)
    laowang.addBullet(danjia, zidan)
    i += 1

print danjia
