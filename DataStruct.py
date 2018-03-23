
# -*- coding:utf-8 -*-
import string
import random

# words = open('word.txt')
# for kk in words:
#     print (string.whitespace in kk) #+'空格'
#     print (string.punctuation in kk) #+'标点'
#     print kk
#
#     # kk.replace(string.whitespace,"")
#     tt = tuple(string.punctuation)
#     ss = tuple(kk)
#     print tt,ss

print "完成"


# 随机数 random
# 函数random返回一个0.0到1.0之间的随机浮点数(包括0.0，但是不包括1.0)
for i in range(10):
    print random.random()
# 函数randint接受参数low和high， 并返回一个low和high之间的整数(两个都包括)
print random.randint(2,5)
# 为了从一个序列中随机的选择一个元素，你可以使用choice:
print random.choice([11,2,444])

def process_file(filename):
    hist = dict()
    fp = open(filename)
    print fp
    for line in fp:
        print line
        process_line(line, hist)
    return hist
def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

hist = process_file('shape.txt')