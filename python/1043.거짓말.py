import sys;rl=sys.stdin.readline
from collections import deque

N, M = list(map(int,rl().split(' ')))
knowTruthCnt, *knowTruths = list(map(int,rl().split(' ')))

relations = [set({_}) for _ in range(N + 1)]
parties = []
for _ in range(M):
  partyCnt, *party = list(map(int,rl().split(' ')))
  parties.append(party)
  for human in party:
    relations[human] = relations[human] | set(party)

knowTruthsAfterParty = [False for _ in range(N + 1)]
dq = deque(knowTruths)
while(len(dq) > 0):
  node = dq.popleft()
  if knowTruthsAfterParty[node]:
    continue
  knowTruthsAfterParty[node] = True
  for next in relations[node]:
    dq.append(next)

def getCanGo(party):
  for human in party:
    if knowTruthsAfterParty[human]:
      return False
  return True

print(list.count(list(map(getCanGo,parties)),True))