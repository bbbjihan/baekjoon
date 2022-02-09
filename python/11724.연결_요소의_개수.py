import sys
from collections import deque

N,M = list(map(int,sys.stdin.readline().split()))
lines = [[]for _ in range(N)]

for _ in range(M):
  a,b = list(map(int,sys.stdin.readline().split()))
  lines[a-1].append(b)
  lines[b-1].append(a)

visited = [False for _ in range(N)]

def sol(key):
    queue = deque()
    queue.append(key)

    while queue:
        tmp = queue.popleft()
        if visited[tmp-1] == False:
            visited[tmp-1] = True
            for node in lines[tmp-1]:
                queue.append(node)

cnt = 0

for i in range(N):
    if visited[i-1] == False:
        sol(i)
        cnt+=1

print(cnt)