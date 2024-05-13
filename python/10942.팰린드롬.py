import sys;rl=sys.stdin.readline

N = int(rl())
nums = list(map(int,rl().split()))

M = int(rl())
questions = []

for _ in range(M):
  questions.append(list(map(int,rl().split())))

dp = [[1 if i == j else 0 for i in range(N + 1)] for j in range(N + 1)]

for diff in range(1, N):
  for i in range(1, N + 1):
    j = i + diff
    if j > N:
      continue
    if diff == 1 and nums[i-1] == nums[j-1]:
      dp[i][j] = 1
      continue
    if dp[i + 1][j - 1] and nums[i-1] == nums[j-1]:
      dp[i][j] = 1

for S,E in questions:
  print(dp[S][E])
