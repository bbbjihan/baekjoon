import sys;rl=sys.stdin.readline
import itertools

n,m=map(int,rl().split())
li = list(map(int,rl().rstrip().split()))
it = itertools.permutations(li,m)
it = list(set(it))
it.sort()

for am in it:
  print(' '.join(map(str,am)))