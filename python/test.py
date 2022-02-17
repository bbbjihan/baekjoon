import sys;rl=sys.stdin.readline
N,S = map(int,rl().split())
An = list(map(int,rl().split()))

Sum = sum(An)
if Sum<S:
    print(0)
else:
    rightp = N
    while Sum>=S:
        rightp-=1
        Sum-=An[rightp]
    Sum+=An[rightp]
    ans = rightp+1

    for i in range(1,N):
        leng = rightp-i+1