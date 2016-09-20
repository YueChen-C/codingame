#coding=utf8
import sys
import math

w, h = [int(i) for i in raw_input().split()]
n = int(raw_input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in raw_input().split()]

print >> sys.stderr, w, h,n
print >> sys.stderr, x0, y0
stx,sty=0,0
enx,eny=w,h
x,y=0,0
#平均数向上取整
while True:
    bomb_dir = raw_input()
    for i in bomb_dir:
        if i=='L':
            x=x0-math.ceil(abs((x0-stx))/2)
            enx=x0
        elif i=='R':
            x=x0+math.ceil(abs((x0-enx))/2)
            stx=x0
        elif i=='U':
            y=y0-math.ceil(abs((y0-sty))/2)
            eny=y0
        elif i=='D':
            y=y0+math.ceil(abs((y0-eny))/2)
            sty=y0
    x0,y0=x,y
    print int(x),int(y)