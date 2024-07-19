import sys;rl=sys.stdin.readline

N, K = map(int,rl().split())

cnt_level = {}
for _ in range(N):
    level = int(rl())
    cnt_level[level] = cnt_level[level] + 1 if level in cnt_level.keys() else 1

sorted_levels = sorted(cnt_level.keys())

index = 0
min_level = sorted_levels[index]
cnt_min_level = 0

while cnt_min_level < K and index < len(sorted_levels) - 1:
    min_level = sorted_levels[index]
    cnt_min_level += cnt_level[min_level]
    next_level = sorted_levels[index + 1]
    
    diff = (next_level - min_level) * cnt_min_level
    if diff > K:
        min_level += K // cnt_min_level
        break
    K -= (next_level - min_level) * cnt_min_level
    index += 1

print(min_level)