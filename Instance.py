
# -*- coding:utf-8 -*-
# 1.必须将编码注释放在第一行或者第二行
# 2.可选格式有

import Category
# 引用数据库类文件
import  anydbm
import  math   #调用数学函数
# import Tkinter
from Tkinter import *           # 导入 Tkinter 库

import MySQLdb
# import MacOS

ss = math.factorial(3)
print ss

print "你好，世界！";

foot = ["1","2",2.3,2111];  #数组里面可以存放不同类型的数据类型，甚至对象；

print foot;

#for in 循环：i代表数组里面的每个值；
for i in foot:
    print i;

#数数：
for i in range(10):
    print i;


def foo(a,b,c):
    return a+b+c;

print foo(1,2,3.4);


def makeVarious():
    backStr = "woshiyizhibird";
    return backStr;

print makeVarious()

print "%s",("上海");

res = 100;
if res<200 and res>50 or res>100:
    print "判断正确"
else:
    print "判断失败"

#多行显示
#但是我们可以使用斜杠（ \）将一行的语句分为多行显示
mine = "1" + "2" \
    "3" + "4" + \
    "5";
print mine;

#语句中包含[], {} 或 () 括号就不需要使用多行连接符。如下实例：
array = ["a","b","c"
          ,"d","e"];

""""
这是一个多行注释

"""
"""
Python空行

函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
记住：空行也是程序代码的一部分。

"""

# raw_input("Enter Your Password:");
#
# root = Tk();
# root.mainloop();
#                                 # 创建两个列表
# li = ['C','python','php','html','SQL','java']
# movie = ['CSS','jQuery','Bootstrap']
# listb = Listbox(root)          #  创建两个列表组件
# listb2 = Listbox(root)
# for item in li:                 # 第一个小部件插入数据
#     listb.insert(0,item)
#
# for item in movie:              # 第二个小部件插入数据
#     listb2.insert(0,item)
#
# listb.pack()                    # 将小部件放置到主窗口中
# listb2.pack()
# root.mainloop()                 # 进入消息循环

testA,testB,testC = 1,2,"Say Hi"

print testA
print testB
print

# 使用del语句删除一些对象引用。
del testC,testB
print testA

s = "a1a2a3...an"
print s


print math.log10(100)
print math.sin(30)


# python函数声明 def；
def NSLog():
    print ("自定义函数")
    print ("自定义函数python")

NSLog()

def NSLog(a,b):
    print a
    print b
    print a,b

NSLog(120,'afifbkf')

# bool运算符(== != >= <= > <) 求余运算符(%) 逻辑运算符（and or not ）
if 10>3:
    print ("这是真爱！！！")

if not 2>3:
    print ("他不爱我--林俊杰")

if '我在上海':
    print ("这是真事")

# if语句体中至少包含一句
if 1>0:
    pass
    print ("pass什么也不干")

if 3>4:
    print ("卧槽尼玛")
else:
    print ("搞什么飞机啊")

if 3>4:
    print ("wo ro")
elif 3==4:
    print ("wrong")
else:
    print ("right")

# python2
# ms = raw_input('Enter Your Name:')
# print ms
# python3
# input()


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            print ("❤️")
            return index
        print ("😊")
        index = index + 1
    return -1

print (find("hello","o"))

# 字符串方法：len upper lower find  in运算等
print (len("hello world"))
print ("hello".upper())
print ("world".find("l"))
print ("mlgbdqnmd").find("nm")

# 中文的长度为一个字三个字节
print len("上海东方明珠电视塔，世界互联网大会")
print len("🔥")

print "上海东方明珠电视塔，世界互联网大会".find('世界',4) #从第四个位置开始找
print "上海东方明珠电视塔，世界互联网大会".find('世界',4,44) #从第四个位置开始找，找到第44个位置（不包括44）

print ("shangHai".lower())
print "90000"

print "a" in "abs" #第一个字符串包含在第二个字符串中

#字符串比较大小 : 小写>大写
words = "ShangHai"
if words == "shang":
    print "🔥"
elif words > "sHang":
    print "🌲"
else:
    print "🦐"


#读取一个文件 输出结果
fin = open('word.txt')
# print fin.readline()
# for letter in fin.readlines():
#     print letter

# for letter in fin:
#     print letter


# 如果空格困 扰了你，我们可以用字符串方法strip删掉它
# print "shanghai shangHHH\r shh".strip()

def has_no_e(a):
    for ll in a:
        if ll == "e":
            return True
    return False

def log_no_e(a):
    if has_no_e(a):
        print a

print has_no_e("abcdfsgg")
print has_no_e("abchefg")

log_no_e("abcdefgppppp")
log_no_e("abcdggg")

def avoids(a,b):
    for letter in a:
        if letter == b:
            return False
    return True

