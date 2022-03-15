import sys;rl=sys.stdin.readline

N = int(rl())
dp = [0 for _ in range(N)]
dp[0:2] = [1,2]

for i in range(2,N):
    dp[i] = (dp[i-2] + dp[i-1])%15746

print(dp[N-1])