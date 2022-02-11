import sys;rl=sys.stdin.readline
n = int(rl())
an = list(map(int,rl().split()))

#dp[i] = i번째 원소까지 만들 수 있는 가장 긴 증가하는 부분수열의 길이
#앞에 있는 dp값 중에서 가장 크면서 i번째 원소보다 작은 값 + 1
dp = [0 for _ in range(n)]

for i in range(n):
  Max = 0
  for j in range(i):
    if an[j]<an[i] and dp[j]>Max:
      Max = dp[j]
  dp[i] = Max + 1

print(max(dp))