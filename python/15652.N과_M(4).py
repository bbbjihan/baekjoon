import sys;rl=sys.stdin.readline
import itertools

n,m=map(int,rl().split())

it = itertools.combinations_with_replacement(range(1,n+1),m)

for am in it:
  
  print(' '.join(map(str,am)))