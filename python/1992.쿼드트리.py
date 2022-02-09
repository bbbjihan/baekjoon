import sys

N = int(sys.stdin.readline())
paint = []

for _ in range(N):
    paint.append(sys.stdin.readline().rstrip())

queue = []

def is0or1(partition,length):
    if sum(list(map(int,partition))) == 0:
        return 0
    elif sum(list(map(int,partition))) == int('1'*length)*length:
        return 1

def zip(x,y,length):
    rtn = ''
    if length == 0:
        return
    part = length//2
    part1 = []
    part2 = []
    part3 = []
    part4 = []
    for i in range(part):
        part1.append(paint[y+i][x:x+part])
        part2.append(paint[y+i][x+part:x+length])
        part3.append(paint[y+i+part][x:x+part])
        part4.append(paint[y+i+part][x+part:x+length])
    if is0or1(part1,part) == 0:
        rtn+='0'
    elif is0or1(part1,part) == 1:
        rtn+='1'
    else:
        rtn+=zip(x,y,part)
    if is0or1(part2,part) == 0:
        rtn+='0'
    elif is0or1(part2,part) == 1:
        rtn+='1'
    else:
        rtn+=zip(x+part,y,part)
    if is0or1(part3,part) == 0:
        rtn+='0'
    elif is0or1(part3,part) == 1:
        rtn+='1'
    else:
        rtn+=zip(x,y+part,part)
    if is0or1(part4,part) == 0:
        rtn+='0'
    elif is0or1(part4,part) == 1:
        rtn+='1'
    else:
        rtn+=zip(x+part,y+part,part)
    
    return '('+rtn+')'

if is0or1(paint,N)==0:
    print(0)
elif is0or1(paint,N)==1:
    print(1)
else:
    print(zip(0,0,N))