#coding=utf8
import time

# str1=()
# str2=[]
# def recursion(num,str1):
#     for i in list:
#         if num[1]==i[0]:
#             if str1==():
#                 str1+=(num,i)
#                 str2.append(str1)
#             else:
#                 if num==str1[-2]:
#                     str1=str1[:-2]+(num,i)
#                     str2.append(str1)
#                 else:
#                     str1+=(num,i)
#                     str2.append(str1)
#             recursion(i,str1)
#     return str2
#
#
# for num in list:
#     p=recursion(num,str1)
# num=0
# for i in p:
#     text=','.join([','.join(map(str,x)) for x in i])
#     if len(set(text.split(',')))>num:
#         num=len(set(text.split(',')))
# print num
#



n = int(raw_input())
graph = {}
for i in xrange(n):

    x, y = [int(j) for j in raw_input().split()]
    graph.setdefault(str(x), list()).append(str(y))

def find_longest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        longest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_longest_path(graph, node, end, path)
                if newpath:
                    if not longest or len(newpath) > len(longest):
                        longest = newpath
        return longest

lista = []

for i in graph.keys():
    lista.append(i)
for i in graph.values():
    for j in i:
        lista.append(j)

lista = list(set(lista))

output = []
for i in range(len(lista)):
    for j in range(len(lista)):
        if i != j:
            a = lista[i]
            b = lista[j]
            if find_longest_path(graph, a, b) != None:
                output.append(find_longest_path(graph, a, b))
numbers = []
for item in output:
    numbers.append(len(item))

print max(numbers)









