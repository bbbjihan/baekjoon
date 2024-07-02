import sys;rl=sys.stdin.readline

T = int(rl())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    R, C = map(int,rl().split())
    field = []
    for _ in range(R):
        field.append(list(map(int,list(rl().strip()))))
    
    adj_cubes = [[0 for _ in range(C)] for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if field[y][x] == 0:
                continue
            adj_cubes[y][x] += 2 * (field[y][x] - 1)
            for k in range(4):
                next_x = x + dx[k]
                next_y = y + dy[k]
                if next_x < 0 or next_x >= C or next_y < 0 or next_y >= R:
                    continue
                adj_cubes[y][x] += min(field[next_y][next_x], field[y][x])
    print((6 * sum(list(map(sum,field)))) - sum(list(map(sum,adj_cubes))))

# (6 * 큐브의 수) - (모든 큐브에 대해 각 큐브가 이웃한 큐브의 개수의 총합)