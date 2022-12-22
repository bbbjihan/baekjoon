import sys;rl=sys.stdin.readline

def isInner(x1,y1,Ox,Oy,r):
    if ((x1-Ox)**2)+((y1-Oy)**2) < r**2:
        return True
    return False

T = int(rl())

for _ in range(T):
    cnt = 0
    x1,y1,x2,y2 = map(int,rl().split())
    N = int(rl())
    for _ in range(N):
        Ox,Oy,r = map(int,rl().split())
        if isInner(x1,y1,Ox,Oy,r) != isInner(x2,y2,Ox,Oy,r):
            cnt+=1
    print(cnt)