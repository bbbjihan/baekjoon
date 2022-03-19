import sys;rl=sys.stdin.readline

N = int(rl())
an = list(map(int,rl().split()))

Min = 1000001
Max = 0

for i in range(N):
    if an[i]>Max:
        Max = an[i]
    if an[i]<Min:
        Min = an[i]

print(Max*Min)