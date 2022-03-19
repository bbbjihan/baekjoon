from math import gcd
import sys;rl=sys.stdin.readline

T = int(rl())
for _ in range(T):
    a, b =  map(int,rl().split())
    print((a*b)//gcd(a,b))