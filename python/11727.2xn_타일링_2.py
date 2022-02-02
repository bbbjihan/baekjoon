import sys #DP, 일반항 dp[i] = dp[i-1] + dp[i-2]*2

n = int(sys.stdin.readline())
li = [0 for i in range(n)]
li[1:2] = [1,3]

for i in range(3,n+1):
    li[i] = (li[i-1] + li[i-2]*2)%10007

print(li[n])