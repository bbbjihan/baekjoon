from collections import deque
from math import log2
import sys;rl=sys.stdin.readline
N,M,K = map(int,rl().split())
li = []
for _ in range(N):
    li.append(int(rl()))

#부분합 세그먼트 트리 초기화. 트리의 크기를 먼저 지정해주고, 리프노드부터 부모로 올라가며 값을 더해줌.
def init(level):
    if level == 0:
        return
    for i in range(2**(level-1),2**(level)):
        ST[i] = ST[i*2] + ST[i*2+1]
    init(level-1)
ST = [0 for _ in range(2**(int(log2(N))+2))]
ST[0] = None
ST[2**(int(log2(N))+1):2**(int(log2(N))+1)+len(li)] = li
init(int(log2(N))+1)

def change(index,value):
    #리스트의 인덱스에 해당하는 트리의 리프노드를 찾아, 모든 부모노드의 값에 목표 값을 더해줌.
    treeIndex = 2**(int(log2(N))+1)+index-1
    while treeIndex != 0:
        ST[treeIndex]-=li[index-1]-value
        treeIndex=treeIndex//2
    li[index-1]=value

def promising_for_query(nodeIdxInST,start,end):
    #노드의 인덱스로 노드가 포함한 구간을 구해서, 목표구간과의 포함관계를 리턴함.
    nodeLevel = int(log2(nodeIdxInST))+1
    left = right = nodeIdxInST
    while nodeLevel < int(log2(N))+2:
        left = left*2
        right = right*2+1
        nodeLevel+=1
    left -= 2**(nodeLevel-1)-1
    right -= 2**(nodeLevel-1)-1
    if start <= left and right <= end: #목표구간이 노드구간 내에 위치한 경우
        return 0
    if start > right or end < left: #목표구간과 노드구간이 아예 겹치지 않는 경우
        return 1
    else: #목표구간과 노드구간이 겹치는 경우
        return 2

def query_dfs(start,end,idx):
    global Sum
    if idx >= len(ST):
        return
    promising = promising_for_query(idx,start,end)
    if promising == 0:
        #목표구간이 노드구간 내에 위치한 경우, 노드의 구간합을 Sum에 더하고 리턴
        Sum+=ST[idx]
        return
    elif promising == 2:
        #목표구간과 노드구간이 아예 겹치는 경우, 좌우 좌식노드를 재귀시킴
        query_dfs(start,end,idx*2)
        query_dfs(start,end,idx*2+1)
    else:
        #목표구간과 노드구간이 아예 겹치지 않는 경우, 노드를 버림
        return

Sum = 0
for _ in range(M+K):
    command,a,b = map(int,rl().split())
    if command == 1:
        change(a,b)
    else:
        query_dfs(a,b,1)
        print(Sum)
        Sum = 0