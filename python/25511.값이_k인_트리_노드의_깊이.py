import sys;rl=sys.stdin.readline
from collections import deque

n, k = map(int,rl().split())

childrens = [[] for _ in range(n)]
for _ in range(n - 1):
    p, c = map(int,rl().split())
    childrens[p].append(c)
numbers = list(map(int,rl().split()))

dq = deque([(0, 0)])
while dq:
    now, depth = dq.popleft()
    if numbers[now] == k:
        print(depth)
        break
    for child in childrens[now]:
        dq.append((child, depth + 1))