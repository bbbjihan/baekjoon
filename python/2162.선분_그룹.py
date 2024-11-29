from collections import Counter

def getParent(num):
    if parents[num] != num:
        parents[num] = getParent(parents[num])
    return parents[num]

def getIsSameGroup(nodeA, nodeB):
    return getParent(nodeA) == getParent(nodeB)

def union(nodeA, nodeB):
    parentA, parentB = getParent(nodeA), getParent(nodeB)
    if parentA > parentB:
        parents[parentA] = parentB
    else:
        parents[parentB] = parentA

def getCCW(coordA, coordB, coordC):
    xA, yA = coordA
    xB, yB = coordB
    xC, yC = coordC
    
    z = (xB - xA) * (yC - yA) - (yB - yA) * (xC - xA)
    return 1 if z > 0 else -1 if z < 0 else 0

def getIsConnected(lineA, lineB):
    coordAA, coordAB = lineA[0:2], lineA[2:4]
    coordBA, coordBB = lineB[0:2], lineB[2:4]
    
    ccwA = getCCW(coordAA, coordAB, coordBA)
    ccwB = getCCW(coordAA, coordAB, coordBB)
    ccwC = getCCW(coordBA, coordBB, coordAA)
    ccwD = getCCW(coordBA, coordBB, coordAB)
    
    flagA = ccwA * ccwB
    flagB = ccwC * ccwD
    
    if flagA == 0 and flagB == 0:
        return (
            min(coordAA[0], coordAB[0]) <= max(coordBA[0], coordBB[0]) and
            min(coordBA[0], coordBB[0]) <= max(coordAA[0], coordAB[0]) and
            min(coordAA[1], coordAB[1]) <= max(coordBA[1], coordBB[1]) and
            min(coordBA[1], coordBB[1]) <= max(coordAA[1], coordAB[1])
        )
    
    return flagA <= 0 and flagB <= 0

N = int(input())

lines = [list(map(int,input().split())) for _ in range(N)]
parents = [i for i in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        if getIsSameGroup(i, j):
            continue
        lineA = lines[i]
        lineB = lines[j]
        
        IsConnected = getIsConnected(lineA, lineB)
        if IsConnected:
            union(i, j)

for i in range(N):
    getParent(i)

count = Counter(parents)
print(len(count))
print(max(count.values()))