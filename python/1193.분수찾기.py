import math
import sys;rl=sys.stdin.readline
inp = int(rl().rstrip())
k = math.ceil((math.sqrt(inp*8+1)-1)/2)+1
l = ((k - 2) * (k - 1))//2
if k%2 == 1:
    print(str(inp-l)+'/'+str(k-inp+l))
else:
    print(str(k-inp+l)+'/'+str(inp-l))