import sys;rl=sys.stdin.readline

M, N = map(int,rl().split())

for _ in range(M):
    l = list(rl().strip())
    l.reverse()
    print(''.join(l))