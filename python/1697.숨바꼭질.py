import sys
from collections import deque

N,M = list(map(int,sys.stdin.readline().split()))

queue = deque()
queue.append([N,0])
visited = [False for _ in range(200000)]

while queue:
    tmp = queue.popleft()
    if tmp[0] == M:
        break
    if tmp[0]>=0 and tmp[0]<=100000:
        if visited[tmp[0]] == False:
            visited[tmp[0]] = True
            queue.append([tmp[0]*2,tmp[1]+1])
            queue.append([tmp[0]+1,tmp[1]+1])
            queue.append([tmp[0]-1,tmp[1]+1])

print(tmp[1])