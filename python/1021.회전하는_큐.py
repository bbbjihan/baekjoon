from collections import deque
import sys;rl=sys.stdin.readline

N,M = map(int,rl().split())
targets = list(map(int,rl().split()))

queue = deque(i+1 for i in range(N))
cnt = 0

for target in targets:
    idx = queue.index(target)
    if idx > len(queue)//2:
        while queue[0] != target:
            queue.appendleft(queue.pop())
            cnt+=1
        queue.popleft()
    else:
        while queue[0] != target:
            queue.append(queue.popleft())
            cnt+=1
        queue.popleft()

print(cnt)