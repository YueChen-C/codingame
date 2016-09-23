n=int(raw_input())
q = raw_input()
l,p=map(int,q.split( )),[]
k=sorted(map(abs,l))
for i in range(n):
    if abs(l[i])==k[0]:p.append(l[i])
if p:print max(p)
else:print 0