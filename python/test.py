import sys;rl=sys.stdin.readline

N,M = map(int,rl().split())
a = list(map(int,rl().split()))
Sumlist = [0]
for i in range(1,N+1):
    Sumlist.append(a[i-1] + Sumlist[-1])

for _ in range(M):
    i,j = map(int,rl().split())
    print(Sumlist[j] - Sumlist[i-1])