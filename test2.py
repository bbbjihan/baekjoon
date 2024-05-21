import sys;rl=sys.stdin.readline

N = int(rl())

treeD = {}
globalMax = 0
pair = ['','']

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
  
  if globalMax < maxCnt:
    globalMax = maxCnt
    pair[1] = string
    
    nowDepth = treeD
    for j in range(splitDepth):
      nowDepth = nowDepth[string[j]]
    candidates = []
    findPair(candidates, nowDepth, string)
    if len(candidates) > 0:
      candidates.sort(key=lambda x: x[1])
      pair[0] = candidates[0][0]

for s in pair:
  print(s)