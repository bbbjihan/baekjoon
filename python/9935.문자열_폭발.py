import sys;rl=sys.stdin.readline

origin = rl().strip()
bomb = rl().strip()

res = []

def BOMB(res):
  lenSt = len(res)
  lenBomb = len(bomb)
  if lenSt < lenBomb:
    return
  
  for i in range(lenBomb):
    if res[lenSt - lenBomb + i] != bomb[i]:
      return
  
  del res[lenSt - lenBomb:]

lenBomb = len(bomb)

for c in origin:
  res.append(c)
  if c == bomb[lenBomb - 1]:
    BOMB(res)

print("".join(res) if len(res) else 'FRULA')