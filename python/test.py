import heapq
import sys;rl=sys.stdin.readline

N,M,K,X = map(int,rl().split())
lines = [[]for _ in range(N)]
for _ in range(M):
    start, desti = map(int,rl().split())
    lines[start-1].append(desti)

INF = int(1e9)
disTable = [INF for _ in range(N)]

heap = []
heapq.heappush(heap,(0,X))
while heap:
    dis,des = heapq.heappop(heap)
    if disTable[des-1] < dis:
        continue
    for i in lines[des-1]:
        cost = disTable[des-1]+1
        if cost < disTable[i-1]:
            disTable[i-1] = cost
            heapq.heappush(heap,i)

print(disTable)