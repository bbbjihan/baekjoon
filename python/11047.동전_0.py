import sys
N,K = list(map(int,sys.stdin.readline().split()))
penny = []
for _ in range(N):
    penny.append(int(sys.stdin.readline()))
penny.sort(reverse=True)
cnt = 0
for i in penny:
    if K >= i:
        cnt+=K//i
        K-=i*(K//i)
print(cnt)