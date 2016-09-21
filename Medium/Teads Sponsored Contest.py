#coding=utf8
import sys
import math
list1=[(0, 1), (0, 8), (0, 15), (1, 2), (1, 5), (2, 3), (2, 4), (5, 6), (5, 7), (8, 9), (8, 12), (9, 10), (9, 11), (12, 13), (12, 14), (15, 16), (15, 19), (16, 17), (16, 18), (19, 20), (19, 21)]

# 该算法节点过多时不适用（逐一计算每个点出发到结束的长度）
# str1=[]
# graph={}
# for i in list1:
#     str1+=i[0],i[1]
#     graph.setdefault(i[0], list()).append(i[1])
#     graph.setdefault(i[1], list()).append(i[0])
# print graph
#
# class main():
#
#     def __init__(self,list1):
#         self.list1=list1
#         self.num=0
#     def recursion(self,nextlist):
#
#         for i in nextlist:
#             nextlist=list(set(nextlist).union(set(self.list1[i])))
#         self.num+=1
#         if len(nextlist)<len(set(str1)):
#             self.recursion(nextlist)
#         return self.num
#
# main=main(graph)
# minnum=main.recursion([0])
# for i in graph:
#     num= main.recursion([i])
#     if num<=minnum:
#         minnum=num
#     main.num=0
# print minnum







import sys, math

#计算一个单节点到最远单节点距离的平均数
n = int(raw_input()) # the number of adjacency relations
graph = {}
for i in xrange(n):

    xi, yi = [int(j) for j in raw_input().split()]
    graph.setdefault(xi,list()).append(yi)
    graph.setdefault(yi,list()).append(xi)

#print >> sys.stderr, graph
count = 0

for vertice in graph.values():
    if len(vertice) == 1:
        leaf_vertix = graph.keys()[count]
        break
    count += 1

def find_path(graph, start):
    tuple = [start, start, 0]
    stack = []
    stack.append(tuple)
    max_dist = 0
    while len(stack) != 0:

        nextV = stack[len(stack)-1][0]
        parent = stack[len(stack)-1][1]
        distance = stack[len(stack)-1][2]
        stack.pop()
        if distance > max_dist:
            max_dist = distance
        for node in graph[nextV]:
            if node != parent:
                stack.append([node, nextV, distance + 1])



    return max_dist+1



distanta = find_path(graph, leaf_vertix)
print (distanta)/2