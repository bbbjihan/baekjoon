import sys;rl = sys.stdin.readline
N = int(rl())
cards = list(map(int, rl().split(' ')))
M = int(rl())
numbers = list(map(int, rl().split(' ')))

cardDict = {}

for card in cards:
  if card in cardDict.keys():
    cardDict[card] += 1
  else:
    cardDict[card] = 1

result = []
for number in numbers:
  if number in cardDict.keys():
    result.append(cardDict[number])
  else:
    result.append(0)

print(*result)