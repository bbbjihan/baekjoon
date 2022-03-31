from collections import deque
from math import gcd
import sys;rl=sys.stdin.readline

N = int(rl())
an = [int(rl()) for _ in range(N)]
an.sort()

Min = an[0]
ans = an[1]-an[0]

for i in range(2,N):
    ans = gcd(ans,(an[i]-Min))

ansFactor=[]
ansFactor2=deque()
for i in range(2,int(ans**(1/2))+1):
    if ans%i == 0:
        ansFactor.append(i)
        if ans//i != i:
            ansFactor2.appendleft(ans//i)
ansFactor2.append(ans)

print(' '.join(map(str,ansFactor+list(ansFactor2))))