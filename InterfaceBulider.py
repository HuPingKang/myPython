# -*- coding:utf-8 -*-
from swampy.Gui import *
from Tkinter import *


# g = Gui()
# g.title("Interface Builder")
# g.mainloop()

# 创建一个画布
tk = Tk()

def hello():
    ca.create_text(100, 100, text='hello', fill='white')

ca = Canvas(tk, bg='red')
ca.pack(side=LEFT)

fr = Frame(tk)
fr.pack(side=LEFT)

bu1 = Button(fr, text='Hello', command=hello)
bu1.pack()
bu2 = Button(fr, text='Quit', command=tk.quit)
# config方法更改属性
bu2.config(text="我点")
bu2.pack()

tk.mainloop()




