import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
li1 = [[] for i in range(n)]
li2 = [False for i in range(n)] #탐색한 적이 있는 경우 True로

for i in range(m):
    tmp = list(map(int,sys.stdin.readline().rstrip().split()))
    li1[tmp[0]-1].append(tmp[1])
    li1[tmp[1]-1].append(tmp[0])

def virus(index):
    if li2[index-1]:
        return
    else:
        li2[index-1] = True
        for i in li1[index-1]:
            virus(i)

virus(1)
print(sum(li2)-1)