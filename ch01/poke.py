#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' 打牌 '
__author__ = 'hanqinxun'

import os
import random
class Card(object):
    def __init__(self,color='',num=''):
        self.num=num
        self.color=color
    def print(self):
        str = '%s %s'%(self.color,self.num)
        print(str,end="")



class Hand():
    def __init__(self,name=''):
        self.name=name
        self.cards=[]
    def getCard(self,card):
        self.cards.append(card)
    def print(self):
        print(self.name,':',end="")
        for card in self.cards:
            card.print()
        print('')



class Poke():
    def __init__(self):
        self.cards=[]
    def populate(self):
        nums =['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        colors=['梅','方','红','黑']
        for color in colors:
            for num in nums:
                c=Card(color,num)
                self.cards.append(c)
    def shuffle(self):
        for v in range(100):
            i = random.randint(0, 51)
            j = random.randint(0, 51)
            c = self.cards[i]
            self.cards[i] = self.cards[j]
            self.cards[j] = c
    def dealCard(self):
        return self.cards.pop()
    def clear(self):
        self.cards=[]
    def print(self):
        for card in self.cards:
            card.print()





def test():
    p=Poke()
    p.populate()#新牌
    p.shuffle()
    h1=Hand('牌手 1')
    h2=Hand('牌手 2')
    h3=Hand('牌手 3')
    h4=Hand('牌手 4')
    for i in range(13):
        h1.getCard(p.dealCard())
        h2.getCard(p.dealCard())
        h3.getCard(p.dealCard())
        h4.getCard(p.dealCard())
    h1.print()
    h2.print()
    h3.print()
    h4.print()


if __name__=='__main__':
    test()