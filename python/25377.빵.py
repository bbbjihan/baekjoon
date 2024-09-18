N=int(input())
ans = 1001
for _ in range(N):
    a,b = map(int,input().split())
    if a <= b:
        ans = min(ans, b)
print(-1 if ans == 1001 else ans)