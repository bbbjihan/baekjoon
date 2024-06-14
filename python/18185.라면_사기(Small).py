import sys;rl=sys.stdin.readline

N = int(rl())
A = list(map(int,rl().split()))
A.extend([0, 0])

ans = 0

for i in range(N):
    if A[i+2] < A[i+1]:
        min_cnt = min(A[i], A[i+1] - A[i+2])
        A[i] -= min_cnt
        A[i+1] -= min_cnt
        ans += 5 * min_cnt
        min_cnt = min(A[i], A[i+1], A[i+2])
        if min_cnt > 0:
            A[i] -= min_cnt
            A[i+1] -= min_cnt
            A[i+2] -= min_cnt
            ans += 7 * min_cnt
    else:
        min_cnt = min(A[i], A[i+1], A[i+2])
        if min_cnt > 0:
            A[i] -= min_cnt
            A[i+1] -= min_cnt
            A[i+2] -= min_cnt
            ans += 7 * min_cnt
        min_cnt = min(A[i], A[i+1])
        if min_cnt > 0:
            A[i] -= min_cnt
            A[i+1] -= min_cnt
            ans += 5 * min_cnt

ans += sum(A * 3)
print(ans)