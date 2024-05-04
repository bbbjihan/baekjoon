import sys;rl=sys.stdin.readline
import math

TC = int(rl())

for _ in range(TC):
  N,M,W = map(int,rl().split())
  
  vertexes = []
  for _ in range(M):
    S,E,T = map(int,rl().split())
    vertexes.append([S,E,T])
    vertexes.append([E,S,T])
  for _ in range(W):
    S,E,T = map(int,rl().split())
    vertexes.append([S,E,-T])
    
  dists = [0 for _ in range(N + 1)]
  
  res = False
  for i in range(1, N + 1):
    for fromNode, toNode, dist in vertexes:
      if dists[toNode] > dists[fromNode] + dist:
        dists[toNode] = dists[fromNode] + dist
        if i == N:
          res = True
  print('YES' if res else 'NO')