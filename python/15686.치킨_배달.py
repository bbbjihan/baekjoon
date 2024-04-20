import sys;rl=sys.stdin.readline
from itertools import combinations
import math

N,M = list(map(int,rl().split(' ')))

field = []
houses = []
chickens = []
cnt = 0
for i in range(N):
  line = list(map(int, rl().split(' ')))
  field.append(line)
  for j in range(N):
    if line[j] == 1:
      houses.append([i,j])
    elif line[j] == 2:
      chickens.append([i,j, cnt])
      cnt += 1

scoresHouse = []
for house in houses:
  scoreHouse = [abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]) for chicken in chickens]
  scoresHouse.append(scoreHouse)

combis = combinations(range(cnt),M)

result = math.inf
for combi in combis:
  scoreCity = 0
  for score in scoresHouse:
    scoreHouse = math.inf
    for index in combi:
      scoreHouse = min(scoreHouse, score[index])
    scoreCity += scoreHouse
  result = min(result, scoreCity)

print(result)