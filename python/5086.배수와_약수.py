import sys;rl=sys.stdin.readline

while 1:
    a,b = map(int,rl().split())
    if a == 0 and b == 0 :
        break
    if a % b == 0 :
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")