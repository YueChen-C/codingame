#coding=utf8
#用最短行编写代码
lx,ly,tx,ty=[int(i) for i in raw_input().split()]
while 1:K,tx,ty=map(lambda (a,b):a+b,zip(("S",0,ty+1)if ty<ly else(("N",0,ty-1)if ly<ty else("",0,ty)),(("E",tx+1,0)if tx<lx else(("W",tx-1,0)if lx<tx else("",tx,0)))));print K,lx,ly,tx,ty



lx,ly,tx,ty=[int(i) for i in raw_input().split()]
while 1:
    if ty<ly:K="S";ty+=1
    elif ly<ty:K="N";ty-=1
    if tx<lx:K+="E";tx+=1
    elif lx<tx:K+="W";tx-=1
    print K,lx,ly,tx,ty

# lx,ly,tx,ty=[int(i) for i in raw_input().split()]
# while 1:
#     K=""
#     if ty<ly:
#         K="S"
#         ty+=1
#     elif ly<ty:
#         K="N"
#         ty-=1
#     if tx<lx:
#         K+="E"
#         tx+=1
#     elif lx<tx:
#         K+="W"
#         tx-=1
#     print K,lx,ly,tx,ty


