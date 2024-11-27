import math

N,M = map(int,input().split())

for _ in range(N):
    x, y = map(int,input().split())
r,g,b = 0,0,0
for _ in range(M):
    x, y, z = input().split()
    if z == 'R':
        r += 1
    elif z == 'G':
        g += 1
    else:
        b += 1
u = r + math.ceil(g/2)
v = b + math.floor(g/2)
print('jhnah917' if u > v else "jhnan917")