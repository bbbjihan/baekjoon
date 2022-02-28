import sys
input = sys.stdin.readline

def Sol(v):
    mx, dp = v[0], v[0]
    for i in range(1, len(v)):
        dp = max(dp + v[i], v[i])
        mx = max(mx, dp)
    return mx

n, m = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(1, m):
        v[i][j] += v[i][j - 1]

mx = -1e9
for l in range(m):
    for r in range(l, m):
        pSum = [v[i][r] - (v[i][l - 1] if l else 0) for i in range(n)]
        mx = max(mx, Sol(pSum))
print(mx)