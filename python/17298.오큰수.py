from collections import deque
import sys;rl=sys.stdin.readline

N = int(rl())
an = list(map(int,rl().split()))
NGE = [-1 for _ in range(N)]
stack = []

for i in range(N):
    now = an[i]
    while stack and stack[-1][0] < now:
        tmp = stack.pop()
        NGE[tmp[1]] = now
    stack.append((now,i))

print(*NGE)