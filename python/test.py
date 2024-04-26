import sys;rl=sys.stdin.readline
from collections import deque

N = int(rl())

isWall = []
for _ in range(N):
  isWall.append(list(map(int, rl().split())))

pathCounts = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

pathCounts[0][1] = [1, 0, 0] #Horizontal, Vertical, Crossed

for i in range(N):
  for j in range(N):
    if (i == 0 and j == 1) or isWall[i][j]:
      continue
    nowCount = [0, 0, 0]
    
    if j > 0:
      nowCount[0] += pathCounts[i][j-1][0]
      nowCount[0] += pathCounts[i][j-1][2]
    
    if i > 0:
      nowCount[1] += pathCounts[i-1][j][1]
      nowCount[1] += pathCounts[i-1][j][2]
    
    if i > 0 and j > 0 and not isWall[i-1][j] and not isWall[i][j-1]:
      nowCount[2] += sum(pathCounts[i-1][j-1])
    
    pathCounts[i][j] = nowCount

print(sum(pathCounts[N-1][N-1]))