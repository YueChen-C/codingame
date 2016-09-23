import sys
import math


n = int(raw_input())
input = raw_input()
text=input.replace(' ','')

num=''
if '-' in text:
    num=text.replace('-','')
    num= "".join((lambda x:(x.sort(),x)[1])(list(num)))
    if '.' in text:
        num=num.replace('.','')
        num='-'+num[:1]+'.'+num[1:]
    else:num='-'+num

    if float(num)==0:
        num=0
else:
    num= "".join((lambda x:(x.sort(reverse=True),x)[1])(list(text)))
    if '.' in text:
        num=num.replace('.','')
        num=num[:-1]+'.'+num[-1:]
        if float(num) ==0:
            num=0
        elif '.0' in num:
            num=num[:num.find('.0')]

print num
