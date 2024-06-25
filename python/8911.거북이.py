import sys;rl=sys.stdin.readline

T = int(rl())

def move(w, h, x, y, dir, isFront):
    if dir == 0:
        y = y + 1 if isFront else y - 1
        if not h[0] <= y <= h[1]:
            if isFront:
                h[1] += 1
            else:
                h[0] -= 1
    elif dir == 1:
        x = x + 1 if isFront else x - 1
        if not w[0] <= x <= w[1]:
            if isFront:
                w[1] += 1
            else:
                w[0] -= 1
    elif dir == 2:
        y = y - 1 if isFront else y + 1
        if not h[0] <= y <= h[1]:
            if isFront:
                h[0] -= 1
            else:
                h[1] += 1
    else:
        x = x - 1 if isFront else x + 1
        if not w[0] <= x <= w[1]:
            if isFront:
                w[0] -= 1
            else:
                w[1] += 1
    
    return w, h, x, y

for _ in range(T):
    commands = rl()
    w, h, x, y, dir = [0, 0], [0, 0], 0, 0, 0 # 0Up, 1Right, 2Down, 3Left
    for command in commands:
        if command == 'F':
            w, h, x, y = move(w, h, x, y, dir, True)
        elif command == 'B':
            w, h, x, y = move(w, h, x, y, dir, False)
        elif command == 'L':
            dir = (dir - 1) % 4
        elif command == 'R':
            dir = (dir + 1) % 4
    
    print(abs(w[1] - w[0]) * abs(h[1] - h[0]))