import sys;rl=sys.stdin.readline

N = int(rl())
ans = []

def sol(num):
    flag = 0
    if num == 1:
        return
    for i in range(2,(num//2)+1):
        if num%i == 0:
            ans.append(i)
            sol(num//i)
            flag = 1
            break
    if flag == 0 and num != 1:
        ans.append(num)

sol(N)
for A in ans:
    print(A)