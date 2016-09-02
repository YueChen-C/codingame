import sys
import math



n = int(raw_input())
q = int(raw_input())
sorts={}
for i in xrange(n):
    ext, mt = raw_input().split()
    sorts[ext.upper()]=mt

for k in xrange(q):
    fname = raw_input()

    if '.' in fname:
        extensions=fname.split('.')[-1].upper()
    else:extensions=None

    if extensions in sorts.keys():
        for v in sorts:
            if v==extensions:
                print sorts[v]
    else:print "UNKNOWN"