x,y = map(int,input().split())
a = x / y
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    a = min(x / y, a)

print(a*1000)