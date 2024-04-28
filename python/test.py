import sys;rl=sys.stdin.readline

dx, dy = [[-1,1,0,0],[0,0,-1,1]]
R,C = map(int,rl().split())

board = []
for _ in range(R):
  board.append(list(rl().strip()))

alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
usedAlphas = {}
for alpha in alphas:
  usedAlphas[alpha] = False

visited=[[ False for _ in range(C) ] for _ in range(R)]
def dfs(Y,X):
  if 0 <= Y <= R - 1 and 0 <= X <= C - 1 and not usedAlphas[board[Y][X]]:
    visited[Y][X] = True
    usedAlphas[board[Y][X]] = True
    for i in range(4):
      dfs(Y+dy[i], X+dx[i])
    usedAlphas[board[Y][X]] = False

dfs(0,0)

print(sum(list(map(sum,visited))))