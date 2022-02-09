import sys
from collections import deque

N,M = list(map(int,sys.stdin.readline().split()))
g_friend = [[]for _ in range(N)]
field = [[6 for _ in range(N)]for _ in range(N)]

for _ in range(M):
    a,b = list(map(int,sys.stdin.readline().split()))
    g_friend[a-1].append(b)
    g_friend[b-1].append(a)

def sol(breadth,friend):
    if breadth == 6:
        return
    tmp_li = [[] for _ in range(N)]

    for i in range(N):
        for j in range(len(friend[i])):
            tmp_li[i]+=friend[friend[i][j]-1]
    
    for i in range(N):
        for j in range(len(tmp_li[i])):
            field[i][tmp_li[i][j]-1] = min(field[i][tmp_li[i][j]-1],breadth)
    tmp_li = list(map(lambda x:list(set(x)),tmp_li))
    #print(tmp_li)

    sol(breadth+1,tmp_li)

#print(g_friend)
sol(2,g_friend)

for i in range(N):
    for j in range(len(g_friend[i])):
        field[i][g_friend[i][j]-1] = 1
#print(field)
ans = 0
min = 600
for i in range(N):
    if sum(field[i])<min:
        min = sum(field[i])
        ans = i+1

print(ans)