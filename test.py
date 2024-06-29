import sys;rl=sys.stdin.readline

N, K = map(int,rl().split())

commands = rl().strip()

now = [0, 0]
for i in range(N):
    c = commands[i]
    if c == 'U':
        now[1] += 1
    elif c == 'D':
        now[1] -= 1
    elif c == 'L':
        now[0] -= 1
    else:
        now[0] += 1
    if now[0] == 0 and now[1] == 0:
        print("YES")
        break
else:
    print('NO')