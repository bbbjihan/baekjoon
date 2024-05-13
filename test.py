import sys;rl=sys.stdin.readline

n, m = map(int,rl().split())

vertexes = [[] for _ in range(n)]

visited = [False for _ in range(n)]

def getCircle(now, start):
  global visited
  
  nexts = vertexes[now]
  for next in nexts:
    if next == start:
      return True
    if visited[next]:
      continue
    visited[next] = True
    getCircle(next, start)
    visited[next] = False

for i in range(m):
  visited = [False for _ in range(n)]
  start, end = map(int,rl().split())
  vertexes[start].append(end)
  vertexes[end].append(start)
  visited[start] = True
  if getCircle(start):
    print(i+1)
    exit()

print(0)

