import sys;rl = sys.stdin.readline

def r(i):
  return int(i) + 1 if (i - int(i)) >= 0.5 else int(i)

n = int(rl())

levels = []

for _ in range(n):
  levels.append(int(rl()))
edge = r((n * 0.15))
levelsSorted = sorted(levels)
levelsValid = levelsSorted[edge: n - edge]

if len(levelsValid) == 0:
  print(0)
else:
  print(r(sum(levelsValid) / len(levelsValid)))