import sys
import math,copy
text=['####', '#OO#', '#OO#', '####']
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


maps1=[]
for i in xrange(len(text)):
    row = text[i]
    print row
    for v in range(len(row)):
        if row[v]=='O':
            maps1.append((v,i))



text=[(0, 0), (1, 1), (2, 1), (3, 3), (1, 2)]


for i in text:
    maps=copy.copy(maps1)
    num=0
    goover=[]
    x, y = i[0],i[1]
    if (x,y) not in maps:
        print 0
        continue
    goover.append((x,y))
    while len(goover)!=0:
        x=goover[0][0]
        y=goover[0][1]
        goover.pop(0)
        if (x-1,y) in maps:
            maps.remove((x-1,y))
            num+=1
            goover.append((x-1,y))
        if (x+1,y) in maps:
            maps.remove((x+1,y))
            num+=1
            goover.append((x+1,y))
        if (x,y-1) in maps:
            maps.remove((x,y-1))
            num+=1
            goover.append((x,y-1))
        if (x,y+1) in maps:
            maps.remove((x,y+1))
            num+=1
            goover.append((x,y+1))

    print num







