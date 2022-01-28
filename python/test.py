import sys

N,M = map(int,sys.stdin.readline().split())

didnt_listen = []
didnt_see = []
didnt_listenandsee = []

for i in range(N):
    didnt_listen.append(sys.stdin.readline().rstrip())

for i in range(M):
    didnt_see.append(sys.stdin.readline().rstrip())

def dup(small,big,target):
    for i in small:
        for j in big:
            if i == j:
                target.append(i)

if N>M:
    dup(didnt_see,didnt_listen,didnt_listenandsee)
else:
    dup(didnt_listen,didnt_see,didnt_listenandsee)

didnt_listenandsee.sort()
print(len(didnt_listenandsee))
for i in didnt_listenandsee:
    print(i)