from math import gcd
import sys;rl=sys.stdin.readline

N = int(rl())
rings = list(map(int,rl().split()))

for i in range(1,N):
    print(str(rings[0]//gcd(rings[0],rings[i]))+'/'+str(rings[i]//gcd(rings[0],rings[i])))