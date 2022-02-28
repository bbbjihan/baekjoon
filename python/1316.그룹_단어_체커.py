import sys;rl=sys.stdin.readline
N = int(rl())
def isGroup(string):
    tmp = [string[0]]
    cntAlpha = string[0]
    for alpha in string:
        if alpha != cntAlpha:
            if alpha in tmp:
                return False
            else:
                tmp.append(alpha)
        cntAlpha = alpha
    return True

cnt = 0
for _ in range(N):
    inputString = rl().rstrip()
    if isGroup(inputString):
        cnt+=1

print(cnt)