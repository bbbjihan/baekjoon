import sys;rl=sys.stdin.readline

string1 = rl().rstrip()
string2 = rl().rstrip()
N = len(string1)
M = len(string2)

dp = [[0 for _ in range(M)] for _ in range(N)]
if string1[0] == string2[0]:
    dp[0][0] = 1
for i in range(N):
    if i > 0:
        dp[i][0] = dp[i-1][0]
        if string1[i] == string2[0]:
            dp[i][0] = 1
    for j in range(1,M):
        if string1[i] == string2[j]:
            if i > 0:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 1
        else:
            if i > 0:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
            else:
                dp[i][j] = dp[i][j-1]

print(dp[N-1][M-1])