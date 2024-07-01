import sys;rl=sys.stdin.readline

N, K = map(int, rl().split())

field = [[False for _ in range(2 * N + 1)] for _ in range(2 * N + 1)]

commands = rl().strip()

x, y = 0, 0
for command in commands:
    if command == 'U':
        y -= 1
    elif command == 'D':
        y += 1
    elif command == 'L':
        x -= 1
    else:
        x += 1
    field[y + N][x + N] = True
    if x == 0 and y == 0:
        print('YES')
        exit()

offset_x, offset_y = x, y

def isInField(x, y):
    return 0 <= y + N <= 2 * N and 0 <= x + N <= 2 * N

x, y = 0, 0
for k in range(K):
    if not isInField(x, y):
        print('NO')
        break
    if field[N - y][N - x]:
        print('YES')
        break
    x += offset_x
    y += offset_y
else:
    print('NO')