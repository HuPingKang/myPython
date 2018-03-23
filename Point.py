
# -*- coding:utf-8 -*-
import copy
class Info(object):
    name,addr,phone = "","",0

class Point(object):
    """Represents a point in 2-D space."""

    # 添加属性
    name,age,isMan = "",0,False
    message = Info()

    # 对象方法
    def logMessage(t):
        print t

    # 对象方法
    def getPoint():
        point = Point()
        point.age = 18
        point.isMan = False
        point.name = "芳华"
        return point;

# 创建一个新对象的过程叫做实例 化(instantiation)，
# 这个新对象叫做这个类的一个实例(instance)。
blan = Point()
print blan
blan.name,blan.isMan,blan.age = "小花",False,15
print blan.name,blan.isMan,blan.age


# 格式化输出
# print '(%g,%g)' % (100.0,200)

# python浅拷贝和深拷贝：

# 1、浅拷贝
    # 通常用复制对象的方法取代为对象起别名。
    # p1和p2拥有相同的数据，但是它们并不是同一个Point对象。
    # 这个操作叫做浅复制(shallow copy)，
    # 因为仅复制了对象以 及其包含的引用， 但未复制嵌套的对象。
# 2、深拷贝
#   不仅可以复制一个对象，还可以复 制这个对象所引用的对象，
#   甚至可以复制这个对象所引用的对象所引用的对象，等等

blan2 = copy.copy(blan)
blan3 = copy.deepcopy(blan)
# ==运算符 的默认行为和is运算符相同; 它检查对象的身份是否相同，而非对象的值是否相同。
print \
    blan2.name,\
    blan is blan2,\
    blan==blan2,\
    blan.message is blan2.message

print "========="
print \
    blan3.name,\
    blan3 is blan,\
    blan == blan3,\
    blan3.message is blan.message