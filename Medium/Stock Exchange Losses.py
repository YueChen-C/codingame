import sys
import math


n = int(raw_input())
list=[]
for i in raw_input().split():
    v = int(i)
    list.append(v)
max_loss = 0
max_num = 0

for i in range(n):
    if int(list[i]) > max_num:
        max_num = int(list[i])
    loss = int(list[i]) - max_num
    if loss < max_loss:
        max_loss = loss
print max_loss
