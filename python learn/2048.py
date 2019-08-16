#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 2048 game '

__author__ = 'han qinxun'

import os
import tkinter
import tkinter.font
from tkinter import messagebox as msgbox
import random

dict = {0:'white',2:'orange',4:'blue',8:'#DC143C',16:'#DA70D6',32:'#BA55D3',64:'#483D8B',128:'#1E90FF',256:'#00FFFF',512:'#7FFFAA',1024:'#F5F5DC',2048:'#BDB76B'}
valueDict = {0,2,4,8,16,32,64,128,256,512,1024,2048}
rValue =[2,2,2,4]


class Board(object):
    def __init__(self,f,cv):
        global valueDict
        self.boxes = [[0 for i in range(4)] for j in range(4)]
        for i in range(4):
            for j in range(4):
                b = Box(0,'white',10+j*100,10+i*100,90,f,cv)
                self.boxes[i][j] = b
        m = random.randint(0,3)
        n = random.randint(0,3)
        m2 = random.randint(0,3)
        n2 = random.randint(0,3)
        m3 = random.randint(0,3)
        n3 = random.randint(0,3)
        self.isMoveFlag = False
        self.isFullFlag = False
        self.boxes[m][n].setValue(rValue[m3])
        self.boxes[m2][n2].setValue(rValue[n3])

    def paint(self):
        for i in range(4):
            for j in range(4):
                self.boxes[i][j].paint()

    def movebox(self):
        self.isMoveFlag = False
        for i in range(4):
            for j in range(4):
                b = self.boxes[i][j]
                v = b.getValue()
                if b.getValue() !=0:
                    index = j-1;
                    while index > -1:
                        temp = self.boxes[i][index]
                        if temp.getValue() != 0:
                            if temp.getValue() == v:
                                self.isMoveFlag = True
                                temp.setValue(2*v)
                                b.setValue(0)
                            break;
                        else:
                            self.isMoveFlag = True
                            temp.setValue(v)
                            b.setValue(0)
                            b = temp
                            index = index -1

    def genbox(self):
        i = random.randint(0, 3)
        blankBoxNum = 0
        v = rValue[i]
        self.isFullFlag = True
        for i in range(4):
            for j in range(4):
                if self.boxes[i][j].getValue() == 0:
                    blankBoxNum = blankBoxNum+1
                    self.isFullFlag = False
        if (not self.isFullFlag) and self.isMoveFlag:
            while(True):
                m = random.randint(0, 3)
                n = random.randint(0, 3)
                if self.boxes[m][n].getValue() == 0:
                    self.boxes[m][n].setValue(v)
                    blankBoxNum = blankBoxNum - 1
                    if blankBoxNum == 0:
                        self.isFullFlag = True
                    break

    def isGameOver(self):
        if not self.isFullFlag:
            return False

        isGameOverFlag = True
        for i in range(4):
            for j in range(3):
                if self.boxes[i][j].getValue() == self.boxes[i][j+1].getValue():
                    isGameOverFlag = False
        self.rotate()
        for i in range(4):
            for j in range(3):
                if self.boxes[i][j].getValue() == self.boxes[i][j+1].getValue():
                    isGameOverFlag = False
        self.rotate()
        self.rotate()
        self.rotate()
        return isGameOverFlag

    """
    逆时针旋转90度
    """
    def rotate(self):
        temp = [[0 for i in range(4)] for j in range(4)]
        for i in range(4):
            for j in range(4):
               temp[3-j][i]= self.boxes[i][j]
        self.boxes = temp


class Box:
    def __init__(self,value,color,x,y,size,font,cv):
        self.value = value
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.font = font
        self.cv = cv

    def setValue(self,value):
        self.value = value

    def getValue(self):
        return self.value

    def round_rectangle(self,x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1 + radius, y1,
                  x1 + radius, y1,
                  x2 - radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1 + radius,
                  x1, y1]

        return self.cv.create_polygon(points, **kwargs, smooth=True)

    def paint(self):
        self.color = dict[self.value]
        self.round_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, width=1, fill=self.color)
        if self.value != 0 :
            self.cv.create_text(self.x + self.size / 2 - 5, self.y + self.size / 2 - 5, text=self.value, font=self.font)


def run():
    root = tkinter.Tk()
    root.title('2048')
    # 获取屏幕 宽、高
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (420/ 2)
    y = (hs / 2) - (420/ 2)
    root.geometry('%dx%d+%d+%d' % (410, 410, x, y))
    cv = tkinter.Canvas(root,width=410,heigh=410,bg='pink')

    def left(event):
        board.movebox()
        board.genbox()
        board.paint()
        if board.isGameOver():
            msgbox.showinfo('失败','Game Over !')

    def right(event):
        board.rotate()
        board.rotate()
        board.movebox()
        board.rotate()
        board.rotate()
        board.genbox()
        board.paint()
        if board.isGameOver():
            msgbox.showinfo('失败','Game Over !')

    def up(event):
        board.rotate()
        board.movebox()
        board.rotate()
        board.rotate()
        board.rotate()
        board.genbox()
        board.paint()
        if board.isGameOver():
            msgbox.showinfo('失败','Game Over !')

    def down(event):
        board.rotate()
        board.rotate()
        board.rotate()
        board.movebox()
        board.rotate()
        board.genbox()
        board.paint()
        if board.isGameOver():
            msgbox.showinfo('失败','Game Over !')

    root.bind('<Left>',left)
    root.bind('<Right>', right)
    root.bind('<Up>', up)
    root.bind('<Down>', down)

    f = tkinter.font.Font(size=20, weight='bold')
    board = Board(f,cv)
    board.paint()
    cv.pack()
    root.mainloop()
if __name__=='__main__':
    run()