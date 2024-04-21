import sys;rl=sys.stdin.readline
import math

V = int(rl())

vertDists = [[] for _ in range(V + 1)]

for _ in range(V):
  nodeNumber, *vertexes = list(map(int,rl().split(' ')))
  for i in range(len(vertexes)):
    if i % 2 == 0:
      if vertexes[i] == -1:
        break
      vertDists[nodeNumber].append([vertexes[i], vertexes[i+1]])

def getFarthestNodeUsingDfs(start):
  maxDist = 0
  node = 0
  stack = [[start, 0]]
  visited = [False for _ in range(V+1)]
  while len(stack) > 0:
    now, distNow = stack.pop()
    if visited[now]:
      continue
    
    visited[now] = True
    vertDistList = vertDists[now]
    for vert, dist in vertDistList:
      if visited[vert]:
        continue
      stack.append([vert,distNow + dist])
      if distNow + dist > maxDist:
        maxDist = distNow + dist
        node = vert
      maxDist = max(maxDist, distNow + dist)
  return maxDist, node

print(getFarthestNodeUsingDfs(getFarthestNodeUsingDfs(1)[1])[0])