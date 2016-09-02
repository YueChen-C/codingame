import sys
import math



width = int(raw_input())
height = int(raw_input())
list=[]
portrait=[]
for i in xrange(height):
    line = raw_input()
    transverse=[]
    start = 0
    if '0' in line:
        for c in range(width):
            index = line.find('0', start)
            if index == -1:
                break
            transverse.append((index,i))
            start = index  + 1
        portrait.append(transverse)

porhig=len(portrait)

for k in range(porhig):

    for v in range(len(portrait[k])):
        one=portrait[k][v]
        three=-1,-1
        if portrait[k+1:k+2]==[]:
            three=-1,-1
        else:
            for m in portrait[k+1:porhig]:
                for n in m:
                    if portrait[k][v][0]==n[0]:
                        three=n
                        break_flag = True
                        break
                else:continue
                break
        if portrait[k][v+1:v+2]==[]:
            two=-1,-1
        else:
            two=portrait[k][v+1:v+2][0]
        num=" ".join(map(str,one+two+three))
        print num
