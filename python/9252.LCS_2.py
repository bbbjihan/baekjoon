import sys;rl=sys.stdin.readline

str1 = rl().strip()
str2 = rl().strip()

N = len(str1)
M = len(str2)

dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
  for j in range(1, M + 1):
    if str1[i-1] == str2[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

res = []
max = 0

for i in range(1, N + 1):
  for j in range(1, M + 1):
    if max < dp[i][j]:
      max = dp[i][j]

i = N
j = M
while i > 0 and j > 0:
  if str1[i - 1] == str2[j - 1]:
    res.append(str1[i - 1])
    i -= 1
    j -= 1
  else:
    if dp[i][j] == dp[i-1][j]:
      i -= 1
    else:
      j -= 1

print(max)
if max > 0:
  print(''.join(res[::-1]))