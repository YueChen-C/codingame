import sys
import math



message = raw_input()

Binary=''
for i in message:
    if i.isalpha()==True:
        Binary=Binary+bin(ord(i))[2:]
    else:Binary=Binary+'0'+bin(ord(i))[2:]

def encode(Binary,count,text=''):
    if Binary=='1':
        text='0 '+'0'*count
    elif Binary=='0':
        text='00 '+'0'*count
    return text

code,count='',1
for k in range(len(Binary)-1):
    if Binary[k+1]==Binary[k]:
        count+=1
        if k==len(Binary)-2:
            code+=encode(Binary[k],count)+' '
    else:
        if k==len(Binary)-2:
            code+=encode(Binary[k],count)+' '
            code+=encode(Binary[k+1],1)+' '
        else:
            code+=encode(Binary[k],count)+' '
        count=1

print code.strip()
