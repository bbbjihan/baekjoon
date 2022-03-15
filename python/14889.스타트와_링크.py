import sys;rl=sys.stdin.readline

N = int(rl())
field = []
for _ in range(N):
    field.append(list(map(int,rl().split())))
 
visited = [False for _ in range(N)]
Min = 4000000

def make_com(num,idx):
    if num==(N//2):
        global Min
        stats = 0
        for member1 in range(N):
            for member2 in range(N):
                if visited[member1] and visited[member2]:
                    stats+=field[member1][member2]
                if not visited[member1] and not visited[member2]:
                    stats-=field[member1][member2]
        Min = min(Min,abs(stats))
        return
    for i in range(idx,N):
        if visited[i] == False:
            visited[i] = True
            make_com(num+1,i+1)
            visited[i] = False

make_com(0,0)

print(Min)