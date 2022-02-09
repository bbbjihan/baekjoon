import sys
from collections import deque

N = int(sys.stdin.readline())

lines = [[] for _ in range(N)]
ans = [['0' for _ in range(N)] for _ in range(N)]

for i in range(N):
    tmp = list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        if tmp[j] == 1:
            lines[i].append(j)

def sol(num):
    visited = [False for _ in range(N)]
    connected = []
    queue = deque()
    queue.append(num)
    first_num_flag = 0
    while queue:
        tmp = queue.popleft()
        if visited[tmp] == False:
            visited[tmp] = True
            if first_num_flag == 0 and tmp == num:
                first_num_flag = 1
                visited[tmp] = False
            else:
                connected.append(tmp)
            for x in lines[tmp]:
                queue.append(x)
    return connected

for i in range(N):
    for j in sol(i):
        ans[i][j] = '1'

print('\n'.join(list(map(lambda x:' '.join(x),ans))))