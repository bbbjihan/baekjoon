import sys;rl=sys.stdin.readline
N = int(rl())
costs = []

for _ in range(N):
  costs.append(list(map(int,rl().split())))

dp = [[0,0,0] for _ in range(N)]
path = [[0,0,0]for _ in range(N)]
path[0] = [-1, -1, -1]
dp[0] = costs[0]

for i in range(1, N - 1):
  if dp[i-1][1] < dp[i-1][2]:
    dp[i][0] = dp[i-1][1] + costs[i][0]
    path[i][0] = 1
  else:
    dp[i][0] = dp[i-1][2] + costs[i][0]
    path[i][0] = 2
    
  if dp[i-1][2] < dp[i-1][0]:
    dp[i][1] = dp[i-1][2] + costs[i][1]
    path[i][1] = 1
  else:
    dp[i][1] = dp[i-1][0] + costs[i][1]
    path[i][1] = 0
    
  if dp[i-1][1] < dp[i-1][0]:
    dp[i][2] = dp[i-1][1] + costs[i][2]
    path[i][2] = 1
  else:
    dp[i][2] = dp[i-1][0] + costs[i][2]
    path[i][2] = 0

startColors = path[N - 2]
for i in range(2, N - 1)[::-1]:
  startColors[0] = path[i - 1][startColors[0]]
  startColors[1] = path[i - 1][startColors[1]]
  startColors[2] = path[i - 1][startColors[2]]

res = [0, 0, 0]

if startColors[0] == 0:
  res[0] = dp[N - 2][0] + min(costs[N - 1][1], costs[N - 1][2])
elif startColors[0] == 1:
  res[0] = dp[N - 2][0] + costs[N - 1][2]
else:
  res[0] = dp[N - 2][0] + costs[N - 1][1]

if startColors[1] == 1:
  res[1] = dp[N - 2][1] + min(costs[N - 1][0], costs[N - 1][2])
elif startColors[1] == 0:
  res[1] = dp[N - 2][1] + costs[N - 1][2]
else:
  res[1] = dp[N - 2][1] + costs[N - 1][0]

if startColors[2] == 2:
  res[2] = dp[N - 2][2] + min(costs[N - 1][0], costs[N - 1][1])
elif startColors[2] == 0:
  res[2] = dp[N - 2][2] + costs[N - 1][1]
else:
  res[2] = dp[N - 2][2] + costs[N - 1][0]

print('costs',costs)
print('path',path)
print('dp',dp)
print('SC', startColors)
print('res',res)
print(min(res))