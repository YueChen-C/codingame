
#coding=utf8
import sys
import math


l = int(raw_input())
h = int(raw_input())
t = raw_input()

for i in range(h):
    row = raw_input()
    text=t.upper()
    Letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ?'
    commont=''
    list={}
    B=0
    for i in range(len(Letter)):
        A=B+l
        A,B=B,A
        list[Letter[i]]=row[A:B]
    for i in text:
        for k in list:
            if k==i:
                commont=commont+list[k]
            elif False == i.isalpha():
                commont=commont+list['?']
                break
    print commont


