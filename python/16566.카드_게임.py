import sys;rl=sys.stdin.readline

N,M,K = map(int,rl().split())
cards = list(map(int,rl().split()))
CheolSu = list(map(int,rl().split()))

cards.sort()
parents = [ i for i in range(M + 1) ]

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

for i in range(K):
    card = CheolSu[i]
    left = 0
    right = M - 1
    while left <= right:
        mid = (left + right) // 2
        card_mid = cards[mid]
        
        if card < card_mid:
            right = mid - 1
        elif card > card_mid:
            left = mid + 1
        else:
            mid += 1
            break
    
    p = getParent(mid)
    print(cards[p])
    union(p, p + 1)