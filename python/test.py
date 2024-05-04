import sys;rl=sys.stdin.readline
from collections import deque
import math

N,K = map(int,rl().split())

field = [math.inf for _ in range(300000)]

dq = deque([[N, 0]])
minDist = math.inf
cnt = 0
while dq:
  now, dist = dq.popleft()
  if now == K:
    if dist <= minDist:
      cnt += 1
      minDist = dist
    else:
      break
  
  if minDist < dist or field[now] < dist:
    continue
  
  field[now] = dist
  
  nextDist = dist + 1
  if nextDist <= minDist:
    if now > 1:
      dq.append([now - 1, nextDist])
    if now < 100000:
      dq.append([now + 1, nextDist])
      dq.append([now * 2, nextDist])

print(minDist if minDist < math.inf else (N-K))
print(cnt if cnt > 0 else 1)