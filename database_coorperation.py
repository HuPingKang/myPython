
# -*- coding:utf-8 -*-

import anydbm

# 模式'c'意思是如果数据库不存在就创建它。 返回的结果是一个数据库对象，
messgaesDb = anydbm.open('message.db','c')

'''
   你可以像使 用一个字典那样使用它(对于大部分操作来说)。 
   当你创建一个新项时，anydbm会更新数 据库文件。
'''
messgaesDb['name'] = '陈小春'
messgaesDb['addr'] = '香港'
messgaesDb['music'] = '独家记忆'
# messgaesDb['movies'] = ("古惑仔","鹿鼎记","算你狠","犯贱")

print messgaesDb['name'];
print messgaesDb['music'];

# 如果你给一个已存在的键赋予另一个值，anydbm会替换旧值。
messgaesDb['music'] = '算你狠'
print messgaesDb['music']

for key in messgaesDb:
    print key

# 和其它文件一样，当工作完成时必须关闭数据库。


'''
  anydbm的一个限制是键和值必须是字符串。 如果你使用其它类型，就会出错。
  pickle模块可以解决这个问题。 
  它可以将几乎所有对象类型转化成字符串，来存储在数据库中，然后可以将字符串重新转化成原来的对象。
  
'''
import pickle
pic = ['a',122,12.0]
# 对象类型转化成字符串
pic_t = pickle.dumps(pic)
print pic_t

# pickle.loads(“load string”)来还原这个对象。
pic_s = pickle.loads(pic_t)
print pic_s

# 将非字符串类型写入anydbm数据库：
movies = ("古惑仔","鹿鼎记","算你狠","犯贱")
pic_movies = pickle.dumps(movies)
messgaesDb['movies'] = pic_movies        #写入
print pickle.loads(messgaesDb['movies']) #读取

# 换种方式说，使用pickle打包然后解包一个对象，相当于复制了这个对象。
print movies == pickle.loads(messgaesDb['movies']) , movies is pickle.loads(messgaesDb['movies'])

for keys in messgaesDb:
    print keys

# 使用pickle在数据库中存储非字符串。 实际上，这种常见的组合方式已经被封装在 一个叫shelve的模块中了。
# import shelve
messgaesDb.close()

# Shell 命令
import os

# 读取当前文件路径下的文件和文件夹
fp = os.popen("ls")
res = fp.read()
print res

# 当操作结束之后，你需要像文件那样关闭管道:
stat = fp.close()
print stat

fileName = 'word.txt'
cmd = 'md5sum ' + fileName
fps = os.popen(cmd)
ress = fps.read()
print ress
status = fps.close()


print '========****======='
#
# def walk(dirname,fileName):
#
#     for name in os.listdir(dirname):
#         print name
#         path = os.path.join(dirname, name)
#         if os.path.isfile(path):
#             # print path.split("/")[-1]
#             # if path.split("/")[-1] == fileName:
#             #     print fileName
#             #     allfiles.append(path)
#             print path
#         else:
#             walk(path,fileName)

def walk(dirname):
    """Finds the names of all files in dirname and its subdirectories.

    dirname: string name of directory
    """
    names = []
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names

print walk(os.getcwd())

# 你可以使用Unix命令diff进行复核：区分两个文件的不同点。
def check_diff(name1, name2):
    """Computes the difference between the contents of two files.

    name1, name2: string filenames
    """
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)

'''
    __name__是一个内置变量，当程序启动时被赋值
    如果程序作为脚本执行（ 当前正在run的.py文件），__name__的值 是__main__; 
    在这种情况下，测试代码会被执行。 否则，如果模块是被导入的，测试代码 就会被跳过。
'''
print __name__;

'''
    python多次import一个文件，只import一次；类型Objective-C语言；
        如果你将一个已经导入的模块再次导入，Python什么也不会做。 
        Python并不重新读 入这个文件，甚至这个文件已经被修改过。
'''

'''
    repr内置函数:它接受任何对象作为参数，返回其转化成字符串的显示;用于bug调试；
    对于字符串来说，它将空白符转化成反斜杠序列。
    
'''
print '1 2\t 3\n 4 '
print repr('1 2\t 3\n 4 ')
tst = ["hi \n","man \n",12,10.0]
print repr(tst)

# 获取网页数据
import urllib
conn = urllib.urlopen('http://www.baidu.com')
for ls in conn:
    print  ls.strip()
