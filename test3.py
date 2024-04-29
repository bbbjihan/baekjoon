import sys;rl=sys.stdin.readline

N,M = map(int,rl().split())
cards = list(map(int,rl().split()))

sum = 0
max = 0
for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M and sum > max:
                max = sum

print(max)