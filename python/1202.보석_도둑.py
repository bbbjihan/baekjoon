import sys

rl = sys.stdin.readline
import heapq

N, K = map(int, rl().split())

jewels = []
bags = []
for _ in range(N):
    jewels.append(list(map(int, rl().split())))
for _ in range(K):
    bags.append(int(rl()))
heapq.heapify(jewels)
heapq.heapify(bags)

ans = 0
q = []
while bags:
    bag = heapq.heappop(bags)
    while jewels and jewels[0][0] <= bag:
        _, price = heapq.heappop(jewels)
        heapq.heappush(q, -price)
    ans -= heapq.heappop(q) if q else 0

print(ans)
