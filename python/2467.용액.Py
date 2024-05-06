import sys;rl=sys.stdin.readline
import math

N = int(rl())

liquids = list(map(int,rl().split()))

pair = [liquids[0], liquids[-1]]

def binSearch(num):
  start = 0
  end = N
  while start < end:
    mid = int((start + end) / 2)
    if num == liquids[mid]:
      return True, mid
    elif num < liquids[mid]:
      end = mid - 1
    else:
      start = mid + 1
  return False, mid

nearstZero = math.inf
pair = [-1, -1]
for liquid in liquids:
  target = - liquid
  isSumZero, index = binSearch(target)
  if isSumZero:
    pair = [liquid, target]
    break
  
  for i in [index - 1, index, index + 1]:
    if 0 <= i <= N-1:
      now = liquids[i]
      if liquid != now and nearstZero > abs(now + liquid):
        nearstZero = abs(now + liquid)
        pair = [liquid, now]

pair.sort()
print(*pair)