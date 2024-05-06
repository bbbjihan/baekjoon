#(a_(n+1)) = (1 1)^n(a_1)
#(a_n)     = (1 0)  (a_0) 피보나치 수열 행렬로 구하기
import sys;rl=sys.stdin.readline
import math

mod = 1000000007
matrixC = [[1, 1],[1, 0]]

n = int(rl().strip())
def matrixMul(matA,matB):
  res = [[0 for _ in range(2)] for _ in range(2)]
  for i in range(2):
    for j in range(2):
      S = 0
      for k in range(2):
        S += (matA[i][k] * matB[k][j]) % mod
      res[i][j] = S % mod
  return res

pows = [[[1, 0], [0, 1]], [[1, 1], [1, 0]]]
for _ in range(int(math.log2(n))):
  pows.append(matrixMul(pows[len(pows) - 1], pows[len(pows) - 1]))

def divide(cnt):
  if cnt <= 1:
    return pows[cnt]
  divBigest = int(math.log2(cnt))
  mod = cnt - (2 ** divBigest)
  return matrixMul(pows[divBigest + 1], divide(mod))

print(divide(n)[0][1])