import sys;rl=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000000)

vertex_cnt,root_num,query_cnt = map(int,rl().split())

edges = [[] for _ in range(vertex_cnt + 1)]
children_cnts = [0 for _ in range(vertex_cnt + 1)]
for _ in range(vertex_cnt - 1):
    node_a,node_b = map(int,rl().split())
    edges[node_a].append(node_b)
    edges[node_b].append(node_a)

def dfs(now, parent):
    global edges, children_cnts
    children = edges[now]
    for child in children:
        if child != parent:
            children_cnts[now] += dfs(child, now)
    children_cnts[now]  += 1
    return children_cnts[now]

dfs(root_num, -1)

for _ in range(query_cnt):
    print(children_cnts[int(rl())])