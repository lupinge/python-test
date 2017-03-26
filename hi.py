#!/usr/bin/env python
# -*- coding: utf-8 -*-


# name = raw_input('enter your name: ')
# print 'hi,', name


#循环打印list
# students = ['jiao','du','cheng']
# for name in students:
#     print name




#计算1~100之和
# sum = 0
# for n in range(101):
#     sum+=n
# print '1~100之和', sum



# while循环计算1~100内奇数之和
# sum = 0
# n = 1
# while n<100:
#     sum+=n
#     n+=2
# print '1~100内奇数之和:', sum


#文件读写
# try:
#     f = open('/Users/luping/Desktop/test.txt', 'r')
#     print f.readlines()
# finally:
#     if f:
#         f.close()

#写
# with open('/Users/luping/Desktop/test.txt', 'w') as f:
#     f.write('Hello, world!')

#追加写
# with open('/Users/luping/Desktop/test.txt', 'a') as f:
#     f.write('Hello, world!')




#正则表达式
import re
test = '0318-7609059'
if re.match(r'^\d{3}\-\d{7}$', test):
    print 'ok'
else:
    print 'failed'