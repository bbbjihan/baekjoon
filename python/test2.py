import sys;rl=sys.stdin.readline
import math

a,b,c = map(int,rl().split())

max_power = int(math.log2(b))
dp = [1 for _ in range(max_power+1)]
dp[1] = a%c
for i in range(2,max_power+1):
    dp[i] = (dp[i-1]**2)%c

def sol(a,b,c): #(a^b)%c
    Log2 = math.log2(b)
    if int(Log2) == Log2:
        return dp[Log2]
    else:
        return (sol(a,2**Log2,c) * sol(a,b-2**Log2,c))%c

print(sol(a,b,c))