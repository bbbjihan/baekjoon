import sys;rl = sys.stdin.readline
from itertools import combinations
import copy
from collections import deque

[N,M] = list(map(int,rl().split(' ')))
lab = []

walls = []
viruses = []
empties = []
for i in range(N):
  line = list(map(int, rl().split(' ')))
  lab.append(line)
  for j in range(len(line)):
    if line[j] == 0:
      empties.append([i,j])
    elif line[j] == 1:
      walls.append([i,j])
    else:

combis = list(combinations(empties, 3))

maxResult = 0

for case in combis:
  nowLab = copy.deepcopy(lab)
  for wall in case:
    nowLab[wall[0]][wall[1]] = 1
  dq = deque()
  for virus in viruses:
    nowLab[virus[0]][virus[1]] = 0
    dq.append(virus)
  while(len(dq) > 0):
    i, j = dq.popleft()
    if i < 0 or i > N - 1 or j < 0 or j > M - 1 or nowLab[i][j] != 0:
      continue
    nowLab[i][j] = 2
    dq.append([i - 1, j])
    dq.append([i + 1, j])
    dq.append([i, j - 1])
    dq.append([i, j + 1])
  emptyCnt = 0
  for line in nowLab:
    emptyCnt += line.count(0)
  maxResult = max(emptyCnt, maxResult)

print(maxResult)