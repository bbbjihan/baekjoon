import sys;rl=sys.stdin.readline

n = int(rl())

vertexes = [[] for _ in range(n + 1)]
for _ in range(n - 1):
  a, b, dist = map(int,rl().split())
  vertexes[a].append([b, dist])
  vertexes[b].append([a, dist])

def dfs(start):
  node, dist = 0, 0
  stack = [[start, 0]]
  visited = [False for _ in range(n + 1)]
  while stack:
    now, distAcc = stack.pop()
    if visited[now]:
      continue
    visited[now] = True

    for nodeNext, distNext in vertexes[now]:
      if visited[nodeNext]:
        continue
      stack.append([nodeNext, distAcc + distNext])
      if dist < distAcc + distNext:
        dist = distAcc + distNext
        node = nodeNext
    
  return node, dist

node, dist = dfs(1)
node2, dist2 = dfs(node)
print(max(dist, dist2))