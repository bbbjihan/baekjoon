import sys;rl=sys.stdin.readline

N = int(rl())
rects = []
circles = []

for _ in range(N):
    inp = rl().split()
    if inp[0] == 'rectangle':
        t, x_1, y_1, x_2, y_2 = inp
        rects.append(((int(x_1), int(y_1)), (int(x_2), int(y_2))))
    else:
        t, x, y, r = inp
        circles.append((int(x), int(y), int(r)))

M = int(rl())
for _ in range(M):
    x, y = map(int,rl().split())
    cnt = 0
    
    for (x_1, y_1), (x_2, y_2) in rects:
        if x_1 <= x <= x_2 and y_1 <= y <= y_2:
            cnt += 1
    
    for x_o, y_o, r in circles:
        if (x - x_o) ** 2 + (y - y_o) ** 2 <= r ** 2:
            cnt += 1
    
    print(cnt)