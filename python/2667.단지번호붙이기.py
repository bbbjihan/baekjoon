import sys
from collections import deque

N = int(sys.stdin.readline())
apart = []

for _ in range(N):
    apart.append(sys.stdin.readline().rstrip())
visited = [[False for _ in range(N)]for _ in range(N)]

def sol(row,col):
    queue = deque()
    queue.append((row,col))
    cnt = 0
    while queue:
        tmp = queue.popleft()
        if tmp[0] < 0 or tmp[1] < 0 or tmp[0] >= N or tmp[1] >= N or apart[tmp[0]][tmp[1]] == '0':
            continue
        elif visited[tmp[0]][tmp[1]] == False and apart[tmp[0]][tmp[1]] == '1':
            cnt+=1
            visited[tmp[0]][tmp[1]] = True
            queue.append((tmp[0]+1,tmp[1]))
            queue.append((tmp[0]-1,tmp[1]))
            queue.append((tmp[0],tmp[1]+1))
            queue.append((tmp[0],tmp[1]-1))
    return cnt

ans = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == False and apart[i][j] == '1':
            ans.append(sol(i,j))

print(len(ans))
ans.sort()
for i in ans:
    print(i)