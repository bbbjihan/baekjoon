import sys;rl=sys.stdin.readline

N = int(rl())
lines = [list(map(int,rl().split()))for _ in range(N)]
lines.sort()
dp = [0 for _ in range(N)]
for i in range(N):
    Max = 0
    valueI = lines[i][1]
    for j in range(i):
        valueJ = lines[j][1]
        if valueJ < valueI and dp[j] > Max:
            Max = dp[j]
    dp[i] = Max + 1

print(N-(max(dp)))