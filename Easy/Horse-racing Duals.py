import sys
import math



n = int(raw_input())
list=[]
for i in range(n):
    pi = int(raw_input())
    list.append(pi)
print list
list.sort()
length=len(list)

D=list[0]
for k in range(length-1):
    if list[k+1]-list[k]<D:
        D=list[k+1]-list[k]
print D
