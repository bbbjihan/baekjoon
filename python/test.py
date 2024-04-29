import sys;rl=sys.stdin.readline

dx, dy = [[-1,1,0,0],[0,0,-1,1]]
R,C = map(int,rl().split())

board = []
for _ in range(R):
  board.append(list(rl().strip()))

usedAlphas = [False for _ in range(26)]

def dfs(Y,X, cnt):
  idx = ord(board[Y][X]) - 65
  if 0 <= Y <= R - 1 and 0 <= X <= C - 1 and not usedAlphas[idx]:
    usedAlphas[idx] = True
    ret = max([dfs(Y+dy[i], X+dx[i], cnt + 1) for i in range(4)])
    usedAlphas[idx] = False
    return ret
  else:
    return cnt

print(dfs(0,0,0))