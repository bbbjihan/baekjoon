import sys;rl=sys.stdin.readline
import math
import heapq

n = int(rl())
m = int(rl())

vertexes = [[] for _ in range(n + 1)]

for _ in range(m):
  start, end, dist = map(int,rl().split())
  vertexes[start].append((end,dist))

def dijkstra(start, end):
  dists = [math.inf for _ in range(n + 1)]
  dists[start] = 0
  pre = [0 for _ in range(n + 1)]
  pre[start] = -1
  q = []
  heapq.heappush(q, (0, start))
  
  while q:
    distNow, edgeNow = heapq.heappop(q)
    
    if distNow > dists[edgeNow]:
      continue
    for edgeNext, distNext in vertexes[edgeNow]:
      if dists[edgeNext] > distNext + distNow:
        dists[edgeNext] = distNext + distNow
        pre[edgeNext] = edgeNow
        heapq.heappush(q,(distNext + distNow, edgeNext))
  
  print(dists[end])
  
  now = end
  path = []
  while now != - 1:
    path.append(now)
    now = pre[now]
  print(len(path))
  print(*path[::-1])

start, end = map(int,rl().split())
dijkstra(start,end)