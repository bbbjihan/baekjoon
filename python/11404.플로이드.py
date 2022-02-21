import sys;rl=sys.stdin.readline
n = int(rl())
m = int(rl())
field = [[float('inf')for _ in range(n)]for _ in range(n)]
for i in range(n):
    field[i][i] = 0
for _ in range(m):
    a,b,c = map(int,rl().split())
    field[a-1][b-1] = min(field[a-1][b-1],c)

for i in range(n):
    for j in range(n):
        for k in range(n):
            field[j][k] = min(field[j][k],field[j][i]+field[i][k])

for i in range(n):
    print(' '.join(list(map(str,field[i]))))