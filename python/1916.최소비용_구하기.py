import heapq
import sys;rl=sys.stdin.readline

N = int(rl())
M = int(rl())
lines = [[] for _ in range(N)]
for _ in range(M):
  a,b,c = map(int,rl().split())
  lines[a-1].append((c,b))
start,end = map(int,rl().split())

start_cost = [float('inf') for _ in range(N)]
start_cost[start-1] = 0

heap = []
heapq.heappush(heap,(0,start))
while heap:
  cost, target = heapq.heappop(heap)
  if start_cost[target-1] == cost:
    for node in lines[target-1]:
      if node[0]+cost < start_cost[node[1]-1]:
        start_cost[node[1]-1] = node[0]+cost
        heapq.heappush(heap,(start_cost[node[1]-1],node[1]))
print(start_cost[end-1])