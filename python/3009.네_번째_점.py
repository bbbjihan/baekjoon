import sys;rl=sys.stdin.readline

x = []
y = []

for _ in range(3):
    x0,y0 = map(int,rl().split())
    if x0 in x:
        del x[x.index(x0)]
    else:
        x.append(x0)
    if y0 in y:
        del y[y.index(y0)]
    else:
        y.append(y0)

print(x[0],y[0])