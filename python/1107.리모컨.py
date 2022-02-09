import sys;rl = sys.stdin.readline

N = int(rl())
M = int(rl())
ans = abs(N-100)

if M == 0:
    button = []
else:
    button = rl().rstrip().split()

for i in range(1000001):
    for j in str(i):
        if j in button:
            break
    else:
        ans = min(ans,len(str(i))+abs(N-i))

print(ans)