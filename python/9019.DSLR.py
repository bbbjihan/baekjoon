import sys;rl=sys.stdin.readline
from collections import deque

N = int(rl())

def sol(start,target):
  visited = [False for _ in range(10000)]
  queue = deque()
  queue.append((start,''))
  while queue:
    node = queue.popleft()
    if visited[node[0]] == False:
      if node[0] == target:
        return node[1]
      visited[node[0]] = True
      queue.append(((node[0]*2)%10000,node[1]+'D'))
      if node[0] == 0:
        queue.append((9999,node[1]+'S'))
      else:
        queue.append((node[0]-1,node[1]+'S'))
      if node[0] > 999:
        queue.append(((node[0]*10)%10000+node[0]//1000, node[1]+'L'))
      else:
        queue.append((node[0]*10,node[1]+'L'))
      queue.append(((node[0]%10)*1000+node[0]//10, node[1]+'R'))
      

for _ in range(N):
  start, target = map(int,rl().split())
  print(sol(start,target))