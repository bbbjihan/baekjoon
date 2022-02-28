import sys;rl=sys.stdin.readline

N,M = map(int,rl().split())
checkpoint = []
for _ in range(N):
    checkpoint.append(int(rl()))
 
worstPoint = max(checkpoint)
totalTime = sum(checkpoint)

def isPossible(time):
    global M, totalTime
    return True

low = 0
high = worstPoint * M
mid = (low+high)//2

while low<high:
    if isPossible(mid):
        high = mid - 1
    else:
        low = mid + 1
    if low<high:
        break
    mid = (low+high)//2

