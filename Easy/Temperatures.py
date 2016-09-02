import sys
import math



n = int(raw_input())
temps = raw_input()



list=map(int,temps.split( ))
list1=sorted(map(abs,list))
p=[]
for i in range(n):
    if abs(list[i])==list1[0]:
        p.append(list[i])
if p:
    print max(p)
else:print 0