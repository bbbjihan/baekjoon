#분할정복, 재귀함수
from math import log2
import sys
n = int(sys.stdin.readline())
paper = []
blue = 0
white = 0

for i in range(n):
    paper.append(list(map(int,sys.stdin.readline().rstrip().split())))

def sum_x_y(paper,x,y,len):
    sum = 0
    x = int(x)
    y = int(y)
    for i in range(x,x+len):
        for j in range(y,y+len):
            if paper[i][j]:
                sum+=1
    return sum

def confirm(paper,x,y,k):
    if k == -1:
        return
    else:
        size = 4 ** k
        sum = sum_x_y(paper,x,y,2**k)
        if sum == 0:
            global white
            white+=1
            return
        elif sum == size:
            global blue
            blue+=1
            return
        else:
            size = 2**(k-1)
            confirm(paper,x,y,k-1)
            confirm(paper,x+size,y,k-1)
            confirm(paper,x,y+size,k-1)
            confirm(paper,x+size,y+size,k-1)


confirm(paper,0,0,int(log2(n)))

print(white)
print(blue)