def avoids_upper(a,b):
    if b not in a:
        return True
    return  False;

def avoids_upper_upper(a,b):
    return (b not in a)

print avoids("abs","a")
print avoids("abs","l")
print avoids_upper("abs","a")
print avoids_upper_upper("abs","l")

# python中的list（列表）：数组 字典等
nuimber = ["s",12,10.1,["",11]]
nuimber[0] = 1111   #列表是可变的  字符串是不可变的
print nuimber[-1] #如果一个索引是一个负值，它从列表的结尾往回数
print (12 in nuimber)  #in运算符也可以用于列表。

print type(nuimber)

# for in
# 空列表上的for循环从不执行循环 体:
for kk in nuimber:
    print kk

for i in range(len(nuimber)): #len 计算list的长度
    print nuimber[i]

# 列表的运算 ： + * 切片
xx = ["a"]
xb = ["b"]
xp = xx+xb
print xp
xs = xx+xb+xx*2
print xs
print xs[:2]
print xs[:]  #如果你不写第一个索引，切片起始于开始。 如果不写第二个，切片直到结束。 所以，如果 你两个都不写，切片拷贝整个列表。

# 赋值语句左侧的切片运算符可以更新多个元素:
xm = xs*3
xm[2:5] = ["2","3","4"]
print xm

#列表的操作： append extend sort 没有返回值
# append在列表结尾增加一个新元素
# extend将一个列表作为实参并追加所有的元素
# sort从低到高排列列表的元素:
xxss = ["a","d","c","m","b"]
xxss.sort()
print xxss
xxss.append("MM")
xxss.extend([20,11])
print xxss
xxss.sort()
print xxss

axa = 0
axa+=10
axa-=1

# python 自动计算法sum 只能计算数字类型，不能计算字符串
print sum([1,2,3])
# sum(["a","v"])

# capitalize 把字符串的首字母变为大些
print "sxs".capitalize()

# pop 删除元素：pop改变列表并返回被删除的元素。 如果不提供索引，它删除并返回最后一个元素。
t = ["a","b","d"].pop(1) #删除列表中的元素，返回删除的元素
print t

# 如果你不需要被删除的值，你可以使用del运算符:
tts = ["a","b","c","d","e","f"]
del tts[1]
del tts[2:4]  #切片删除
print tts
tts.remove("a") #删除特定值元素
print tts

tsl = "avchbws"
# list将字符串转化成字符列表
tsla = list(tsl)
print tsla

tslla = 'pining for the fjords'
# 将字符串分成单词，你可以使 用split方法:
tsllaa = tslla.split()
print tsllaa

sqlites = 'spam-spam-spam'
#根据特定字符切割
sqlitesss = sqlites.split("-")
print sqlitesss

qqa = ['pining', 'for', 'the', 'fjords']
# 根据特定字符拼接  join是一个字符串方法
qqai = '--'.join(qqa)
print qqai

# 模式'c'意思是如果数据库不存在就创建它。 返回的结果是一个数据库对象，你可以像使 用一个字典那样使用它(对于大部分操作来说)。 当你创建一个新项时，anydbm会更新数 据库文件。
# db = anydbm.open('hpk.db','c')
# sql = "CREATE TABLE 'messages'('id' INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,'name' VARCHAR (255),'sex' VARCHAR (255),'phone' VARCHAR(255))"
# db.execute(sql)
# CREATE TABLE 'pauseDatas' ('id' INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL ,'planId' VARCHAR(255) , 'planType' VARCHAR(255) , 'courseId' VARCHAR(255) , 'courseName' VARCHAR(255) , 'pauseTime'   integer , 'pausePart' integer , 'pauseCardTimes' integer , 'pauseCardIndex' integer , 'progressNum' integer , 'lastPlayCount' integer , 'lastTestString' VARCHAR(255) , 'lastResultDix' VARCHAR(255) , 'hasBegin' integer , 'learnStage' VARCHAR(255) , 'testResults' VARCHAR(255) , 'stages' VARCHAR(255) , 'saveDix' VARCHAR(255) , 'timeString' VARCHAR(255))

# 如果两个对象相同，那么它们也是相等的， 但是如果它们相等，它们不一定相同。
# a = 'banana'
# b = 'banana'
# a is b
# True

# 我们应该说两个列表相等(equivalent) 因为它们具有相同的元素，但不是相 同(identical) 因为它们不是相同的对象
# a = [1, 2, 3]
# b = [1, 2, 3]
# a is b
# False

# 变量和对象之间的关联被称作引用(reference)
# >>> a = [1, 2, 3]
# >>> b = a
# >>> b is a
# True
#
# >>> b[0] = 17
# >>> print a
# [17, 2, 3]

sqliteDb = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
