N = int(input())
A = list(map(int,input().split()))

dp = [1 for _ in range(N)]
find = [0]
for i in range(N):
    a = A[i]
    start, end = 0, len(find) - 1
    while start <= end:
        mid = (start + end) // 2
        if a == find[mid]:
            break
        elif a < find[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    if find[mid] < a:
        if mid < len(find) - 1:
            find[mid + 1] = a
        else:
            find.append(a)
        dp[i] = mid + 1
    else:
        find[mid] = a
        dp[i] = mid

print(max(dp))