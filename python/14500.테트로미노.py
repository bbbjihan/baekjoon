import sys;rl = sys.stdin.readline
from collections import deque
N,M = map(int,rl().split())
visited = [[False for _ in range(M)] for _ in range(N)]
field = []
for _ in range(N):
    field.append(list(map(int,rl().split())))
relative_T = [[[0,0],[0,-1],[0,1],[1,0]],[[0,0],[-1,0],[1,0],[0,1]],[[0,0],[0,1],[0,-1],[-1,0]],[[0,0],[0,-1],[-1,0],[1,0]]]

def get_sum_T(start_y,start_x):
    li = [0]
    for i in relative_T:
        tmp = 0
        flag = 0
        for j in i:
            if 0<=start_y+j[0]<N and 0<=start_x+j[1]<M:
                tmp+=field[start_y+j[0]][start_x+j[1]]
            else:
                flag = 1
                break
        if flag == 0:
            li.append(tmp)
    return max(li)

def get_sum_etc(start_y,start_x,distance,total):
    global max_sum
    if distance == 3:
        if total > max_sum:
            max_sum = total
    else:
        for i in range(4):
            ny = start_y + dy[i]
            nx = start_x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == False:
                    visited[ny][nx] = True
                    get_sum_etc(ny,nx,distance+1,total+field[ny][nx])
                    visited[ny][nx] = False

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
sum_field = []
max_sum = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        sum_field.append(get_sum_T(i,j))
        get_sum_etc(i,j,0,field[i][j])
        visited[i][j] = False

print(max(max(sum_field),max_sum))