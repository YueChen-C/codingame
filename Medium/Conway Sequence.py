#coding=utf8
import sys
import math

#康威序列
r = int(raw_input())
l = int(raw_input())
str1=[str(r)]
i=1
num=1
member=[]
while i<l:
    for k in range(len(str1)):
        if str1[k:k+1]==str1[k+1:k+2]:
            num+=1
        else:
            member.append(str(num))
            member.append(str1[k:k+1][0])
            num=1
    str1=member
    member=[]
    i+=1


print ' '.join(str1)
