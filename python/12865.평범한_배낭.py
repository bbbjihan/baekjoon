import sys;rl=sys.stdin.readline
#https://claude-u.tistory.com/208

N,K = map(int,rl().split())
weight = [0]
value = [0]
for _ in range(N):
    wei, val = map(int,rl().split())
    weight.append(wei)
    value.append(val)

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for j in range(1,K+1):
    for i in range(1,N+1):
        if j < weight[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],value[i]+dp[i-1][j-weight[i]])

print(dp[N][K])