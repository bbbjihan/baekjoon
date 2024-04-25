import sys;rl = sys.stdin.readline
from collections import deque
n,k = map(int,rl().split())

MAX = 100001

field = [-1 for _ in range(MAX)]
dq = deque([n])

field[n] = 0

while dq:
  now = dq.popleft()
  
  if now == k:
    break
  
  teleport = now
  while 0 < teleport < MAX:
    if field[teleport] == -1:
      field[teleport] = field[now]
      dq.append(teleport)
    teleport *= 2
  
  if now - 1 > -1 and field[now - 1] == -1:
    field[now - 1] = field[now] + 1
    dq.append(now - 1)
  
  if now + 1 < MAX and field[now + 1] == -1:
    field[now + 1] = field[now] + 1
    dq.append(now + 1)

print(field[k])