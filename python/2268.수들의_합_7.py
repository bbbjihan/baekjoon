import sys;rl=sys.stdin.readline
import math

N, M = map(int,rl().split())

arr = [0 for _ in range(N+1)]

treeLength = 2 ** (int(math.log2(N)) + 2)
segTree = [0 for _ in range(treeLength)]

def Modify(start, end, node, i):
  if i < start or end < i:
    return 0
  if start == end:
    tmp = segTree[node]
    segTree[node] = arr[i]
    return arr[i] - tmp
  mid = int((start + end) / 2)
  diff = Modify(start, mid, node * 2, i) + Modify(mid + 1, end, node * 2 + 1, i)
  segTree[node] += diff
  return diff

def Sum(start, end, node, i, j):
  if j < start or i > end:
    return 0
  elif i <= start and end <= j:
    return segTree[node]
  else:
    mid = int((start + end) / 2)
    leftSum = Sum(start, mid, node * 2, i, j)
    rightSum = Sum(mid + 1, end, node * 2 + 1, i, j)
    return leftSum + rightSum

for _ in range(M):
  a,b,c = map(int,rl().split())
  if a == 0:
    if c > b:
      print(Sum(1,N,1,b,c))
    else:
      print(Sum(1,N,1,c,b))
  else:
    arr[b] = c
    Modify(1,N,1,b)