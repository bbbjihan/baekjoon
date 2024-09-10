import sys;rl=sys.stdin.readline
N = int(rl())
a = 0
for _ in range(N):
    d = int(rl().strip().split('D-')[1])
    if d < 91:
        a += 1

print(a)