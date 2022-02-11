import sys;rl=sys.stdin.readline
import itertools

n,m=map(int,rl().split())
li = list(map(int,rl().rstrip().split()))
li.sort()

it = itertools.permutations(li,m)

for am in it:
  
  print(' '.join(map(str,am)))