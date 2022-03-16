import heapq
import sys;rl=sys.stdin.readline

N = int(rl())
sold = list(map(int,rl().split()))
heapq.heapify(sold)
ans = 1
while sold:
    tmp = heapq.heappop(sold)
    if ans != tmp:
        break
    ans+=1
print(ans)