import sys;rl=sys.stdin.readline
import math

N, M, X, Y = map(int,rl().split())

edges = [ [] for _ in range(N + 1) ]
indegrees = [ 0 for _ in range(N + 1) ]
minTurn = [ 0 for _ in range(N + 1)]
successValues = [(-1, -1)]

q = []
sortedCustomers = []

for _ in range(M):
  start, end = list(map(int,rl().split()))
  indegrees[end] += 1
  edges[start].append(end)

for _ in range(N):
  successValues.append(list(map(int,rl().split())))

for vertex in range(1, N + 1):
  if indegrees[vertex] == 0:
    q.append(vertex)

while q:
  now = q.pop(0)
  sortedCustomers.append(now)
  for next in edges[now]:
    indegrees[next] -= 1
    minTurn[next] += 1
    if indegrees[next] == 0:
      q.append(next)

dp = [[[math.inf for _ in range(Y + 1)] for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0

for i in range(1, N + 1):
  x_i, y_i = successValues[i]
  for x in range(X + 1):
    for y in range(Y + 1):
      dp[i][x][y] = min(dp[i][x][y], dp[i-1][x][y])
      print(x_i, y_i)
      if x < x_i or y < y_i:
        continue
      dp[i][x][y] = min(dp[i-1][x][y], dp[i-1][x-x_i][y-y_i] + 1)

print(dp)

if len(sortedCustomers) < N:
  print(-1)
else:
  print(sortedCustomers)

for customer in sortedCustomers:
  print('['+ str(customer)+']' + str(successValues[customer])+', minTurn: ' + str(minTurn[customer]))