import sys;rl=sys.stdin.readline
from collections import deque

N = int(rl())
paint = []
for _ in range(N):
    paint.append(list(rl().rstrip()))

visited = [[False for _ in range(N)] for _ in range(N)]

def ordin(start_x,start_y,color):
    queue = deque()
    queue.append([start_x,start_y])
    while queue:
        x,y = queue.popleft()
        if 0<=x<N and 0<=y<N:
            if visited[y][x] == False and paint[y][x] == color:
                visited[y][x] = True
                queue.append([x+1,y])
                queue.append([x-1,y])
                queue.append([x,y+1])
                queue.append([x,y-1])

cnt1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            ordin(j,i,paint[i][j])
            cnt1+=1

visited = [[False for _ in range(N)] for _ in range(N)]

def blind(start_x,start_y):
    queue = deque()
    queue.append([start_x,start_y])
    while queue:
        x,y = queue.popleft()
        if 0<=x<N and 0<=y<N:
            if visited[y][x] == False and (paint[y][x] == 'R' or paint[y][x] == 'G'):
                visited[y][x] = True
                queue.append([x+1,y])
                queue.append([x-1,y])
                queue.append([x,y+1])
                queue.append([x,y-1])

cnt2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            if paint[i][j] == 'R' or paint[i][j] == 'G':
                blind(j,i)
                cnt2+=1
            else:
                ordin(j,i,'B')
                cnt2+=1

print(cnt1,cnt2)