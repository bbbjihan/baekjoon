# O(N^2)
# https://www.acmicpc.net/problem/10025
import sys;rl=sys.stdin.readline

N, K = map(int,rl().split())

ice = []
for _ in range(N):
    weight, coord = map(int,rl().split())
    ice.append((coord,weight))

ice.sort(key=lambda x:x[0])
sum_range = 2 * K + 1
global_max = 0
break_flag = False

for i in range(N):
    if break_flag:
        break
    
    left, left_weight = ice[i]
    right = left + sum_range - 1
    local_sum = 0
    
    if right > ice[-1][0]:
        right = ice[-1][0]
        break_flag = True
    
    j = i
    while True:
        if j > N - 1:
            break
        now, now_weight = ice[j]
        if now > right:
            break
        local_sum += now_weight
        j += 1
    
    global_max = max(global_max, local_sum)

print(global_max)