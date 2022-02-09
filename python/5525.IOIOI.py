import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()

tmp = 0
flag = 0
ans = 0

for i in range(M):
    if flag == 1 and string[i] == 'O':
        continue
    elif string[i:i+3] == 'IOI':
        tmp+=1
        flag = 1
        if tmp == N:
            ans+=1
            tmp-=1
    else:
        tmp = 0
        flag = 0

print(ans)