# -*- coding:utf-8 -*-
# 继承

class Human(object):
    sex,name,age,height = "Man","",0,0;
    def print_height(self):
            print("我的身高是：%f" % self.height)
    @staticmethod
    def getClass(self):
        print("我属于Human类")

class Man(Human):
    hasMusle,isStrong,isSmart,isHandSome = False,False,False,False;
    def areYouStrong(self):
        if self.isStrong:
            print ("我很强")
        else:
            print ("我很弱")

    def getMySex(self):
        print(self.sex)


man = Man()
man.sex = "BigMan"
man.name = "Smitch EOS"
man.age = 20
man.height = 200;
man.hasMusle = True;
man.isStrong = True;
man.isSmart = True;
man.isHandSome = True;

man.areYouStrong()
man.getMySex()
man.print_height()
