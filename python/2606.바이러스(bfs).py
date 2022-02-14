import sys;rl=sys.stdin.readline
from collections import deque

computers= int(rl())
web_cnt = int(rl())
networks = [[] for _ in range(computers+1)]
visited = [False for _ in range(computers+1)]

for _ in range(web_cnt):
  a,b = map(int,rl().split())
  networks[a].append(b)
  networks[b].append(a)

def virus(computer):
  queue = deque()
  queue.append(computer)
  while queue:
    now = queue.popleft()
    if visited[now] == False:
      visited[now] = True
      global cnt
      cnt+=1
      for next in networks[now]:
        queue.append(next)

cnt = 0
virus(1)
print(cnt-1)