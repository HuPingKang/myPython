
# -*- coding:utf-8 -*-
# 元祖是不可变的
tuple_a = (1,2,3,4)
# 为了用一个单独的元素生成一个元组， 你必须包括最后的逗号:
tuple_b = 1,
print type(tuple_b)
print type(tuple_a)

# 括号中的一个值不是元组:
print type(1)

# 元祖的初始化,生成一个空的元祖
t = tuple()

# python中的序列包括：list/dict/string
tt = tuple('abcdefg')
# 如果实参是一个序列(字符串、列表或元组)， 返回值是一个以该序列元组组成的元组。
# ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print tt

# 元祖的运算方法：tt[0] tt[1:3] +
print tt[0]
print tt[1:3]
print tt[1:3]+("ab",)
# 如果你试图修改一个元组的元素，你会获得一个错误:
# tt[0] = "ABABA"
# 你不能改变元组的元素，但是你可以用一个元组替换另一个
tt = ('abs',)+tt[1:]
print tt

# 元祖赋值
ttt = ('a','cc')
tttt = ttt
print tttt

# 元祖值交换
tts = ("aaaa","cccc")
ttx = ('aaaaa','cc')
# tss = tuple()
# tts = tss
# tss = ttx
# ttx = tts
# print tts,ttx,tss

# 左侧是一个变量的元组;右侧是表达式的元组。
# 每个值被赋给它的各自的变量。 右侧的所有表达式在赋值之前被计算。
tts,ttx = ttx,tts
print tts,ttx
print type(ttx),type(tts)

# 更一般地，右侧可以是任意类型的序列(字符串、列表或者元组)
tts,ttx = "836546005@qq.com".split("@")
print tts,ttx

# 字符串赋值
ass,bss = "123@qq.com".split("@")
print ass,bss
print type(ass),type(bss)
print type(ttx),type(tts)

test_a = tuple()
test_b = tuple()
test_a,test_b = "836546005@qq.com".split("@")
print test_a,test_b
print type(test_a),type(test_b)

# 元祖作为返回值:解决了一个函数只能返回一个值的问题，元祖可以存放多个值,
# 再使用多个元祖变量同时赋值：a,b,c = (),(),()，实现一个函数返回多个值的使用
def test_tuple():
    return ("836546005","@qq.com")

my_email = test_tuple()
print my_email

# divmod接受两个实参并返回两个值的元组，商和余数
test_divmod = divmod(10,3)
print test_divmod

# 返回一个list里面的最小和最大元素，作为元祖：
def min_max(t):
    return min(t),max(t)

maxMin = min_max([3333,1,2,3,555,22])
print maxMin

# 函数可以接受一个可变数量的实参。 一个以*开始的形参名汇集(gathers)实参到一个元组中
def printAll(*args):
    print args,type(args)

mlgb = (1,23)
haha = [2,3,4,5]
bbb = "aaa"

printAll(mlgb,haha,bbb)

# zip内建函数：
# zip是一个内建函数，其接受两个或者更多的序列并把它们“zip”到一个元组列表中， 其中 每个元组包括来自每个序列的一个元素
ss = "Absorts"
kk = [1,2]
# 序列长度不同，结果是较短的序列的长度。
print zip(ss,kk)  #[('A', 1), ('b', 2)]

# 元祖列表的for循环
for a,b in [(1,2),("aa","bb")]:
    print a,b

# 如果你需要遍历一个序列的元素以及它们的索引值， 你可以使用内建函数enumerate
for index,element in enumerate("absddf"):
    print index,element;

# 字典的items()方法：返回一个元祖的列表，其中每个元祖是一个键值对：
dix = {"aa":1,"bb":2,"cc":3}
dix_tuple = dix.items()
print dix_tuple  #[('aa', 1), ('cc', 3), ('bb', 2)]

# 将元祖的列表转化成字典
dixx = dict(dix_tuple)
print dixx

# 元祖作为字典的键和值：
my_dix = dict()
my_dix[(0,1)] = ("Hpk","huPingKang")
my_dix[3] = "Hello ShangHai"
print my_dix

# 元祖比较
'''
# 关系运算符可用于元组和其它的序列;Python开始比较每个序列的第一个元素。 如果它
们相等，它继续到下一个元素，以此类推，指导发现不同的元素。 后续的元素不被考虑了
(即使它们相当的大)
'''
print (1,2) < (0,3)

kks = [('A',1),('A',2)];
# reverse=True 从大到小排序，reverse=False 从小到大排序
kks.sort(reverse=True)
print kks

'''
因为元组是不可变的，所以它们不提供类似sort和reverse的方法， 
其改变已有的列表。 但是Python提供内建函数sorted和reversed，
其接受任意序列作为形参并返回一个新的 相同元素，不同顺序的列表。
'''
# 列表、字典和元组通常被看做数据结构(data structures)
tuple_ss = sorted((1,3,2))
print tuple_ss
