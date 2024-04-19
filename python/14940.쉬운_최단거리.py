import sys;rl=sys.stdin.readline
from collections import deque
import math

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = list(map(int,rl().split(' ')))

field = []
visited = [[False for _ in range(m)] for _ in range(n)]
result = [[math.inf for _ in range(m)] for _ in range(n)]
dq = deque([])
for i in range(n):
  line = list(map(int,rl().split(' ')))
  field.append(line)
  if 2 in line:
    dq.append([i, line.index(2), 0])
    line[line.index(2)] = 1

while(len(dq) > 0):
  y, x, dist = dq.popleft()
  if y < 0 or y > n - 1 or x < 0 or x > m - 1 or field[y][x] == 0 or visited[y][x]:
    continue
  visited[y][x] = True
  result[y][x] = min(result[y][x], dist)
  for i in range(4):
    dq.append([y + dy[i], x + dx[i], dist + 1])

for i in range(n):
  for j in range(m):
    if visited[i][j] == False or result[i][j] == math.inf:
      result[i][j] = -1
    if field[i][j] == 0:
      result[i][j] = 0

for i in range(n):
  print(*result[i])