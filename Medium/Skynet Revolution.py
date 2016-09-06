#coding=utf8

import sys
import math


#思路：优先删除临近出口坐标，如没有的到达，随机删除包含出口坐标

n, l, e = [int(i) for i in raw_input().split()]
links = []
gateway = []
for i in xrange(l):
    n1, n2 = [int(j) for j in raw_input().split()]
    links.append({n1, n2})
for i in xrange(e):
    ei = int(raw_input())
    gateway.append(ei)

# game loop

while True:
    si = int(raw_input())
    nextLink = [{si, gateway[i]} for i in range(len(gateway))]
    i = 0
    #删除临近
    for nextL in nextLink:
        if nextL in links:
            i = 1
            print nextL.pop(), nextL.pop()
            break

    #随机删除包含出门坐标
    while i == 0:
        for gate in gateway:
            for line in links:
                if gate in line:
                    print line.pop(), line.pop()
                    i = 1
                    break
            if i == 1:
                break


