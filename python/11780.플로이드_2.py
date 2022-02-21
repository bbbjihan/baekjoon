import sys;rl=sys.stdin.readline
n = int(rl())
m = int(rl())
field = [[float('inf')for _ in range(n)]for _ in range(n)]
next = [[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    field[i][i] = 0
for _ in range(m):
    a,b,c = map(int,rl().split())
    if c < field[a-1][b-1]:
        field[a-1][b-1] = c
        next[a-1][b-1] = b


for i in range(n):
    for j in range(n):
        for k in range(n):
            if field[j][i] + field[i][k] < field[j][k]:
                field[j][k] = field[j][i] + field[i][k]
                next[j][k] = next[j][i]

def Lambda(x):
    if x == float('inf'):
        return 0
    return x
for i in range(n):
    print(' '.join(list(map(lambda x:str(Lambda(x)),field[i]))))

# i번 마을에서 j번 마을로 가는 최단경로
for i in range(n):
    for j in range(n):
        ans = [i]
        start = i
        flag = 0
        while ans[len(ans)-1] != j:
            if next[start][j] == 0:
                flag = 1
                break
            ans.append(next[start][j]-1)
            start = next[start][j]-1
        
        if flag == 1 or len(ans) == 1:
            print(0)
        else:
            print(str(len(ans))+' '+' '.join(list(map(lambda x:str(x+1),ans))))