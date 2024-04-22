# C^(X-2) = C^(-1) (mod X)
import sys;rl=sys.stdin.readline

prime = 1000000007

def powerOfMod(base, exponent):
  if exponent == 0:
    return 1
  elif exponent % 2 == 1:
    return (powerOfMod(base, exponent - 1) * base) % prime

  a = powerOfMod(base, exponent // 2) % prime
  return a * a % prime

def getInverseOfMod(numerator, denominator):
  return (powerOfMod(numerator, prime - 2) * denominator) % prime

N = int(rl())
result = 0
for _ in range(N):
  num, denom = list(map(int, rl().split(' ')))
  result += getInverseOfMod(num ,denom)
  if result > prime:
    result -= prime

print(result)