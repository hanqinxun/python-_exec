#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'通讯录'
__author__ = 'han qinxun'
import os
import sqlite3


def opendb():
    conn = sqlite3.connect('/Users/hanqinxun/contacts.db')
    cur = conn.execute("create table if not exists contacts(id integer primary key,"
                       "username varchar(128), passwd varchar(64), address varchar(128),"
                       "phone varchar(32))")
    return conn,cur


def info():
    id = input('请输入学号：')
    username = input('请输入姓名：')
    passwd = input('请输入密码：')
    address = input('请输入地址：')
    phone = input('请输入电话：')
    return id, username,passwd,address,phone


def addContacts():
    person = info()
    v = opendb()
    v[1].execute("insert into contacts(id,username,passwd,address,phone) values (?,?,?,?,?)",(person[0],person[1],person[2],person[3],person[4]))
    v[0].commit()
    print("--------------添加数据成功-----------------")
    v[0].close()


def queryall():
    v = opendb()
    v[1].execute("select id,username,passwd,address,phone from contacts")
    res = v[1].fetchall()
    for line in res:
        print(line)


def delContacts():
    welcome = '----------------欢迎使用删除数据库功能 ---------'
    print(welcome)
    delchoice=input('请输入要删除的学号: ')
    v=opendb()
    v[1].execute("delete from contacts where id =",+delchoice)
    v[0].commit()
    print('-------------------删除数据成功--------------------')
    queryall()
    v[0].close()



def updateContacts():
    welcome='-------------------欢迎使用修改数据功能-----------------'
    print(welcome)
    changechoice=input('请输入想要修改的学生的学号:')
    v=opendb()
    person=info()
    v[1].execute("update contacts set id=?,username=?,passwd=?,address=?,phone=? where id=" +changechoice,(person[0],person[1],person[2],person[3],person[4]))
    v[0].commit()
    queryall()
    v[0].close()
    

def welcome():
    flag = True
    while flag:
        welcome ='------------欢迎使用通讯录管理系统-----------\n'
        print(welcome)
        show="""
        （1 添加）往数据库里面添加内容
        （2 删除〉删除数据库中内容
        （3 修改）修改数据库的内容
        （4 查询）查询数据库的内容
        （0 退出）
         选择您想要进行的操作：
        """
        print(show)
        choice = input("请输入你的选择：")
        if choice == '1':
            addContacts()
        elif choice =='2':
            delContacts()
        elif choice =='3':
            updateContacts()
        elif choice =='4':
            queryall()
        elif choice == '0':
            break
        else:
            print('错误的命令！')

if __name__=='__main__':
    welcome()