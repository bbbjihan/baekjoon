import sys;rl=sys.stdin.readline
N,M=map(int,rl().split())
print(320 if (12<=N<=16) and M == 0 else 280)