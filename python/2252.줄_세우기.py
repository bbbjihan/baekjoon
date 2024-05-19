import sys;rl=sys.stdin.readline

N,M = map(int,rl().split())

edges = [[] for _ in range(N + 1)]
indegrees = [0 for _ in range(N + 1)]
for _ in range(M):
  start, end = map(int,rl().split())
  indegrees[end] += 1
  edges[start].append(end)

q = []


for i in range(1, N + 1):
  if indegrees[i] == 0:
    q.append(i)

visited = [ False for _ in range(N + 1) ]
res = []
while q:
  now = q.pop(0)
  visited[now] = True
  res.append(now)
  for next in edges[now]:
    if not visited[next]:
      indegrees[next] -= 1
      if indegrees[next] == 0:
        q.append(next)

print(*res)