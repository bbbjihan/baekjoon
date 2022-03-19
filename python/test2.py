from collections import deque
import sys;rl=sys.stdin.readline

ans = deque()
N = int(rl())
an = deque(map(int,rl().split()))

NGE = an.pop()
ans.append(-1)

while an:
    tmp = an.pop()
    if tmp > NGE:
        NGE = tmp
        ans.appendleft(-1)
    else:
        ans.appendleft(NGE)

print(ans)