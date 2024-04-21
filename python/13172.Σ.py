import sys;rl=sys.stdin.readline

prime = 1000000007

def getInverseOfMod(numerator, denominator):
  a = denominator
  memo = 0
  while a % numerator != 0:
    memo += int(a / numerator)
    a %= numerator
    a += prime
  x = int(a / numerator) + memo
  return x

N = int(rl())
result = 0
for _ in range(N):
  num, denom = list(map(int, rl().split(' ')))
  result += getInverseOfMod(num ,denom)
  if result > prime:
    result -= prime

print(result)