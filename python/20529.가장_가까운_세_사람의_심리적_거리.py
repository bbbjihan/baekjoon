import sys;rl=sys.stdin.readline
from itertools import combinations
import math
import copy

def getDist(ch1, ch2):
  return sum([1 if ch1[i] != ch2[i] else 0 for i in range(4)])

def getDist3(ch1,ch2,ch3):
  return getDist(ch1,ch2)+getDist(ch2,ch3)+getDist(ch1,ch3)

MBTIS = ["ENTP","ENTJ","ENFP","ENFJ","ESTP","ESTJ","ESFP","ESFJ","INTP","INTJ","INFP","INFJ","ISTP","ISTJ","ISFP","ISFJ"]
scores = [[[getDist3(MBTIS[i], MBTIS[j], MBTIS[k]) for i in range(16)] for j in range(16)] for k in range(16)]
nodes = [[MBTIS[i], MBTIS[j], MBTIS[k], getDist3(MBTIS[i], MBTIS[j], MBTIS[k])] for i in range(16) for j in range(16) for k in range(16)]
nodesSorted = sorted(nodes, key=lambda x: x[3])

T = int(rl())

for _ in range(T):
  N = int(rl())
  chs = rl().strip().split(' ')
  for node in nodesSorted:
    a, b, c, score = node
    if a in chs:
      indexA = chs.index(a)
      chs[indexA] = "XXXX"
      if b in chs:
        indexB = chs.index(b)
        chs[indexB] = "XXXX"
        if c in chs:
          print(score)
          break
        else:
          chs[indexB] = b
          chs[indexA] = a
      else:
        chs[indexA] = a
        