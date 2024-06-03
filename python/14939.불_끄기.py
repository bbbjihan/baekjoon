import sys;rl=sys.stdin.readline
import copy

board = []
for _ in range(10):
    board.append(list(map(lambda x: x == 'O', rl().strip())))

ans = 101

dx = [-1 , 1, 0, 0]
dy = [0, 0, -1, 1]

def push_switch(board, y, x):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 10 and 0 <= ny < 10:
            board[ny][nx] = not board[ny][nx]
    board[y][x] = not board[y][x]

for i in range(2 ** 10):
    local_board = copy.deepcopy(board)
    cnt = 0
    push_first_line = bin(i)[2:].zfill(10)
    for j in range(10):
        if push_first_line[j] == '1':
            push_switch(local_board, 0, j)
            cnt += 1
    if cnt > ans:
        continue
    for j in range(1, 10):
        for k in range(10):
            if local_board[j-1][k]:
                push_switch(local_board, j, k)
                cnt += 1
        if any(local_board[j-1]):
            break
        if cnt > ans:
            break
    else:
        if not any(local_board[-1]) and cnt < ans:
            ans = cnt

print(ans if ans < 101 else -1)