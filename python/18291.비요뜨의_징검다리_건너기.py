import sys;rl=sys.stdin.readline

prime = 1000000007

def powerOfMod(base, exponent):
  if exponent == 0:
    return 1
  elif exponent % 2 == 1:
    return (powerOfMod(base, exponent - 1) * base) % prime

  a = powerOfMod(base, exponent // 2) % prime
  return a * a % prime

T = int(rl())
for _ in range(T):
  N = int(rl())
  if N == 1 or N == 2:
    print(1)
  else:
    print(powerOfMod(2,N - 2))