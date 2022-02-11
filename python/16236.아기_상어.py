import sys;rl = sys.stdin.readline
from collections import deque
import math
N = int(rl())
field = []

for _ in range(N):
    field.append(list(map(int,rl().split())))

shark_level = 2
shark_feed = 0
time = 0

def shark_lvup():
    global shark_level,shark_feed
    if shark_feed == shark_level:
        shark_level+=1
        shark_feed = 0

def check_feed(shark_level):
    tmp = list(set(sum(field,[])))
    for i in tmp:
        if 0 < i < shark_level:
            return True
    return False

def proximate(start_y,start_x):
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append((start_y,start_x,0))
    global time, shark_level, shark_feed, shark
    prox_dis = math.inf
    prox_li = []
    while queue:
        y,x,dis = queue.popleft()
        if 0<=y<N and 0<=x<N:
            if dis <= prox_dis:
                if 0 < field[y][x] < shark_level:
                    prox_dis = dis
                    prox_li.append([y,x])
                if visited[y][x] == False and (field[y][x] == 0 or field[y][x] == shark_level):
                    visited[y][x] = True
                    queue.append((y-1,x,dis+1))
                    queue.append((y,x+1,dis+1))
                    queue.append((y,x-1,dis+1))
                    queue.append((y+1,x,dis+1))
    if any(prox_li):
        prox_li.sort(key=lambda x:(x[0],x[1]))
        y,x = prox_li[0][0],prox_li[0][1]
        field[y][x] = 0
        shark_feed+=1
        time+=prox_dis
        shark_lvup()
        shark = [y,x]
    else:
        global can_feed
        can_feed = False
    return

for i in range(N):
    for j in range(N):
        if field[i][j] == 9:
            shark = [i,j]
            field[i][j] = 0

can_feed = check_feed(shark_level)

while 1:
    if can_feed == False:
        break
    can_feed = check_feed(shark_level)
    proximate(shark[0],shark[1])

print(time)