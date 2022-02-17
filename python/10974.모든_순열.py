import sys;rl=sys.stdin.readline

N = int(rl())
visited = [False for _ in range(N)]
ans = []

def dfs(cnt):
  global ans
  if cnt == N:
    print(' '.join(ans))
    return
  else:
    for i in range(N):
      if visited[i] == False:
        visited[i] = True
        ans.append(str(i+1))
        dfs(cnt+1)
        ans.pop()
        visited[i] = False

dfs(0)