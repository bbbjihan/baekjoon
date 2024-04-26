import sys;rl=sys.stdin.readline
import heapq
import math

N,E = map(int, rl().split())

vertexes = [[] for _ in range(N + 1)]
for _ in range(E):
  a,b,c = map(int, rl().split())
  vertexes[a].append([b,c])
  vertexes[b].append([a,c])

v1, v2 = map(int,rl().split())

def dijkstra(v1, v2):
  dist = [math.inf for _ in range(N + 1)]
  dist[v1] = 0
  queue = []
  heapq.heappush(queue, [0, v1])
  
  while queue:
    distNow, vertexNow = heapq.heappop(queue)
    
    if dist[vertexNow] < distNow:
      continue
    
    for vertexNext, distNext in vertexes[vertexNow]:
      tmp = distNext + distNow
      if dist[vertexNext] > tmp:
        dist[vertexNext] = tmp
        heapq.heappush(queue, [tmp, vertexNext])
  
  return dist[v2]

res = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N),
          dijkstra(1, v2) + dijkstra(v1, v2) + dijkstra(v1, N))
print(res if res != math.inf else -1)