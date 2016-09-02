import math


lon = raw_input()
lat = raw_input()
n = int(raw_input())

lon=float(lon.replace(',','.'))
lat=float(lat.replace(',','.'))

list={}
for i in xrange(n):
    defib = raw_input()
    content=defib.split(';')
    name=content[1]
    userlon=float(content[4].replace(',','.'))
    userlat=float(content[5].replace(',','.'))
    x=(lon-userlon)*math.cos((lon+userlon)/2)
    y=(lat-userlat)
    d=((x**2+y**2)**0.5)*6371
    list[name]=d



for i in list:
    if list[i]<=min(list.values()):
        print i
