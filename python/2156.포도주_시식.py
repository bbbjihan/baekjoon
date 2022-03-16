import sys;rl=sys.stdin.readline

N = int(rl())
wine = [int(rl()) for _ in range(N)]
dp = [[0,0] for _ in range(N)]
# 0번째 원소 -> 이전 잔을 마시지 않은 경우
# 1번째 원소 -> 이전 잔을 마신 경우
dp[0] = [wine[0],wine[0]]

if N == 1:
    print(wine[0])
else:
    dp[1] = [wine[1],wine[0]+wine[1]]
    Max = max(dp[0]+dp[1])
    for i in range(2,N):
        dp[i] = [max(dp[i-2]+dp[i-3])+wine[i],dp[i-1][0]+wine[i]]
        Max = max(Max,dp[i][0],dp[i][1])
    print(Max)