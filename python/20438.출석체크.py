import sys;rl=sys.stdin.readline
N,K,Q,M = map(int,rl().split())
sleep = [False for _ in range(N+3)]
checked = [False for _ in range(N+3)]
for i in list(map(int,rl().split())):
    sleep[i] = True
for i in list(map(int,rl().split())):
    if not sleep[i]:
        for j in range(i,N+3,i):
            if not sleep[j]:
                checked[j] = True

PS = [0 for _ in range(N+3)]
for i in range(N+3):
    PS[i] = PS[i-1] + checked[i]

for _ in range(M):
    s,e = map(int,rl().split())
    print(e-s+1-PS[e]+PS[s-1])