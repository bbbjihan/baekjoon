import sys;rl=sys.stdin.readline

N, M = map(int,rl().split())

rect = []
for _ in range(N):
  rect.append(list(rl().strip()))

longSide = max(N,M)
res = min(N,M)

if res == 1:
  print(res)
  exit()

while res > 0:
  offset = res - 1
  for i in range(N - offset):
    for j in range(M - offset):
      if rect[i][j] == rect[i + offset][j] == rect[i][j + offset] == rect[i + offset][j + offset]:
        print(res * res)
        exit()
  res -= 1