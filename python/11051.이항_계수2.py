import sys;rl=sys.stdin.readline

a,b = map(int,rl().split())

fact = [1]

for i in range(1,a+1):
    fact.append((fact[i-1]*i))

print((fact[a]//(fact[a-b]*fact[b]))%10007)