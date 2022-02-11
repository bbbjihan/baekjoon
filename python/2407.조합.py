import sys;rl = sys.stdin.readline

n,m = map(int, rl().split())

fact = [1 for _ in range(n+1)]

for i in range(2,n+1):
    fact[i] = i * fact[i-1]

print(fact[n]//(fact[m]*fact[n-m]))