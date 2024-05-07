import sys;rl=sys.stdin.readline
import math

N = int(rl())
MAX = 1000001
cards = list(map(int,rl().split()))
cardIndex = [False for _ in range(MAX)]

for card in cards:
  cardIndex[card] = True

maxCard = max(cards)

points = [0 for _ in range(MAX)]

for i in range(MAX):
  if not cardIndex[i]:
    continue
  tmp = i * 2
  while tmp <= maxCard:
    if cardIndex[tmp]:
      points[i] += 1
      points[tmp] -= 1
    tmp += i

print(*list(map(lambda x: points[x], cards)))