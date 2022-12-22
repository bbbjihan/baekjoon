import sys;rl=sys.stdin.readline

N = int(rl())
MaxX = 0
MaxY = 0
MaxXi = 0
MaxYi = 0
inp = []

for i in range(6):
    inp.append(list(map(int,rl().split())))

for i in range(3):
    if inp[i*2][1] > MaxX:
        MaxX = inp[i*2][1]
        MaxXi = i*2
    if inp[i*2-1][1] > MaxY:
        MaxY = inp[i*2-1][1]
        MaxYi = i*2-1

S = MaxX*MaxY - inp[(MaxXi+3)%6][1]*inp[(MaxYi+3)%6][1]
print(S * N)