# -- coding: utf-8 --
from swampy.TurtleWorld import *
from math import pi
world = TurtleWorld()
bob = Turtle()
print bob

# fd(bob,50)
# rt(bob)
# fd(bob,50)
# rt(bob)
#
# fd(bob,50)
# rt(bob)
# fd(bob,100)
# lt(bob)
# fd(bob,50)
# lt(bob)
#
# fd(bob,50)
# lt(bob)
# fd(bob,50)
# lt(bob)
#

bob.delay = 0.02

def square(a,length):
    for i in range(8):
        fd(a,length)
        rt(a,45)  #函数lt和rt默认转动90度，而你可以提供第二个实参来制定角度


def polygon(a,length,n):
    for i in range(n):
        fd(a,length)
        rt(a,360.0/n)  #函数lt和rt默认转动90度，而你可以提供第二个实参来制定角度

def circle(t,r):
    n = int(2*pi*r/10)
    polygon(t,10,n);

def arc(t, r, angle):
    arc_length = 2 * pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)

# circle(bob,100);
# 关键字实参
# circle(bob,r=100);

arc(bob,100,360)
# square(bob,60)

# polygon(bob,3,30)

wait_for_user()
