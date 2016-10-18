#coding=utf8
import sys
import math
n = int(input())
text=[]
for i in range(n):
    w = input()
    text.append(w)
letters = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

points={1:"e,a,i,o,n,r,t,l,s,u",2:'d,g',3:'b,c,m,p',4:'f,h,v,w,y',5:'k',6:'j,x',7:'q,z'}

#将letters分解列出
letpoints={}
for i in letters:
    for k in points:
        if i in points[k]:
            letpoints[i]=k

maxnum=0
for word in text:
    jump=True
    for v in set(word):
        if word.count(v)>letters.count(v):
            jump=False
            break
    #如果出现重复字符串，则跳过该单词
    if jump==False:
        jump=True
        continue
    num=0
    for wordstr in word:
        if wordstr not in letpoints.keys():
            num=0
            break
        else:
            for v in letpoints:
                if wordstr==v:
                    num+=letpoints[v]
    if num>maxnum:
        Expected=word
        maxnum=num

print Expected

