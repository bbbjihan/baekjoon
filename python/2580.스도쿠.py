import sys;rl=sys.stdin.readline

board = [list(map(int,rl().split()))for _ in range(9)]
track = []
iter_track = 0
for i in range(9):
    for j in range(9):
        if board[i][j] == 0 :
            track.append((i,j))

def promising(col,row,num):
    if num in board[row]:
        return False
    for line in board:
        if num == line[col]:
            return False
    start_col = (col//3)*3
    start_row = (row//3)*3
    for square_line in range(start_row,start_row+3):
        if num in board[square_line][start_col:start_col+3]:
            return False
    return True

def dfs(num):
    global iter_track
    if num == len(track):
        for i in range(9):
            print(*board[i])
        sys.exit()
    for i in range(1,10):
        if promising(track[iter_track][1],track[iter_track][0],i):
            board[track[iter_track][0]][track[iter_track][1]] = i
            iter_track+=1
            dfs(num+1)
            iter_track-=1
            board[track[iter_track][0]][track[iter_track][1]] = 0

dfs(0)