#coding=utf8
import sys
import math


#思路:先计算x总长，再逐步计算每个y长度
N = int(raw_input())

setX = []
setY = []
for i in xrange(N):
    X, Y = [int(j) for j in raw_input().split()]
    setX.append(X)
    setY.append(Y)

setY.sort()

#y集合点的中间值
if len(setY) % 2 == 1:
    median = setY[(len(setY) - 1)/2]
elif len(setY) % 2 == 0:
    median = (setY[(len(setY))/2 - 1] + setY[len(setY)/2]) / 2

#x总长度
lengthX = max(setX) - min(setX)
distance = lengthX


for i in setY:
    distance += abs(median - i)

print distance








