import sys;rl=sys.stdin.readline
import math
from collections import deque

N, M, X, Y = map(int,rl().split())

edges = [ [] for _ in range(N + 1) ]
indegrees = [ 0 for _ in range(N + 1) ]
minTurn = [ 0 for _ in range(N + 1)]
successValues = [(-1, -1)]

dq = deque([])
sortedCustomers = []

for _ in range(M):
  start, end = list(map(int,rl().split()))
  indegrees[end] += 1
  edges[start].append(end)

for _ in range(N):
  successValues.append(list(map(int,rl().split())))

for vertex in range(1, N + 1):
  if indegrees[vertex] == 0:
    dq.append(vertex)

while dq:
  now = dq.popleft()
  sortedCustomers.append(now)
  for next in edges[now]:
    indegrees[next] -= 1
    minTurn[next] += 1
    if indegrees[next] == 0:
      dq.append(next)

if len(sortedCustomers) != N:
  print(-1)
else:
  dp = [[[math.inf for _ in range(Y + 1)] for _ in range(X + 1)] for _ in range(N)]

  for i in range(N):
    xAmount, yAmount = successValues[sortedCustomers[i]]
    for xNeed in range(X + 1):
      for yNeed in range(Y + 1):
        if xNeed <= xAmount and yNeed <= yAmount:
          dp[i][xNeed][yNeed] = 1
          continue
        
        if i > 0:
          dp[i][xNeed][yNeed] = min(
            dp[i-1][xNeed][yNeed],
            dp[i-1][1 if xNeed < xAmount else xNeed-xAmount][1 if yNeed < yAmount else yNeed-yAmount] + 1
            )

  minCustomerCnt = math.inf
  lastCustomerCandidate = -1
  for i in range(N):
    cnt = dp[i][X][Y]
    if minCustomerCnt > cnt:
      minCustomerCnt = cnt
      lastCustomerCandidate = i

  if minCustomerCnt == math.inf:
    print(-1)
  else:
    print(minCustomerCnt)
    print(sortedCustomers[lastCustomerCandidate])