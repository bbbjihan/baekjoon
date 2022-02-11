import sys;rl=sys.stdin.readline
import itertools

n,m=map(int,rl().split())
li = list(map(int,rl().rstrip().split()))
it = itertools.combinations_with_replacement(li,m)
it = list(map(list,it))
for am in it:
  am.sort()
it = list(map(tuple,it))
it = list(set(it))
it.sort()

for am in it:
  print(' '.join(map(str,am)))