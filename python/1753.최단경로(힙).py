import heapq
import sys;rl=sys.stdin.readline

V,E = map(int,rl().split())
K = int(rl())

lines = [[] for _ in range(V)]
for _ in range(E):
    u,v,x = map(int,rl().split())
    lines[u-1].append((x,v))

ans = [float('inf') for _ in range(V)]
ans[K-1] = 0
heap = []
heapq.heappush(heap,(0,K))
while heap:
    cost, target = heapq.heappop(heap)
    if cost == ans[target-1]:
        for node in lines[target-1]:
            if node[0]+cost < ans[node[1]-1]:
                ans[node[1]-1] = node[0]+cost
                heapq.heappush(heap,(ans[node[1]-1],node[1]))

for i in ans:
    if i == float('inf'):
        print("INF")
    else:
        print(i)