import sys;rl=sys.stdin.readline

N, K = map(int,rl().split())
INF = int(1e9)
field = [[INF for _ in range(N)] for _ in range(N)]

for _ in range(K):
    start, desti = map(int,rl().split())
    field[start-1][desti-1] = 1
    field[desti-1][start-1] = 1
for i in range(N):
    field[i][i] = 0

for k in range(N):
    for i in range(N):
        if i == k : continue
        for j in range(N):
            if i == j or j == k : continue
            cost = field[i][k] + field[k][j]
            if cost < field[i][j]:
                field[i][j] = cost

flag = 0
for i in range(N):
    for j in range(N):
        if field[i][j] > 6:
            flag = 1
            break

if flag:
    print("Big World!")
else:
    print("Small World!")
    