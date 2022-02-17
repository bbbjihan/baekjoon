import sys;rl=sys.stdin.readline

N = int(rl())
visited = [False for _ in range(N)]

def dfs(cnt,x):
    global ans
    if cnt == N:
        print(' '.join(ans))
        ans = [str(x+1)]
        return
    else:
        for i in range(N):
            if visited[i] == False:
                visited[i] = True
                ans.append(str(i+1))
                dfs(cnt+1,x)
                visited[i] = False

for i in range(N):
    visited[i] = True
    ans = [str(i+1)]
    dfs(1,i)
    visited[i] = False