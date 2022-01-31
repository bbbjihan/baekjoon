#DP(N): return min(DP(N/2),DP(N/3),DP(N-1))
#상향식(Bottom-up) DP하여야 시간 절약 가능

import sys
n = int(sys.stdin.readline())
li = [0] * (n + 1)

for i in range(2,n+1):
    div2 = 999999999999
    div3 = 999999999999
    plus1 = li[i-1] + 1
    if i%2 == 0:
        div2 = li[i//2]+1
    if i%3 == 0:
        div3 = li[i//3]+1
    li[i] = min(plus1,div2,div3)

print(li[n])