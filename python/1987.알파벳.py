import sys;rl=sys.stdin.readline

dx, dy = [[-1,1,0,0],[0,0,-1,1]]
R,C = map(int,rl().split())

board = []
for _ in range(R):
  board.append(list(rl().strip()))

usedAlphas = [False for _ in range(26)]

def dfs(Y,X, cnt):
  if Y < 0 or Y > R - 1 or X < 0 or X > C - 1:
    return cnt
  
  idx = ord(board[Y][X]) - 65
  
  if usedAlphas[idx]:
    return cnt
  
  usedAlphas[idx] = True
  ret = 0
  for i in range(4):
    ret = max(ret, dfs(Y+dy[i], X+dx[i], cnt + 1))
  usedAlphas[idx] = False
  return ret

print(dfs(0,0,0))