
# -*- coding:utf-8 -*-

# 列表的运算 : + [:](切片)
a=[1,2,3]
b=['a','b','c']
c=a+b

c=c*2

print c

c[1:3]

print c

c.append("333")
c.extend(['1','2222'])
# sort从低到高排列列表:
c.sort()
print c

t = [1,2,3,4]
# 计算list的和：适用数字类型
print sum(t)
# ss = ['a','b']
# print sum(ss)

# isupper是一个字符串方法， 如果字符串只包含大写字母，其返回True。
print "S is upper".isupper()
print 'SS'.isupper()

print "hello".strip()
# print "world".sort()