import sys
import math


while True:
    mountain=[]
    for i in range(8):
        mountain_h = int(raw_input())
        mountain.append(mountain_h)
    print mountain.index(max(mountain))