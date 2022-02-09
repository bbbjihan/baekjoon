import sys;rl=sys.stdin.readline
import heapq

T = int(rl())

for _ in range(T):
    k = int(rl())
    deleted = [False for _ in range(k)]
    maxheap,minheap = [],[]

    for key in range(k):
        oper = rl().split()
        if oper[0] == 'I':
            heapq.heappush(minheap,(int(oper[1]),key))
            heapq.heappush(maxheap,(-int(oper[1]),key))
            deleted[key] = True
        elif oper[1] == '1':
            while len(maxheap) != 0 and not deleted[maxheap[0][1]]:
                heapq.heappop(maxheap)
            if len(maxheap) == 0:
                continue
            deleted[maxheap[0][1]] = False
            heapq.heappop(maxheap)
        else:
            while len(minheap) != 0 and not deleted[minheap[0][1]]:
                heapq.heappop(minheap)
            if len(minheap) == 0:
                continue
            deleted[minheap[0][1]] = False
            heapq.heappop(minheap)
    
    while len(maxheap) != 0 and not deleted[maxheap[0][1]]:
        heapq.heappop(maxheap) 
    while len(minheap) != 0 and not deleted[minheap[0][1]]:
        heapq.heappop(minheap)
    
    if len(maxheap) != 0 and len(minheap) != 0:
        print(-maxheap[0][0],minheap[0][0])
    else:
        print('EMPTY')