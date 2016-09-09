#coding=utf8

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#电话正序排序，对比前后电话不同的数字加入到字符串中，输出字符串长度
n = int(raw_input())
list=[]
for i in xrange(n):
    telephone = raw_input()
    list.append(telephone)

list.sort()
num=list[0]
longtel=len(list)

for i in range(longtel-1):
    current=len(list[i])
    nextt=len(list[i+1])
    if current>=nextt:
        for j in range(nextt):
            if list[i][j]!=list[i+1][j]:
                num+=list[i+1][j:nextt]
                break
    else:
        if list[i][:current]==list[i+1][:current]:
            num+=list[i+1][current:]
        else:
            for j in range(current):
                if list[i][j]!=list[i+1][j]:
                    num+=list[i+1][j:nextt]
                    break
print len(num)


# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."


# The number of elements (referencing a number) stored in the structure.

