n = int(input())
bs = list(map(int,input().split()))

a = 1
flag = False
for b in bs:
    a = ( a * 2 ) - b
    if a < 0:
        flag = True
        break

print('error' if flag else a % 1000000007)