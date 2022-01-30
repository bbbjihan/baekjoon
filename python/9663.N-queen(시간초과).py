import sys #python으로 시간초과되어서 c++로 작성하여 제출함

N = int(sys.stdin.readline())

board = [0]*N
cnt = 0

def promising(rows):
    for i in range(rows):
        if board[rows] == board[i] or rows-i == abs(board[rows] - board[i]):
            return False
    return True

def confirm(k):
    if k==N:
        global cnt
        cnt+=1
        return
    else:
        for i in range(N):
            board[k] = i
            if promising(k):
                confirm(k+1)

confirm(0)
print(cnt)