import sys;rl=sys.stdin.readline
import heapq
import math

N, M, X = map(int,rl().split())
vertexes = [[] for _ in range(N + 1)]
for i in range(M):
  a,b, dist = map(int,rl().split())
  vertexes[a].append([b, dist])

def dijkstra(start, end):
  dists = [math.inf for _ in range(N + 1)]
  dists[start] = 0
  
  q = []
  heapq.heappush(q, [0, start])
  while q:
    dist, now = heapq.heappop(q)
    
    if dists[now] < dist:
      continue
    
    for next, distNext in vertexes[now]:
      if  dists[next] > dists[now] + distNext:
        dists[next] = dists[now] + distNext
        heapq.heappush(q, [dists[now] + distNext, next])
  
  if end == -1:
    return dists
  else:
    return dists[end]

goHome = dijkstra(X, -1)

res = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
  res[i] += dijkstra(i, X) + goHome[i]

print(max(res[1:]))