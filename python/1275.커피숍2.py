from math import log2
import sys;rl=sys.stdin.readline

N,Q = map(int,rl().split())
An = list(map(int,rl().split()))
leafLevel = int(log2(N))+2 #N = 5 -> leafLevel = 4
#bottom-up형태로 구현할 것이기 때문에 leaf의 level을 설정하여 필요한 크기의 트리를 초기화해줌.
#이 때 leafLevel의 최대 노드 수가 An의 길이보다 크거나 같은 가장 작은 2의 제곱수여야 함.
Tree = [[0,0,0] for _ in range(2**leafLevel)]
#트리의 각 노드는 [value,start,end]로 구간정보를 포함하고 있음.

def init():
    #리프노드를 채워줌.
    for nodeIndex in range(2**(leafLevel-1),2**(leafLevel)):
        n = nodeIndex - 2**(leafLevel-1)
        if n < N:
            Tree[nodeIndex] = [An[n],n+1,n+1]
        else:
            Tree[nodeIndex] = [0,n+1,n+1]
    #리프 위부터 각 level을 채워줌.
    level = leafLevel-1
    while level>0:
        for nodeIndex in range(2**(level-1),2**(level)):
            Tree[nodeIndex] = [Tree[nodeIndex*2][0]+Tree[nodeIndex*2+1][0],Tree[nodeIndex*2][1],Tree[nodeIndex*2+1][2]]
        level-=1

#node 내에 각 구간정보를 포함시켰으므로 query함수는 node의 구간을 파라미터로 받을 필요가 없다.
def query(nodeIndex,targetStart,targetEnd):
    nodeValue,nodeStart,nodeEnd = Tree[nodeIndex]
    #노드의 범위와 타겟의 범위가 하나도 겹치지 않는 경우 0을 rtn에 더한다.
    if targetEnd < nodeStart or nodeEnd < targetStart:
        return 0
    #노드의 범위가 타겟의 범위 안에 포함된 경우 노드의 value를 rtn에 더한다.
    elif targetStart <= nodeStart and nodeEnd <= targetEnd:
        return nodeValue
    #노드의 범위와 타겟의 범위의 일부에 겹쳐있는 경우 child의 구간을 확인하고 recursion sum하여 return.
    else:
        return query(nodeIndex*2,targetStart,targetEnd) + query(nodeIndex*2+1,targetStart,targetEnd)

def change(n,changeValue):
    #An의 n번째 원소에 대한 트리의 리프에서의 인덱스를 구함.
    nodeIndex = 2**(leafLevel-1)+n-1
    #리프노드에서부터 부모노드를 참조해가며 An의 n번째 원소를 포함한 모든 노드의 value를 수정해줌.
    while nodeIndex > 0:
        Tree[nodeIndex][0]+=changeValue-An[n-1]
        nodeIndex//=2
    An[n-1] = changeValue

init()
for _ in range(Q):
    x,y,a,b = map(int,rl().split())
    if y < x:
        print(query(1,y,x))
    else:
        print(query(1,x,y))
    change(a,b)