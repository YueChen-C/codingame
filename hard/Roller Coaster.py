#coding=utf8
L, C, N = [int(i) for i in raw_input().split()]
text = []
idx = 0
memory = {}
for i in xrange(N):
    Pi = int(raw_input())
    text.append(Pi)
num = 0
#遍历满足小于等于L位置作为key，如果超过一轮则直接使用记录值，不在遍历
while C > 0:
    origIdx = idx
    ride = 0
    try:
        num+=memory[idx][0]
        idx = memory[idx][1]
    except KeyError:
        Amount = 0
        while ride+text[idx]<=L:
            ride+=text[idx]
            num+=text[idx]
            Amount+=text[idx]
            idx = int((idx+1)%len(text))
            if idx == origIdx:
                break
        memory[origIdx] = [Amount, idx]
    C-=1
print num