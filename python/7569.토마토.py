import sys
from collections import deque

row,col,hei = list(map(int,sys.stdin.readline().split()))
box = []
for _ in range(hei):
    box.append([])
    for _ in range(col):
        box[len(box)-1].append(list(map(int,sys.stdin.readline().split())))

visited = [[[False for _ in range(row)] for _ in range(col)] for _ in range(hei)]
queue = deque()
max = 0

for i in range(hei):
    for j in range(col):
        for k in range(row):
            if box[i][j][k] == 1 and visited[i][j][k] == False:
                queue.append([i,j,k,0])
                box[i][j][k] = 0

while queue:
    node = queue.popleft()
    if node[0]<0 or node[1]<0 or node[2]<0 or node[0]>=hei or node[1]>=col or node[2]>=row or box[node[0]][node[1]][node[2]] == -1:
        continue
    if visited[node[0]][node[1]][node[2]] == False and box[node[0]][node[1]][node[2]] == 0:
        visited[node[0]][node[1]][node[2]] = True
        box[node[0]][node[1]][node[2]] = 1
        if max< node[3]:
            max = node[3]
        queue.append([node[0]+1,node[1],node[2],node[3]+1])
        queue.append([node[0]-1,node[1],node[2],node[3]+1])
        queue.append([node[0],node[1]+1,node[2],node[3]+1])
        queue.append([node[0],node[1]-1,node[2],node[3]+1])
        queue.append([node[0],node[1],node[2]+1,node[3]+1])
        queue.append([node[0],node[1],node[2]-1,node[3]+1])

for i in range(hei):
    for j in range(col):
        for k in range(row):
            if box[i][j][k] == 0:
                max = -1
                break

print(max)