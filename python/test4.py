import sys; rl = sys.stdin.readline

N,M = map(int,rl().split())
Arr = [[]for _ in range(N)]
for i in range(N):
    Arr[i] = list(map(int,rl().split()))
ps = [[0 for _ in range(M)]for _ in range(N)]
ps[0][0] = Arr[0][0]

for i in range(1,M):
    ps[0][i] = ps[0][i-1] + Arr[0][i]

for i in range(1,N):
    for j in range(M):
        if j == 0:
            ps[i][j] = Arr[i][j] + ps[i-1][j]
        else:
            ps[i][j] = Arr[i][j] + ps[i][j-1] + ps[i-1][j] - ps[i-1][j-1]

def getSum(y1,x1,y2,x2):
    if y1 == 0 and x1 == 0:
        return ps[y2][x2]
    elif y1 == 0:
        return ps[y2][x2] - ps[y2][x1-1]
    elif x1 == 0:
        return ps[y2][x2] - ps[y1-1][x2]
    else:
        return ps[y2][x2] + ps[y1-1][x1-1] - ps[y1-1][x2] - ps[y2][x1-1]

K = int(rl())
for _ in range(K):
    a,b,c,d = map(int,rl().split())
    print(getSum(a-1,b-1,c-1,d-1))