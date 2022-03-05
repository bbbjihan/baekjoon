import sys;rl=sys.stdin.readline
M = int(rl())
N = int(rl())
primeList = []
def isPrime(num):
    if num == 1:
        return False
    tmp = 2
    while tmp<num:
        if num%tmp == 0:
            return False
        tmp+=1
    return True

for num in range(M,N+1):
    if isPrime(num):
        primeList.append(num)

if primeList:
    print(sum(primeList))
    print(primeList[0])
else:
    print(-1)