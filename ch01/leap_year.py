#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 计算闰年 '

__author__ = 'hanqinxun'

import os

def test():
    year = int(input("please input a year:"))
    if( (year % 4 ==0 and year % 100 !=0) or year % 400 ==0):
        print('is leap year')
    else:
        print('is not leap year')

if __name__=='__main__':
    test()