import sys #S(i~j) = S(0~i) - S(0~j-1)
import math

N,M = list(map(int,sys.stdin.readline().rstrip().split()))
li = list(map(int,sys.stdin.readline().rstrip().split()))
li2 = [0]
for i in range(1,N+1):
    li2.append(li2[i-1]+li[i-1])

for i in range(M):
    x,y = list(map(int,sys.stdin.readline().rstrip().split()))
    print(li2[y]-li2[x-1])