import sys
import math


road = int(raw_input())
gap = int(raw_input())
platform = int(raw_input())

while 1:
    speed = int(raw_input())
    coord_x = int(raw_input())

    if coord_x > road:
        print "SLOW"
    elif coord_x + speed > road:
        print "JUMP"
    else:
        if speed <= gap:
            print "SPEED"
        elif speed > gap + 1:
            print "SLOW"
        else:
            print "WAIT"
