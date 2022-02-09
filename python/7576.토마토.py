import sys
from collections import deque

row,col = list(map(int,sys.stdin.readline().split()))
box = []
for _ in range(col):
    box.append(list(map(int,sys.stdin.readline().split())))

visited = [[False for _ in range(row)] for _ in range(col)]

queue = deque()
max = 0

for i in range(col):
    for j in range(row):
        if box[i][j] == 1 and visited[i][j] == False:
            queue.append([i,j,0])
            box[i][j] = 0

while queue:
    node = queue.popleft()
    if node[0]<0 or node[0]>=col or node[1]<0 or node[1]>=row or box[node[0]][node[1]] == -1:
        continue
    if visited[node[0]][node[1]] == False and box[node[0]][node[1]] == 0:
        visited[node[0]][node[1]] = True
        box[node[0]][node[1]] = 1
        if max < node[2]:
            max = node[2]
        queue.append([node[0]-1,node[1],node[2]+1])
        queue.append([node[0]+1,node[1],node[2]+1])
        queue.append([node[0],node[1]-1,node[2]+1])
        queue.append([node[0],node[1]+1,node[2]+1])

for i in range(col):
    for j in range(row):
        if box[i][j] == 0:
            max = -1
            break

print(max)