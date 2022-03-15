import sys;rl=sys.stdin.readline

dp = [[[0 for _ in range(21)]for _ in range(21)]for _ in range(21)]

for a in range(21):
    for b in range(21):
        for c in range(21):
            if a == 0 or b == 0 or c == 0:
                dp[a][b][c] = 1
            elif a<b and b<c:
                dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
            else:
                dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]

while 1:
    a,b,c = map(int,rl().split())
    if a==-1 and b==-1 and c==-1:
        break
    string = 'w('+str(a)+', '+str(b)+', '+str(c)+') ='
    if a <= 0 or b <= 0 or c <= 0:
        print(string,1)
    elif a > 20 or b > 20 or c > 20:
        print(string,dp[20][20][20])
    else:
        print(string,dp[a][b][c])