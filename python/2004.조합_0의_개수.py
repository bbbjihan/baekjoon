import sys;rl=sys.stdin.readline

def getXInFact(num,x):
    rtn = 0
    tmp = num
    while 1:
        if tmp < x:
            break
        rtn+=tmp//x
        tmp//=x
    return rtn

n,r = map(int,rl().split())
n25 = [getXInFact(n,2),getXInFact(n,5)]
r25 = [getXInFact(r,2),getXInFact(r,5)]
nMr25 = [getXInFact(n-r,2),getXInFact(n-r,5)]
ans = [n25[0]-r25[0]-nMr25[0],n25[1]-r25[1]-nMr25[1]]

print(min(ans))