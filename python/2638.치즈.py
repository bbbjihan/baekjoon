import sys;rl=sys.stdin.readline
from collections import deque

dx, dy = [[-1,1,0,0], [0,0,-1,1]]

N,M = map(int,rl().split())

externalAir = [[False for _ in range(M)] for _ in range(N)]
field = []

for _ in range(N):
  field.append(list(map(int,rl().split())))

def getIsCheeseExist():
  dq = deque([(0,0)])
  
  while dq:
    y, x = dq.popleft()
    if y < 0 or y > N - 1 or x < 0 or x > M - 1 or externalAir[y][x] or field[y][x] == 1:
      continue
    externalAir[y][x] = True
    for i in range(4):
      dq.append((y + dy[i], x + dx[i]))
  for i in range(N):
    for j in range(M):
      if not externalAir[i][j]:
        return True
  return False

def melt():
  for i in range(N):
    for j in range(M):
      if field[i][j] == 1:
        cnt = 0
        for k in range(4):
          nxtY = i + dy[k]
          nxtX = j + dx[k]
          if 0 <= nxtY <= N - 1 and 0 <= nxtX <= M - 1 and externalAir[nxtY][nxtX]:
            cnt+=1
        if cnt > 1:
          field[i][j] = 0

isCheeseExist = getIsCheeseExist()
cnt = 0
while isCheeseExist:
  melt()
  externalAir = [[False for _ in range(M)] for _ in range(N)]
  cnt += 1
  isCheeseExist = getIsCheeseExist()

print(cnt)