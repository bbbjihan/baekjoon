import sys;rl=sys.stdin.readline

V,E = map(int,rl().split())
K = int(rl())
graph = [[200001 for _ in range(V)] for _ in range(V)]

for i in range(E):
  u,v,w = map(int,rl().split())
  if graph[u-1][v-1]>w:
    graph[u-1][v-1] = w

visited = [False for _ in range(V)]

def return_min_idx(li):
  Min = 200001
  Min_idx = -1
  for i in range(len(li)):
    if visited[i] == False and li[i]<Min:
      Min = li[i]
      Min_idx = i
  return Min_idx

def djikstra():
  for i in range(V):
    min_idx = return_min_idx(graph[K-1])
    visited[min_idx] = True
    for j in range(V):
      if graph[K-1][j] > graph[min_idx][j] + graph[K-1][min_idx]:
        graph[K-1][j] = graph[min_idx][j] + graph[K-1][min_idx]
  return 0

djikstra()
graph[K-1][K-1] = 0

for i in graph[K-1]:
  if i == 200001:
    print('INF')
  else:
    print(i)