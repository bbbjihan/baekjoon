import sys;rl=sys.stdin.readline

N = int(rl())

matrix = [[0 for _ in range(N)] for _ in range(N)]

for now in range(N-1):
    _ = rl()
    direction = map(int, rl().split())
    for next in direction:
        matrix[now][next - 1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = 1

for i in range(N):
    if matrix[i][i] and matrix[0][i]:
        print('CYCLE')
        break
else:
    print('NO CYCLE')