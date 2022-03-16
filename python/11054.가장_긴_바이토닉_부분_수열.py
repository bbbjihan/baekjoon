import sys;rl=sys.stdin.readline

N = int(rl())
an = list(map(int,rl().split()))

def cntBitonic(mid):#idx를 기준으로 하는 가장 긴 바이토닉 수열의 길이
    leftMax = 0
    rightMax = 0
    if mid>0:
        for i in range(mid):
            Max = 0
            for j in range(i):
                if an[j] < an[i] and dp[j] > Max:
                    Max = dp[j]
            dp[i] = Max + 1
    if mid<N-1:
        for i in range(N-1,mid,-1):
            Max = 0
            for j in range(N-1,i,-1):
                if an[j] < an[i] and dp[j] > Max:
                    Max = dp[j]
            dp[i] = Max + 1

    for i in range(N):
        if i < mid:
            if an[i] < an[mid] and dp[i] > leftMax:
                leftMax = dp[i]
        else:
            if an[i] < an[mid] and dp[i] > rightMax:
                rightMax = dp[i]
    
    return leftMax + rightMax + 1

Max = 0
for i in range(N):
    dp = [0 for _ in range(N)]
    Max = max(Max,cntBitonic(i))

print(Max)