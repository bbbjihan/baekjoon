import sys;rl=sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R,C,T = map(int,rl().split())

room = []
for _ in range(R):
  room.append(list(map(int,rl().split())))

machineTop = 0
machineBotton = 0
for i in range(R):
  if room[i][0] == -1:
    machineTop = i
    machineBottom = i +1
    break

def spread():
  dustDiff = [[0 for _ in range(C)] for _ in range(R)]
  for i in range(R):
    for j in range(C):
      dust = room[i][j]
      if dust > 0:
        cnt = 0
        amountSpread = int(dust / 5)
        for k in range(4):
          y = i + dy[k]
          x = j + dx[k]
          if 0 <= y <= R - 1 and 0 <= x <= C - 1 and room[y][x] != -1:
            cnt += 1
            dustDiff[y][x] += amountSpread
        dustDiff[i][j] = dustDiff[i][j] - (amountSpread * cnt)
  for i in range(R):
    for j in range(C):
      room[i][j] = room[i][j] + dustDiff[i][j]

def purify():
  topY = machineTop
  topX = 0
  bottomY = machineBottom
  bottomX = 0
  topPrev = 0
  bottomPrev = 0
  while topX < C - 1:
    topNow = room[topY][topX]
    bottomNow = room[bottomY][bottomX]
    if topNow != -1:
      room[topY][topX] = topPrev
      topPrev = topNow
    if bottomNow != -1:
      room[bottomY][bottomX] = bottomPrev
      bottomPrev = bottomNow
    topX += 1
    bottomX += 1
    
  while topY > 0:
    topNow = room[topY][topX]
    if topNow != -1:
      room[topY][topX] = topPrev
      topPrev = topNow
    topY -= 1
  
  while bottomY < R - 1:
    bottomNow = room[bottomY][bottomX]
    if bottomNow != -1:
      room[bottomY][bottomX] = bottomPrev
      bottomPrev = bottomNow
    bottomY += 1
  
  while topX > 0:
    topNow = room[topY][topX]
    bottomNow = room[bottomY][bottomX]
    if topNow != -1:
      room[topY][topX] = topPrev
      topPrev = topNow
    if bottomNow != -1:
      room[bottomY][bottomX] = bottomPrev
      bottomPrev = bottomNow
    topX -= 1
    bottomX -= 1
  
  while topY < machineTop:
    topNow = room[topY][topX]
    if topNow != -1:
      room[topY][topX] = topPrev
      topPrev = topNow
    topY += 1
  
  while bottomY > machineBottom:
    bottomNow = room[bottomY][bottomX]
    if bottomNow != -1:
      room[bottomY][bottomX] = bottomPrev
      bottomPrev = bottomNow
    bottomY -= 1

def TIK():
  spread()
  purify()

for _ in range(T):
  TIK()

result = 0
for i in range(R):
  for j in range(C):
    if room[i][j] != -1:
      result += room[i][j]

print(result)