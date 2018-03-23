
# *- coding:utf-8 -*-
from swampy.Gui import *
from Tkinter import *


# def hello():
#     ca.text([0, 0], 'hello', 'blue')
#
# gui = Gui()
# gui.row()
# ca = gui.ca(bg='white')
#
# gui.col()
# gui.bu(text='Hello', command=hello)
# gui.bu(text='Quit', command=gui.quit)
# gui.endcol()
#
# gui.endrow()
# gui.mainloop()

tk = Tk()


def hello():
    ca.create_text(100, 100, text='hello', fill='blue')

ca = Canvas(tk, bg='white')
ca.pack(side=LEFT)

fr = Frame(tk)
fr.pack(side=LEFT)

bu1 = Button(fr, text='Hello', command=hello)
bu1.pack()
bu2 = Button(fr, text='Quit', command=tk.quit)
bu2.pack()

tk.mainloop()


# g = Gui()
# g.title('Gui')
# g.mainloop()
# button = g.bu(text='Press me.')
# button2 = g.bu(text='No, press me!')


# label = g.la(text='Press the button.')
#
# canvas = g.ca(width=500, height=500)
# canvas.config(bg='white')
# canvas.rectangle([[0, 0], [200, 100]],
#                  fill='blue', outline='orange', width=10)
# canvas.oval([[0, 0], [200, 100]], outline='orange', width=10)
# canvas.line([[0, 100], [100, 200], [200, 100]], width=10)
# canvas.polygon([[0, 100], [100, 200], [200, 100]],
#                fill='red', outline='orange', width=10)
#
#
# item = canvas.circle([0,0], 100, fill='red')
# item.config(fill='yellow', outline='orange', width=10)
#
# entry = g.en(text='Default text.')
#
# text = g.te(width=100, height=5)
# text.insert(1, 'A line of text.')
#
# def make_label():
#     g.la(text='Thank you.')