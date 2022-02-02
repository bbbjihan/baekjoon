import sys
import math

N = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().rstrip().split()))

li.sort()
sum = 0

for i in range(len(li),0,-1):
    sum+=i*li[len(li)-i]

print(sum)