import sys;rl=sys.stdin.readline
from collections import deque

dx, dy = [[-1,1,0,0], [0,0,-1,1]]

N,M = map(int,rl().split())

field = []
visited = [[[False,False] for _ in range(M)] for _ in range(N)]

for _ in range(N):
  field.append(list(rl().strip()))

dq = deque([(0, 0, 1, False)])

res = -1

while dq:
  y, x, dist, broken = dq.popleft()
  
  if visited[y][x][0 if broken else 1]:
    continue
  
  visited[y][x][0 if broken else 1] = True
  
  if field[y][x] == '1' :
    broken = True
  
  if y == N - 1 and x == M - 1:
    res = dist
    break
  
  for i in range(4):
    nxtY = y + dy[i]
    nxtX = x + dx[i]
    if 0 <= nxtY <= N - 1 and 0 <= nxtX <= M - 1:
      if field[nxtY][nxtX] == '1' and broken:
        continue
      dq.append((y + dy[i], x + dx[i], dist + 1, broken))

print(res)