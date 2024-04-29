import sys;rl=sys.stdin.readline
import math
import copy

N,B = map(int,rl().split())

matrix = []
for _ in range(N):
  matrix.append(list(map(int,rl().split())))

def matrixMul(matA, matB):
  ret = [[0 for _ in range(N)] for _ in range(N)]
  for i in range(N):
    for j in range(N):
      S = 0
      for k in range(N):
        S += (matA[i][k] * matB[k][j])
      ret[i][j] = S % 1000
  return ret

pows = [[[1 if i == j else 0 for i in range(N)] for j in range(N)], copy.deepcopy(matrix)]
for _ in range(int(math.log2(B))):
  pows.append(matrixMul(pows[len(pows) - 1], pows[len(pows) - 1]))

def divide(cnt):
  if cnt <= 1:
    return pows[cnt]
  divBigest = int(math.log2(cnt))
  mod = cnt - (2 ** divBigest)
  return matrixMul(pows[divBigest + 1], divide(mod))

result = divide(B)

for i in range(N):
  for j in range(N):
    result[i][j] = result[i][j] % 1000

for i in range(N):
  print(*result[i])