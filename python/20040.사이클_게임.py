import sys;rl=sys.stdin.readline

n, m = map(int,rl().split())

parents = [i for i in range(n)]

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

for i in range(m):
  a, b = map(int,rl().split())
  if getIsSameGroup(a, b):
    print(i + 1)
    break
  union(a, b)
else:
  print(0)