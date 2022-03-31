import sys;rl=sys.stdin.readline

N,M = map(int,rl().split())
matrixA = []
for _ in range(N):
    matrixA.append(list(map(int,rl().split())))
M,K = map(int,rl().split())
matrixB = []
for _ in range(M):
    matrixB.append(list(map(int,rl().split())))

matrixC = [[0 for _ in range(K)]for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            matrixC[n][k]+=(matrixA[n][m]*matrixB[m][k])

for i in range(N):
    print(*matrixC[i])