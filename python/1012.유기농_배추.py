#deque을 활용한 BFS(너비우선탐색)
#출처: https://hongcoding.tistory.com/72
#더 공부해야될 점
#bfs가 활용되는 이유와 구체적인 구현방법
import sys 
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

T = int(sys.stdin.readline())

def bfs(N,M):
    cnt = 0
    for b in range(N):
        for a in range(M):
            if field[b][a] == 1:
                cnt+=1
                queue = deque()
                queue.append((a,b))
                field[b][a] = 0

                while queue:
                    x,y = queue.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx<0 or nx>=M or ny<0 or ny>=N:
                            continue
                        if field[ny][nx] == 1:
                            field[ny][nx] = 0
                            queue.append((nx,ny))
    return cnt

for _ in range(T):
    M,N,K = list(map(int,sys.stdin.readline().split()))
    field = [[0 for _ in range(M)] for _ in range(N)]
    arr = []
    for _ in range(K):
        arr.append(list(map(int,sys.stdin.readline().split())))
    
    for cabbage in arr: #배추심기
        field[cabbage[1]][cabbage[0]] = 1
    
    print(bfs(N,M))