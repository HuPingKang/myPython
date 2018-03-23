
# -*- coding:utf-8 -*-

# 要写一个文件，你需要将open函数的第二个参数设置为模式'w'。
# 如果这个文件已经存在，使用写模式打开，会将其之前的内容全部抹去从零开始。
# 所以一 定要小心! 如果这个文件不存在，它会被创建。
fout  = open("output.txt","w")

# write方法将数据写入文件
line1 = "天青色等烟雨，而我在等你\n"
fout.write(line1)

# 文件对象会记录写入的位置，所以再次使用write方法，会在文件的最后写入新数据。
line2 = "问道是三国周郎赤壁"
fout.write(line2)

line3 = "\n第三极-许巍\n"
fout.write(line3)

# 格式化操作符
'''
 write方法的参数必须是一个字符串， 所以当我们要向文件写入其它类型的值，
 我们需要将其转换成字符串。
  
 1.最简单的方法是使用str。
 2.另一种方法是使用格式化操作符(format operator)，%。 
 当应用在整数上时，%是模运算 操作符。 
 但若第一个运算对象是字符串时，%就成为格式化操作符了。
 
'''
line4 = 1000
fout.write(str(line4)+"\n")

# 格式化字符串
line5 = 1314
fout.write(("%d\n" % line5))

# 当写完以后，你需要关闭文件。
fout.close()

# 格式化序列可以在字符串中的任何位置出现， 所以将值嵌入到一句话中:
print "何必管一片海，有多么澎湃；%d 何必看那山高" % 1000

# '%d'格式化一个整数，'%g'格式化一个浮点数(不要问为什么)， '%s'格式化一个字符串
'''
 如果在字符串中出现大于1个格式化序列，那么第二个参数必须是元组。 
 每一个格式化序列 按顺序对应元组中的每一个元素。
 
'''
print "This is %s Victory,This is %s Moment,This is %s Time" % ("Your","Your","Your")


'''
    os模块提供了操作文件和目录的函数(“os”代表“操作系统 operating system”)。 
    os.getcwd返回当前目录名:
'''
import os

# os.getcwd返回当前目录名:
cwd = os.getcwd()
print cwd

'''
  相对路径(relative path)从 当前目录开始; 
  绝对路径(absolute path)从文件系统的最顶端的目录开始。
'''
# 获取某个文件的绝对路径
print os.path.abspath("File_Read_Write.py")

# os.path.exists检测某个文件或者目录是否存在。
print os.path.exists("word.txt")

# 如果存在，os.path.isdir检测其是否是目录(文件夹)。
print os.path.isdir("word.txt")  #文件
print os.path.isdir(os.getcwd()) #文件夹

# 类似地，os.path.isfile检测其是否是文件。
print os.path.isfile("word.txt")

# os.listdir返回文件(以及目录)的列表。
print os.listdir(cwd)

# os.path.join 接受了一个目录和一个文件名并将它们组合成一个完整的路径。
print os.path.join(cwd,"messages.txt")

'''
  当你尝试读写文件时，很容易发生错误:
    如果你尝试打开一个不存在的文件，就会产生IOError。
    如果你没有权限操作一个文件:
    如果你尝试写一个目录
  
  为了避免这些错误，你应该使用os.path.exists和os.path.isfile这类函数，
  但是这会 占用你很多时间检查所有的可能性;
  
  更好的办法是就这样尝试着执行下去—如果有错误再处理—这就是try语句做的事。 
  它的 语法与if语句很相似:
  try:
    fin = open('bad_file')
    for line in fin:
        print line
    fin.close()
  except:
    print 'Something went wrong.'
    
  
'''
# openFi = open("dzbEnglish.txt")
# fout = open('/etc/passwd', 'w')
# fin = open('/home')

'''
    Python首先执行try子句。 如果一切正确，except子句就会被跳过，接着执行下面的语 句。 
    如果有异常发生，它会跳出try子句，执行except子句。
'''
try:
    openFi = open("messages.pdf")
    for li in openFi:
        print li;
    openFi.close()
except:
    print "文件读取失败"

import database_coorperation
