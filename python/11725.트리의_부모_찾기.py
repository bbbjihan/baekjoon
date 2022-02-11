import sys;rl=sys.stdin.readline
from collections import deque
N = int(rl())
nodes = [[]for _ in range(N+1)]
visited  = [False for _ in range(N+1)]
parent = [1 for _ in range(N+1)]

for N in range(N-1):
  node = list(map(int,rl().split()))
  nodes[node[0]].append(node[1])
  nodes[node[1]].append(node[0])

def sol(idx):
  queue = deque()
  queue.append(idx)
  while queue:
    now = queue.popleft()
    if visited[now] == False:
      visited[now] = True
      for next in nodes[now]:
        if visited[next] == False:
          parent[next] = now
          queue.append(next)

sol(1)
for i in parent[2:]:
  print(i)