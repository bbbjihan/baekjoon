import sys;rl=sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N,M = list(map(int,rl().split(' ')))

map = []
dq = deque()
for i in range(N):
  line = list(rl())
  for j in range(M):
    if line[j] == 'I':
      dq.append([i, j])
      line[j] == 'O'
  map.append(line)

meet = 0
visited = [[False for _ in range(M)] for _ in range(N)]
while(len(dq) > 0):
  y, x = dq.popleft()
  if y < 0 or x < 0 or y > N - 1 or x > M - 1 or map[y][x] == 'X' or visited[y][x]:
    continue
  visited[y][x] = True
  if map[y][x] == 'P':
    meet+=1
  for i in range(4):
    dq.append([y + dy[i], x + dx[i]])
    
if meet == 0:
  print('TT')
else:
  print(meet)