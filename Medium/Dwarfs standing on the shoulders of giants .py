#coding=utf8
import sys
import math

n = int(raw_input())
list = []
for i in xrange(n):
    x, y = [int(j) for j in raw_input().split()]
    list.append((x,y))

str1=()
str2=[]

#递归返回超过两个连接的数组
def recursion(num,str1):
    for i in list:
        if num[1]==i[0]:
            if str1==():
                str1+=(num,i)
                str2.append(str1)
            else:
                if num==str1[-2]:
                    str1=str1[:-2]+(num,i)
                    str2.append(str1)
                else:
                    str1+=(num,i)
                    str2.append(str1)
            recursion(i,str1)
    return str2


for num in list:
    p=recursion(num,str1)

num=2
for i in p:
    text=','.join([','.join(map(str,x)) for x in i])
    if len(set(text.split(',')))>num:
        num=len(set(text.split(',')))
print num