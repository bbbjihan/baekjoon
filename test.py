import sys;rl=sys.stdin.readline

N = int(rl())

treeD = {}
globalMax = 0
globalPair = [('',200001),('',200001)]

def findPair(candidates, nowDepth, origin):
  if "origin" in nowDepth.keys():
    candidate = nowDepth["origin"]
    if candidate[0] != origin:
      candidates.append(candidate)
  for key in nowDepth.keys():
    if key == 'origin':
      continue
    findPair(candidates, nowDepth[key], origin)

for i in range(N):
  string = rl().strip()
  nowDepth = treeD
  
  maxCnt = globalMax
  splitDepth = 0
  for j in range(len(string)):
    char = string[j]
    if char in nowDepth.keys():
      maxCnt = max(maxCnt, j + 1)
      splitDepth = j + 1
    else:
      nowDepth[char] = {}
    nowDepth = nowDepth[char]
  nowDepth["origin"] = (string,i)
  
  if globalMax <= maxCnt:
    
    nowDepth = treeD
    for j in range(splitDepth):
      nowDepth = nowDepth[string[j]]
    candidates = []
    findPair(candidates, nowDepth, string)
    
    if len(candidates) == 0:
      continue
    
    candidates.sort(key=lambda x: x[1])
    pair = [candidates[0],(string, i)]
    
    if globalMax < maxCnt:
      globalMax = maxCnt
      globalPair = pair
      continue
    
    if pair[0][1] < globalPair[0][1]:
      globalPair = pair
    elif pair[0][1] == globalPair[0][1]:
      if globalPair[1][1] > globalPair[1][1]:
        globalPair = pair

for s in globalPair:
  print(s[0])