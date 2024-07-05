import sys;rl=sys.stdin.readline
N = int(rl())

for _ in range(N):
    a, b, x = map(int,rl().split())
    print(a * (x - 1) + b)