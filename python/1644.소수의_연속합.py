import sys

rl = sys.stdin.readline

N = int(rl())

visited = [False] * (N + 1)
primes = []

for i in range(2, N + 1):
    if not visited[i]:
        primes.append(i)
        for j in range(i * 2, N + 1, i):
            visited[j] = True


cnt = 0
for i in range(len(primes)):
    S = 0
    for j in range(i, len(primes)):
        S += primes[j]
        if S == N:
            cnt += 1
            break
        if S > N:
            break

print(cnt)
