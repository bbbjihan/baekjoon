import sys; rl = sys.stdin.readline
n,m = map(int,rl().split())
An = list(map(int,rl().split()))

MST = [None]

for _ in range(m):
    i,j,k = map(int,rl().split())