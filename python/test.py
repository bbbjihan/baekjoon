import sys;rl=sys.stdin.readline
from collections import deque

def outOfMap(position):
  return position > N - 1 or position < 0

N = int(rl())

isWall = []
for _ in range(N):
  isWall.append(list(map(bool, rl().split())))

print(isWall)

matrix = []
for _ in range(N):
  matrix.append(list(map(int, rl().split())))

dq = deque([[1, 0, "H"]])
result = 0
while dq:
  nowX, nowY, nowStatus = dq.popleft()
  nowPosition = [nowX, nowY]
  
  if nowX == nowY == N -1:
    result += 1
    continue
  
  if nowStatus == "H":
    if outOfMap(nowX + 1) or matrix[nowY][nowX + 1] == 1:
      continue
    dq.append([nowX + 1, nowY, "H"])
    if outOfMap(nowY + 1) or matrix[nowY + 1][nowX] == 1 or matrix[nowY + 1][nowX + 1] == 1:
      continue
    dq.append([nowX + 1, nowY + 1, "C"])
  elif nowStatus == "V":
    if outOfMap(nowY + 1) or matrix[nowY + 1][nowX] == 1:
      continue
    dq.append([nowX, nowY + 1, "V"])
    if outOfMap(nowX + 1) or matrix[nowY][nowX + 1] == 1 or matrix[nowY + 1][nowX + 1] == 1:
      continue
    dq.append([nowX + 1, nowY + 1, "C"])
  else:
    canGoRight = not outOfMap(nowX + 1) and matrix[nowY][nowX + 1] == 0
    canGoDown = not outOfMap(nowY + 1) and matrix[nowY + 1][nowX] == 0
    if canGoRight:
      dq.append([nowX + 1, nowY, "H"])
    if canGoDown:
      dq.append([nowX, nowY + 1, "V"])
    if canGoRight and canGoDown and not outOfMap(nowX + 1) and not outOfMap(nowY + 1) and matrix[nowY + 1][nowX + 1] == 0:
      dq.append([nowX + 1, nowY + 1, "C"])

print(result)