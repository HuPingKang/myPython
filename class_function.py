
# -*- coding:utf-8 -*-
class Time(object):
    '''表示今天的时间:
        属性：hour , minute , second
        对象方法：print_time (打印当前时间)
    '''
    hour,minute,second = 0,0,0


    '''
        声明一个实例方法：形参至少包含self；
    '''
    # 方法在一个类定义内部声明，为了显示地同类进行关联。
    # 约定方法的第一个参数写作self，所以print_time写成:
    def print_time(self):
        # %.2d输出两位数字：类似%02d
        print '%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second)

    # 带有两个参数的方法：使用第一个对象调用的时候，只需要传递第二个对象作为参数；
    def print_times(self,other):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
        print '%.2d:%.2d:%.2d' % (other.hour, other.minute, other.second)

    # 对象的初始化方法
    def __init__(self,hour=0,minute=0,second=0):
        self.hour,self.minute,self.second = hour,minute,second

    # __str__是一个和__init__方法类似的特殊方法，用来返回一个对象的字符串表达。
    # 当你print一个对象，Python调用str方法:
    def __str__(self):
        return "BeiJing Time is 18:06"

    # 执行Time的两个对象相加的操作时调用
    def __add__(self, other):
        print "两个Time对象相加了"
        print other  #调用print时，调用__str__方法；

    '''
       声明一个类方法/静态方法：
    '''
    @staticmethod
    def print_staticMethod():
        print("我是一个静态方法/类方法！")
    @staticmethod
    def print_staticMethods(a):
        print(" 我是一个带参数 %s 的静态方法/类方法" % a)

time = Time()
time.hour = 12
time.minute = 34
time.second = 56

other = Time()
other.hour = 10;
other.minute = 30
other.second = 59

# 方法既可以用类调用，也可以用对象调用
time.print_time()       #对象调用
Time.print_time(time)   #类调用
time.print_times(other) # 带有两个参数的方法,使用第一个对象调用的时候，只需要传递第二个对象作为参数；

# 如果你不带参数的调用Time，你会得到默认值。
test_zero = Time()
test_zero.print_time()

# 如果你提供一个参数，它会覆盖hour:
test_one = Time(11)
test_one.print_time()

# 如果你提供两个参数，他们会覆盖hour和minute。
test_two = Time(11,20)
test_two.print_time()

# 如果你提供三个参数，它们会覆盖三个默认值。
test_three = Time(17,57,59)
test_three.print_time()

test_three+test_two
# 当你print一个对象，Python调用str方法:
print test_three

"""
   类方法的调用
    
"""
Time.print_staticMethod()
Time.print_staticMethods("100")

print("----" * 20)

"""
   isinstance 判断对象test_one的类型是否是Time；

"""
print( isinstance(test_one,Time))
print(isinstance("",Time))

# 纯函数
'''
    该函数创建一个新的Time对象，初始化它的属性，
    然后返回这个新对象的引用。这个被叫做 纯函数;
    因为它没有修改任何以参数传入的对象并且没有副作用。
    最后返回了一个值。
    
'''
def add_time(t1,t2):
    sum = Time()
    sum.hour = t1.hour+t2.hour
    sum.minute = t1.minute+t2.minute
    sum.second = t1.second+t2.second
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum;


# **keywords表示接收的是一个字典类型（包含key=value）
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
'''
输出结果：
    -- Do you have any Limburger ?
    -- I'm sorry, we're all out of Limburger
    It's very runny, sir.
    It's really very, VERY runny, sir.
    ----------------------------------------
    shopkeeper : Michael Palin
    client : John Cleese
    sketch : Cheese Shop Sketch
'''

# 声明一个带默认值的函数：有值的形参可以不传
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action)
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# 正确的调用函数：
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# 错误的调用函数
'''
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument

'''

'''
range的使用：
    range(5, 10) --> 5 through 9
    range(0, 10, 3) --> 以3递增  : 0, 3, 6, 9

    list(range(3, 6)) --> [3, 4, 5]  
    args = [3, 6]
    list(range(*args)) --> [3, 4, 5]

'''

print lambda x:x+10
