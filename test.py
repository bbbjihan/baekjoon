import sys;rl=sys.stdin.readline

n = int(rl())

vertexes = [[] for _ in range(n + 1)]
for _ in range(n - 1):
  a, b, dist = map(int,rl().split())
  vertexes[a].append([b, dist])
  vertexes[b].append([a, dist])

visited = [False for _ in range(n + 1)]

def dfs(node, dist):
  if visited[node]:
    visited[node] = False
    return node, dist
  visited[node] = True
  for nextNode, nextDist in vertexes[node]:
    a, b = dfs(nextNode, nextDist + dist)
    return a, max(dist, b)

a,b = dfs(1, 0)
print(max(b, dfs(a, 0)[1]))