import sys;rl=sys.stdin.readline

N = int(rl())
needs = list(map(int,rl().split()))
T, P = map(int,rl().split())

t = 0
for need in needs:
    t += (need - 1) // T + 1

print(t)
print(N // P, N % P)