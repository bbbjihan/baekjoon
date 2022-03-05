import sys;rl=sys.stdin.readline
inp = int(rl())
if inp != 1:
    op = 2
    tmp = inp
    while op<(inp)//2+1:
        if tmp%op == 0:
            print(op)
            tmp = tmp//op
        else:
            op+=1