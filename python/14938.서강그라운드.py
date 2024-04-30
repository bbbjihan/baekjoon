import sys;rl=sys.stdin.readline
import math

n,m,r = map(int,rl().split())
points = list(map(int,rl().split()))
matrix = [[0 if i == j else math.inf for i in range(n+1)] for j in range(n+1)]

for _ in range(r):
  a, b, dist = map(int,rl().split())
  matrix[a][b] = dist
  matrix[b][a] = dist

for k in range(n + 1):
  for i in range(n + 1):
    for j in range(n + 1):
      matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

res = 0
for i in range(1, n+1):
  S = 0
  for j in range(1, n+1):
    if matrix[i][j] <= m:
      S += points[j - 1]
  res = max(res, S)

print(res)