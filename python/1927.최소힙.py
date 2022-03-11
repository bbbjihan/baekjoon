import heapq
import sys;rl=sys.stdin.readline
minHeap = []

N = int(rl())
for _ in range(N):
    command = int(rl())
    if command == 0:
        if minHeap:
            print(heapq.heappop(minHeap))
        else:
            print(0)
    else:
        heapq.heappush(minHeap,command)
