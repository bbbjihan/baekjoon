# dfs로 횟수를 늘려가면서 탐색.
# dp로 값을 채울 때 인덱싱오류가 나지 않고 시간복잡도를 줄이는 형태로 구현
# dp[i] = min(min(dp[i-6:i])+1,ladder[i]+1,snake[i]+1)
import sys
from collections import deque
N,M = list(map(int,sys.stdin.readline().split()))
ladder = []
snake = []
for _ in range(N):
    ladder.append(list(map(int,sys.stdin.readline().split())))
for _ in range(M):
    snake.append(list(map(int,sys.stdin.readline().split())))

def jump(num): #num번째 칸으로 이동 시 jump되는 칸의 번호를 리턴하는 함수
    for i in ladder:
        if i[0] == num:
            return i[1]
    for i in snake:
        if i [0] == num:
            return i[1]
    return num

visited = [-1 for _ in range(101)]
queue = deque()
queue.append((1,0))
while queue:
    tmp = queue.popleft()
    if tmp[0]<1 or tmp[0]>100:
        continue
    elif tmp[0] == 100:
        break
    elif visited[tmp[0]] == -1:
        visited[tmp[0]] = tmp[1]
        for dx in range(1,7):
            queue.append((jump(tmp[0]+dx),tmp[1]+1))

print(tmp[1])