import sys
import math

n = int(sys.stdin.readline())

for i in range(n):
    m = int(sys.stdin.readline())
    items = dict()
    for j in range(m):
        Name,Type = sys.stdin.readline().rstrip().split()
        if Type in items:
            items[Type].append(Name)
        else:
            items[Type] = [Name]
    
    ans = 1
    for j in items:
        ans*=len(items[j])+1
    ans-=1
    print(ans)
    
    