import sys;rl=sys.stdin.readline

N = int(rl())

roads = list(map(int,rl().split()))
cities = list(map(int,rl().split()))

preCheapestCityIdx = 0
nowCheapestCityIdx = 0
cheapestPrice = cities[0]
cost = 0

for i in range(N):
    if cities[i] < cheapestPrice :
        preCheapestCityIdx = nowCheapestCityIdx
        nowCheapestCityIdx = i
        cost+= sum(roads[preCheapestCityIdx:nowCheapestCityIdx])*cheapestPrice
        cheapestPrice = cities[i]

if nowCheapestCityIdx < N-1:
    cost+= sum(roads[nowCheapestCityIdx:])*cheapestPrice

print(cost)