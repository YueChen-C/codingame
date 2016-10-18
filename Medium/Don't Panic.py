import sys
import math

q,w,e,r, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in raw_input().split()]

floorTarget = [0 for i in range(q)]
floorProcessed = [False for i in range(q)]
for i in xrange(nb_elevators):
     # elevator_floor: floor on which this elevator is found
     # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in raw_input().split()]
    floorTarget[elevator_floor] = elevator_pos

floorTarget[r] = exit_pos


while 1:
    clone_floor, clone_pos, direction = raw_input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    if(clone_floor < 0 or clone_pos < 0 or direction == 'NONE' or floorProcessed[clone_floor]):
        print "WAIT"
    elif(clone_pos > floorTarget[clone_floor] and direction == 'RIGHT'):
        print "BLOCK"
        floorProcessed[clone_floor] = True
    elif(clone_pos < floorTarget[clone_floor] and direction == 'LEFT'):
        print "BLOCK"
        floorProcessed[clone_floor] = True
    else:print "WAIT"