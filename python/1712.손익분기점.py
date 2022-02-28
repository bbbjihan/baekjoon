import sys;rl=sys.stdin.readline
a,b,c = map(int,rl().split())
if b>=c:
    print(-1)
else:
    print(int(a/(c-b)))