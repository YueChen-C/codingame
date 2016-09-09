import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())
c = int(raw_input())
list=[]
for i in xrange(n):
    b = int(raw_input())
    list.append(b)
list.sort()
text=[]

if sum(list)<c:
    print 'IMPOSSIBLE'
else:
    for num in list:
        average =c/n
        if num <=average :
            text.append(num)
            c-=num
            n-=1
        else:
            text.append(average)
            c-=average
            n-=1
for n in text:
    print n

text='1234'

for i in text:
    print i