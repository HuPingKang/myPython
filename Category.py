
# -*- coding:utf-8 -*-
# 1.必须将编码注释放在第一行或者第二行
# 2.可选格式有
def getStrings():
    return "MacBook Pro";

def addNumbers(a,b):
    return a+b;

computerName = "macbook pro 2016";


#以下划线开头的标识符是有特殊意义的。以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用"from xxx import *"而导入；

_fooTestStr = "American";

testEnglish = "English";

#以双下划线开头的（__foo）代表类的私有成员;
__fooPrivateStr = "";

#以双下划线开头和结尾的  \（__foo__）代表python里特殊方法专用的标识，如__init__（）代表类的构造函数。
def __fooTestScore__():
    print "特殊方法专用的标识";


def __init__():
    print "初始化";

__init__();


