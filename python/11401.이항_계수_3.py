import sys;rl=sys.stdin.readline

prime = 1000000007

def powerOfMod(base, exponent):
  if exponent == 0:
    return 1
  elif exponent % 2 == 1:
    return (powerOfMod(base, exponent - 1) * base) % prime

  a = powerOfMod(base, exponent // 2) % prime
  return a * a % prime

def getFactOfMod(num):
  ret = 1
  for i in range(1, num + 1):
    ret *= i
    ret %= prime
  return ret

N, K = list(map(int, rl().split(' ')))

print(getFactOfMod(N) * powerOfMod((getFactOfMod(N-K) * getFactOfMod(K)), prime-2) % prime)