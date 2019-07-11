#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 猜大小 '
__author__ = 'han qinxun'

import tkinter
import os
import random

guessNum=random.randint(1,100)

def test():
    root=tkinter.Tk()
    root.geometry('500x90+200+200')
    root.title('猜数字游戏')
    lab01=tkinter.Label(root,text='准备开始猜数字',width=80)
    lab01.pack(side='top')

    entry01=tkinter.Entry(root,width=40)
    entry01.pack(side='left')
    entry01.focus_get()

    btn01=tkinter.Button(root,text='猜',width=5)
    btn01.pack(side='left')
    btn02=tkinter.Button(root,text='关闭',width=5)
    btn02.pack(side='left')


    def guess(event):
        v=int(entry01.get())
        if v>guessNum:
            lab01.config(lab01,text='你猜大了')
        elif v<guessNum:
            lab01.config(lab01,text='你猜小了')
        else:
            lab01.config(lab01,text='你猜对了')


    def close(event):
        root.destroy()


    btn01.bind('<Button-1>',guess)
    btn02.bind('<Button-1>',close)

    root.mainloop()




if __name__=='__main__':
    test()
