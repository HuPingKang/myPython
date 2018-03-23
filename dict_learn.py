
# -*- coding:utf-8 -*-

# dict函数生成一个新的没有任何项的字典。 因为dict是内建函数名，你应该避免将其用于 变量名。
eng2sp = dict()
eng2sp['hi'] = 'hello'
print eng2sp
eng2sp[1] = 100
print eng2sp
eng2sp[0]=909
print eng2sp
eng2sp['aaa'] = 222
print eng2sp
# 以键取值
print eng2sp[0]
print eng2sp['aaa']

# in 告诉你是否一些东西在字典中作为键出现 (作为值出现不够 好)。
print 'aaa' in eng2sp
# key和value
print eng2sp.keys()
print eng2sp.values()

# 如果你在for中使用字典，那么它遍历该字典的键
for kk in eng2sp:
    print kk
