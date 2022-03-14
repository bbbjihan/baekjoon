from copy import deepcopy
import sys;rl=sys.stdin.readline

N,M = map(int,rl().split())
tmp = []

def dfs(num):
    if num == M:
        print(' '.join(map(str,tmp)))
        return
    for i in range(N):
        tmp.append(i+1)
        dfs(num+1)
        tmp.pop()

dfs(0)