from collections import deque
import sys
rl = sys.stdin.readline
N, M = map(int, rl().split())

queue = deque()
queue.append((N, 0))
flag = 0
while queue:
    value, cnt = queue.popleft()
    if value == M:
        flag = 1
        break
    elif value < M:
        queue.append((value*2, cnt+1))
        queue.append((value*10+1, cnt+1))
if flag == 0:
    print(-1)
else:
    print(cnt+1)
