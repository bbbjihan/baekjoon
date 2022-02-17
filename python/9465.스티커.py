import sys;rl=sys.stdin.readline
T = int(rl())

for _ in range(T):
    n = int(rl())
    li = [list(map(int,rl().split()))]
    li.append(list(map(int,rl().split())))
    for i in range(1,n):
        if i == 1:
            li[0][i] += li[1][i-1]
            li[1][i] += li[0][i-1]
        else:
            li[0][i] += max(li[1][i-1], li[1][i-2])
            li[1][i] += max(li[0][i-1], li[0][i-2])
    print(max(li[0][n-1],li[1][n-1]))