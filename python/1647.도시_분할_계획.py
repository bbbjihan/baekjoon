# 크루스칼 알고리즘: 간선 정렬
# -> 가중치가 가장 낮은 간선부터 그룹에 편입
# -> 이미 양끝 노드가 같은 그룹일 경우 continue
# -> 양끝 노드가 같은 그룹인 것은 Union Find로 확인

import sys;rl=sys.stdin.readline

N,M = map(int,rl().split())

vertexes = []
for _ in range(M):
  vertexes.append(list(map(int,rl().split())))
vertexes.sort(key=lambda x: x[2])

parents = [ i for i in range(N + 1) ]

def getParent(num):
  if parents[num] != num:
    parent = getParent(parents[num])
    parents[num] = parent
    return parent
  return num

def getIsSameGroup(nodeA, nodeB):
  return getParent(nodeA) == getParent(nodeB)

def union(nodeA, nodeB):
  parentA, parentB = getParent(nodeA), getParent(nodeB)
  if parentA < parentB:
    parents[parentB] = parentA
  else:
    parents[parentA] = parentB

maxCost = 0
sumCost = 0
cnt = 0
for start,end,cost in vertexes:
  if getIsSameGroup(start, end):
    continue
  union(start,end)
  sumCost += cost
  cnt += 1
  if maxCost < cost:
    maxCost = cost
  if cnt == N - 1:
    break

print(sumCost - maxCost)