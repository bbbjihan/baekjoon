import sys;rl=sys.stdin.readline

N = int(rl())
an = list(map(int,rl().split()))
dp = [0 for _ in range(N)]
dp[0] = an[0]
for i in range(1,N):
    dp[i] = max(an[i],dp[i-1] + an[i])
print(max(dp))