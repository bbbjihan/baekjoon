import sys
rl = sys.stdin.readline
N = int(rl())
li = []
for _ in range(N):
    li.append(list(map(int, rl().split())))
ans = [li[0]]
for i in range(1, N):
    tmp = []
    for j in range(len(li[i])):
        if j == 0:
            tmp.append(ans[i-1][0]+li[i][0])
        elif j == len(li[i])-1:
            tmp.append(ans[i-1][j-1] + li[i][j])
        else:
            tmp.append(max(ans[i-1][j]+li[i][j], ans[i-1][j-1]+li[i][j]))
    ans.append(tmp)

print(max(ans[len(ans)-1]))
