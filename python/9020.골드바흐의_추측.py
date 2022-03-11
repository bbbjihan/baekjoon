import sys;rl=sys.stdin.readline

N = int(rl())
Primes = [True for _ in range(10001)]
for i in range(2,10000):
    if Primes[i]:
        x = i + i
        while x <= 10000:
            Primes[x] = False
            x += i

for _ in range(N):
    T = int(rl())
    if T == 4:
        print(2,2)
        continue
    elif T%4 == 0:
        a = T//2 + 1
        b = a - 2
    else:
        a = b = T//2
    while not Primes[a] or not Primes[b]:
        a = a + 2
        b = b - 2
    print(b,a)