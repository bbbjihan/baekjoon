from copy import deepcopy
import sys;rl=sys.stdin.readline

N,M = map(int,rl().split())

visited = [False for i in range(N)]
ans = []
tmp = []

def dfs(num):
    if num==M:
        ans.append(deepcopy(tmp))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            tmp.append(i+1)
            dfs(num+1)
            tmp.pop()
            visited[i] = False

dfs(0)

for com in ans:
    print(' '.join(map(str,com)))