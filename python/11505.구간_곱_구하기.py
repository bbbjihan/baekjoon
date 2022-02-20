from collections import deque
from math import log2
import sys;rl=sys.stdin.readline
N,M,K = map(int,rl().split())
li = []
for _ in range(N):
    li.append(int(rl()))

def init(level):
    if level == 0:
        return
    for i in range(2**(level-1),2**(level)):
        ST[i] = (ST[i*2] * ST[i*2+1])%1000000007
    init(level-1)
ST = [1 for _ in range(2**(int(log2(N))+2))]
ST[0] = None
ST[2**(int(log2(N))+1):2**(int(log2(N))+1)+len(li)] = li
init(int(log2(N))+1)
def change(index,value):
    treeIndex = 2**(int(log2(N))+1)+index-1
    ST[treeIndex] = value
    treeIndex=treeIndex//2
    while treeIndex != 0:
        ST[treeIndex] = (ST[treeIndex*2]*ST[treeIndex*2+1])%1000000007
        treeIndex=treeIndex//2
    if treeIndex == 0:
        li[index-1] = 1
    else:
        li[index-1]=value

def promising_for_query(nodeIdxInST,start,end):
    nodeLevel = int(log2(nodeIdxInST))+1
    left = right = nodeIdxInST
    while nodeLevel < int(log2(N))+2:
        left = left*2
        right = right*2+1
        nodeLevel+=1
    left -= 2**(nodeLevel-1)-1
    right -= 2**(nodeLevel-1)-1
    if start <= left and right <= end:
        return 0
    if start > right or end < left:
        return 1
    else:
        return 2

def query_dfs(start,end,idx):
    global Mul
    if idx >= len(ST):
        return
    promising = promising_for_query(idx,start,end)
    if promising == 0:
        Mul = (Mul * ST[idx])%1000000007
        return
    elif promising == 2:
        query_dfs(start,end,idx*2)
        query_dfs(start,end,idx*2+1)
    else:
        return

Mul = 1
for _ in range(M+K):
    command,a,b = map(int,rl().split())
    if command == 1:
        change(a,b)
    else:
        query_dfs(a,b,1)
        print(Mul)
        Mul = 1