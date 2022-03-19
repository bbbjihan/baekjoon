import sys;rl=sys.stdin.readline

T = int(rl())
dp = [1,]
for i in range(1,31):
    dp.append(dp[i-1]*i)
for _ in range(T):
    a,b = map(int,rl().split())
    print((dp[b]//(dp[a]*dp[b-a])))