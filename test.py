N = int(input())

lines = [list(map(int,input().split())) for _ in range(N)]

parents = [i for i in range(N)]

def getParent(num):
    if parents[num] != num:
        parent = getParent(parents[num])
        parents[num] = parent
        return parent
    return num

def getIsSameGroup(nodeA, nodeB):
    return getParent(nodeA) == getParent(nodeB)

def union(nodeA, nodeB):
    parentA, parentB = getParent(nodeA), getParent(nodeB)
    if parentA > parentB:
        parents[parentB] = parentA
    else:
        parents[parentA] = parentB

def getIsConnected(lineA, lineB):
    