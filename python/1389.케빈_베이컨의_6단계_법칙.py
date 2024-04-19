import sys;rl=sys.stdin.readline
import math

N, M = list(map(int,rl().split(' ')))

relation = []
matrix = [[math.inf if i != j else 0 for i in range(N)] for j in range(N)]
for _ in range(M):
  l = list(map(int, rl().split(' ')))
  relation.append(l)
  matrix[l[0] - 1][l[1] - 1] = 1
  matrix[l[1] - 1][l[0] - 1] = 1
  
for k in range(N):
  for i in range(N):
    for j in range(N):
      if i == j:
        continue
      matrix[i][j] = min(matrix[i][k] + matrix[k][j], matrix[i][j])

sums = [sum(matrix[i]) for i in range(N)]

print(sums.index(min(sums)) + 1)