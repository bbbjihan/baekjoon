n,m,k = map(int,input().split())
v=list(input().strip())
t=[False for _ in range(n)]

for i in range(n):
    c = v[i]
    if c == 'R':
        left=i-k
        right=i+k
        left=max(0,left)
        right=min(n-1,right)
        for j in range(left,right+1):
            t[j]=True

a = sum(t)
print('Yes' if m >= a else 'No')