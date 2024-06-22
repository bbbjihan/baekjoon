import sys;rl=sys.stdin.readline
import itertools

N = int(rl())
petals = list(map(int,rl().split()))

ans = 0
for i in range(N):
    for j in range(i + 1, N + 1):
        now = petals[i:j]
        if (sum(now) / len(now)) in now:
            ans += 1

print(ans)