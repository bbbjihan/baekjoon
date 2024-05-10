import sys;rl=sys.stdin.readline
import copy
import math

N = int(rl())
costs = []

for _ in range(N):
  costs.append(list(map(int,rl().split())))

ans = math.inf
for startColor in range(3):
  costForDP = copy.deepcopy(costs)
  dp = [[0,0,0] for _ in range(N)]
  costForDP[0] = [math.inf for _ in range(3)]
  costForDP[0][startColor] = costs[0][startColor]

  for i in range(N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costForDP[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costForDP[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + costForDP[i][2]
  
  dp[N-1][startColor] = math.inf
  ans = min(*dp[N-1], ans)

print(ans)