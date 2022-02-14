from collections import deque
from copy import deepcopy
import sys;rl=sys.stdin.readline
V,E = map(int,rl().split())
K = int(rl())
graph = [[200001 for _ in range(V)] for _ in range(V)]

for _ in range(E):
    a,b,c = map(int,rl().split())
    graph[a-1][b-1] = c

visited = [False for _ in range(V)]
ans = graph[K-1]

def getmin():
    Min = 200001
    idx = -1
    for i in range(V):
        if visited[i] == False and ans[i] < Min:
            Min = ans[i]
            idx = i
    return idx

def dijkstra(start):
    visited[start] = True
    for i in range(V):
        now = getmin()
        visited[now] = True
        for j in range(V):
            if visited[j] == False:
                if graph[now][j]+ans[now] < ans[j]:
                    ans[j] = graph[now][K-1] = graph[now][j]+ans[now]

dijkstra(getmin())

ans[K-1] = 0

for i in ans:
    if i == 200001:
        print('INF')
    else:
        print(i)