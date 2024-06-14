import sys;rl=sys.stdin.readline

def get_cost(A,B):
    xA,yA,zA = A
    xB,yB,zB = B
    return min(abs(xA-xB),abs(yA-yB),abs(zA-zB))

def _union(a,b):
    global parents
    parent_a = get_parent(a)
    parent_b = get_parent(b)
    if parent_a < parent_b:
        parents[parent_b] = parent_a
    else:
        parents[parent_a] = parent_b

def get_parent(node):
    global parents
    parent = parents[node]
    if parent != node:
        parent_parent = get_parent(parent)
        parents[node] = parent_parent
        return parent_parent
    return node

def get_is_same_parent(a,b):
    return get_parent(a) == get_parent(b)

N = int(rl())
parents = [i for i in range(N + 1)]
x = []
y = []
z = []
for i in range(N):
    x_p, y_p, z_p = list(map(int, rl().split()))
    x.append((x_p, i))
    y.append((y_p, i))
    z.append((z_p, i))

x.sort(key=lambda x:x[0])
y.sort(key=lambda x:x[0])
z.sort(key=lambda x:x[0])

edges = []
for i in range(1, N):
    edges.extend([(abs(x[i-1][0] - x[i][0]), x[i-1][1], x[i][1]), (abs(y[i-1][0] - y[i][0]), y[i-1][1], y[i][1]), (abs(z[i-1][0] - z[i][0]), z[i-1][1], z[i][1])])

edges.sort()
MST = []
total_cost = 0
iter = 0
while len(MST) < N - 1:
    edge = edges[iter]
    cost, p_from, p_to = edge
    if not get_is_same_parent(p_from, p_to):
        total_cost += cost
        _union(p_from, p_to)
        MST.append(edge)
    iter += 1

print(total_cost)